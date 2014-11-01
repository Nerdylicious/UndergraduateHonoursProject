import numpy as np
from parse_file import parse

def build_binding_protein_data_for_cross_validation():

    file_name = 'dataset_positive.fasta'
    file_type = 'fasta'
    count = 150

    positive_sequences = parse(file_name, file_type, count)

    file_name = 'dataset_negative.fasta'
    file_type = 'fasta'
    count = 150

    negative_sequences = parse(file_name, file_type, count)

    data = {}
    sequence_data = []
    labels = []

    for i in range(len(positive_sequences)):
        sequence_data.append(positive_sequences[i])
        labels.append(1)
        sequence_data.append(negative_sequences[i])
        labels.append(0)

    data["values"] = np.array(sequence_data)
    data["labels"] = np.array(labels)

    return data
