# `document_tracking_resources`

This package is part of the `news_tracking` project and aims at providing the necessary resources for algorithms to run and data preparation.

## Data format

Document tracking algorithms use two classes, `NewsCorpus` and `TwitterCorpus` respectively for news articles data (with title and content) and tweets. A corpus is to be seen as a table of elements that comprises, at least, three categories of elements:

  * Document **characteristics**: the columns that correspond to the document itself: date of publication, title, text, source, etc. See the `DOCUMENT_COLUMNS` property.
  * Document **features**: the different computed features (either TF-IDF weightings or dense representation for instance) that represent the multiple dimensions of the documents (title, text or both) of the original corpus. See the `FEATURE_COLUMNS` property.
  * Document **cluster**: the ground truth cluster id of each document, in order to train and test the corpus. See the `GROUND_TRUTH_COLUMNS` property.

This data format relies on the `pandas` library, especially the `DataFrame` data structure. It is generally saved in `.pickle` format in order to make it easy to load and save the structure. The `Corpus` API provides functions to load `DataFrame` in `.pickle` format as a `Corpus`.

### Features format

The features of the `Corpus` are column named after the `FEATURES_COLUMNS` list. This package allows manipulating two kind of data different features:

* **Sparse**: generally produced via a TF-IDF weighting model, the sparse representation is saved as a mapping, for each dimension (title, text or both) between the feature to weight (the tokens for instance) and its weight. Each dimension is then a dictionary of all the terms and their weightings.
* **Dense**: vectors of equal size that provide a representation, as a vector of number of each dimension of the original document (title, text or both).
