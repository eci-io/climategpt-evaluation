import datasets
import numpy as np
import sklearn.metrics

cols_to_remove = ['id_qa', 'corpus', 'question_pt_origin', 'question_en_paraphase', 'question_pt_paraphase', 'answer_en_origin', 'answer_pt_origin', 'answer_en_validate', 'answer_pt_validate', 'eid_article_scopus', 'question_generic', 'answer_in_text', 'answer_difficulty', 'question_meaningful', 'answer_equivalent', 'question_type', 'abstract_translated_pt', 'pt_question_translated_to_en']

def f1(predictions, references):  # This is a passthrough function
    return (predictions[0], references[0])

    # _prediction = predictions[0]
    # _reference = references[0]
    # string_label = ['A', 'B', 'C', 'D', 'E']
    # reference = string_label.index(_reference)
    # prediction = (
    #     string_label.index(_prediction)
    #     if _prediction in string_label
    #     else not bool(reference)
    # )

    # return (prediction, reference)

def agg_f1(items):

    predictions, references = zip(*items)
    references, predictions = np.asarray(references), np.asarray(predictions)

    return sklearn.metrics.f1_score(references, predictions, average='micro')


def convert_to_int(example):
    example["label"] = int(example["label"])
    return example

def prepate_AT_data(dataset: datasets.Dataset) -> datasets.Dataset:
    # Only supports and refutes
    at_data = dataset.remove_columns(cols_to_remove)
    at_data = at_data.rename_column("question_en_origin", "question")
    at_data = at_data.rename_column("at_labels", "label")
    data = at_data.filter(lambda example: example["label"] is not None)
    return data.map(convert_to_int)


    # return dataset.filter(lambda example: example["claim_label"] in [0,1])