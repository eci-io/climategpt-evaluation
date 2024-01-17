import datasets
import numpy as np
import logging
from sklearn.metrics import f1_score

def filter_multi(dataset: datasets.Dataset) -> datasets.Dataset:
    # Only supports and refutes
    return dataset.filter(lambda example: example["label"] in [0,1,2,3,4])

def f1(predictions, references):  # This is a passthrough function
    return (predictions[0], references[0])

def agg_f1(items):

    predictions, references = zip(*items)
    logging.info(f"predictions: {predictions}")
    logging.info(f"references: {references}")
    references, predictions = np.asarray(references), np.asarray(predictions)

    return f1_score(references, predictions, average='macro')
