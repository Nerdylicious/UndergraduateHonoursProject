import numpy as np
import random
from parse_file import parse

def build_binding_protein_data_for_cross_validation(total_pos_samples, total_neg_samples, sample_size):

    file_name = 'dataset_positive.fasta'
    file_type = 'fasta'

    positive_sequences = parse(file_name, file_type, total_pos_samples)

    file_name = 'dataset_negative.fasta'
    file_type = 'fasta'

    negative_sequences = parse(file_name, file_type, total_neg_samples)

    data = {}
    sequence_data = []
    labels = []

    #randomly select the samples and ensuring that we have an equal number of positive and negative samples
    sample_dictionary = {}
    count = 0
    while count < sample_size:
        to_add_pos_sequence = True
        while to_add_pos_sequence:
            rand_index = random.randint(0, len(positive_sequences) - 1)
            sequence = positive_sequences[rand_index]
            #don't include any sequences that would be a duplicate in our sample 
            if not sequence in sample_dictionary:
                sequence_data.append(sequence)
                labels.append(1)
                sample_dictionary[sequence] = None 
                count = count + 1
                to_add_pos_sequence = False
        to_add_neg_sequence = True
        while to_add_neg_sequence:
            rand_index = random.randint(0, len(negative_sequences) - 1)
            sequence = negative_sequences[rand_index]
            if not sequence in sample_dictionary:
                sequence_data.append(sequence)
                labels.append(0)
                sample_dictionary[sequence] = None 
                count = count + 1
                to_add_neg_sequence = False

    data["values"] = np.array(sequence_data)
    data["labels"] = np.array(labels)

    return data
