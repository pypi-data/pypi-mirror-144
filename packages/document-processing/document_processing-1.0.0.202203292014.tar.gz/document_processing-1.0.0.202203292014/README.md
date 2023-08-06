# `document_processing`

This package provides functions to pre-process text for various NLP tasks. It uses [`spaCy`](https://spacy.io/) and its models to analyse the text.

## Behaviour

The entry point of this package is `process_dcouments` in which you put the `Series` of documents to process and the `spaCy` model name that will be loaded to transform the texts.

From a document, you can extract tokens, lemmas and entities with the `get_tokens_lemmas_entities_from_document` function, giving it the document returned by the previous function, and the preprocessing function, as described below.

### Pre-processing functions

- `preprocess_list_of_texts`: process tokens, remove stopwords, non-standard characters, etc.
- `preprocess_list_of_tweets`: same as above, and remove all token that seem to be HTTP links, which are often present in Tweets.

