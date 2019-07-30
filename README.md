# Raincaller

This library provides a data augmentation suites for Natural Language Processsing tasks including:

- Text classification
- Speech recognition

# Text Classification
- Character level augmentation
- Word level augmentation

Character level augmentations include insertion, omission (and replacement and swap).

- `safe_checker`
Some characters must not be processed by this blind folded approach. The `safe_checker` module provides helpers to ensure that critical parts of a sentence remain intact.

- `distribution`
This module derives ditributions from given base dataset. The distributions can be later used in data augmentations providing sound assumptions to its process.

- `measures`
This modules provides set of metrics to evaluate statiscal properties of (augmented) dataset.