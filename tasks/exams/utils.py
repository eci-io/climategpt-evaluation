import datasets
from ast import literal_eval 

def relabel_labels(example):
    example["choices"] = literal_eval(example["choices"])
    example["answer"]= example["choices"]["label"].index(example["answerKey"].lstrip())
    return example

def process_docs_filter_science(dataset: datasets.Dataset) -> datasets.Dataset:
    dataset = dataset.filter(lambda x: x['subject'] == 'Science')
    dataset = dataset.map(relabel_labels, batched=False)
    return dataset

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    dataset = dataset.map(relabel_labels, batched=False)
    return dataset

