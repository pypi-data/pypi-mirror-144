## Infrastructure

- Recreate `krasserm-perceiver-io` environment
- Use `jsonargparse[signatures]` dependency instead of `pytorch-lightning[extra]`.
- Compare PR with local changes on `Borda-refactor/pkg-local` 
- Read https://medium.com/geekculture/thought-on-why-code-formatting-is-important-even-more-for-open-source-476829b54eaf
- Get familiar with
  - GitHub actions
  - pre-commit utility

## Features

- Train on GoEmotions dataset
  - https://ai.googleblog.com/2021/10/goemotions-dataset-for-fine-grained.html
  - https://www.marktechpost.com/2021/11/05/google-ai-introduces-goemotions-an-nlp-dataset-for-fine-grained-emotion-classification/
- Create sequence batches with minimal padding
- Use LAMB optimizer
