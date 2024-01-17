import datasets
import numpy as np
import sklearn.metrics

def select_first_1100(dataset: datasets.Dataset) -> datasets.Dataset:
    # Only supports and refutes
    return dataset.shuffle(42).select(range(1100))

def filter_multi(dataset: datasets.Dataset) -> datasets.Dataset:
    # Only supports and refutes
    return dataset.filter(lambda example: example["label"] in [0,1])

def filter_main(dataset: datasets.Dataset) -> datasets.Dataset:
    dataset = select_first_1100(dataset)
    return filter_multi(dataset)

def f1(predictions, references):  # This is a passthrough function

    _prediction = predictions[0]
    _reference = references[0]
    print(f"_prediction: {_prediction}")
    print(f"_reference: {_reference}")
    string_label = ['no', 'yes']
    reference = string_label.index(_reference)
    prediction = (
        string_label.index(_prediction)
        if _prediction in string_label
        else not bool(reference)
    )

    return (prediction, reference)

def agg_f1(items):

    predictions, references = zip(*items)
    references, predictions = np.asarray(references), np.asarray(predictions)

    return sklearn.metrics.f1_score(references, predictions, average='macro')