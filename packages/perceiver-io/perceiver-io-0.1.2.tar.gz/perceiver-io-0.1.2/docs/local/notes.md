## Per GPU memory usage

- settings:
  - batch_size=64
  - precision=32
  - num_encoder_layers=2

- baseline: 7635M
- activation checkpointing + DDP: 5895M
- activation checkpointing + DDPSharded: 5895M
- activation checkpointing + FSDP: 5895M

## Distributed training

```shell
python -m torch.distributed.run \
  --nnodes=2 \
  --master_addr 192.168.94.50 \
  --master_port 1234 \
  --node_rank 0 \
  train/train_mlm.py --dataset=imdb --learning_rate=1e-3 --max_epochs=100 --max_seq_len=512 --batch_size=64 --dropout=0.0 --weight_decay=0.0 --accelerator=ddp --gpus=1 --num_nodes=2 --experiment=tmp

python -m torch.distributed.run \
  --nnodes=2 \
  --master_addr 192.168.94.50 \
  --master_port 1234 \
  --node_rank 1 \
  train/train_mlm.py --dataset=imdb --learning_rate=1e-3 --max_epochs=100 --max_seq_len=512 --batch_size=64 --dropout=0.0 --weight_decay=0.0 --accelerator=ddp --gpus=1 --num_nodes=2 --experiment=tmp
```

## jsonargparse

```python
...
```

## Misc

python scripts/mlm.py fit \
  --model.num_latent_channels=64 \
  --model.encoder.num_layers=3 \
  --model.encoder.dropout=0.0 \
  --model.decoder.dropout=0.0 \
  --data=IMDBDataModule \
  --data.max_seq_len=512 \
  --data.batch_size=64 \
  --optimizer.lr=0.003 \
  --optimizer.weight_decay=0.0 \
  --lr_scheduler.pct_start=0.1 \
  --trainer.accelerator=gpu \
  --trainer.devices=-1 \
  --trainer.max_steps=50000 \
  --trainer.check_val_every_n_epoch=1

python scripts/seq_clf.py fit \
  --model.mlm_ckpt=... \
  --model.num_latent_channels=64 \
  --model.encoder.num_layers=3 \
  --model.encoder.dropout=0.0 \
  --model.encoder.freeze=true \
  --model.decoder.dropout=0.0 \
  --data=IMDBDataModule \
  --data.max_seq_len=512 \
  --data.batch_size=128 \
  --optimizer.lr=0.001 \
  --optimizer.weight_decay=0.01 \
  --trainer.accelerator=gpu \
  --trainer.devices=-1 \
  --trainer.max_epochs=30

python scripts/seq_clf.py fit \
  --model.clf_ckpt=... \
  --model.num_latent_channels=64 \
  --model.encoder.num_layers=3 \
  --model.encoder.dropout=0.0 \
  --model.decoder.dropout=0.0 \
  --data=IMDBDataModule \
  --data.max_seq_len=512 \
  --data.batch_size=128 \
  --optimizer.lr=0.0001 \
  --optimizer.weight_decay=0.01 \
  --trainer.accelerator=gpu \
  --trainer.devices=-1 \
  --trainer.max_epochs=30