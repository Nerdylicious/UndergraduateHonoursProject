import numpy as np
import random
from generate_operon_data import *

def build_operon_data_for_cross_validation(total_pos_samples, total_neg_samples, sample_size):

    positive_samples = get_positive_samples(total_pos_samples)
    negative_samples = get_negative_samples(total_neg_samples)

    data = {}
    sequence_data = []
    labels = []

    sample_dictionary = {}
    count = 0
    while count < sample_size:
        to_add_pos_sequence = True
        while to_add_pos_sequence:
            rand_index = random.randint(0, len(positive_samples) - 1)
            sequence = positive_samples[rand_index]
            if not sequence in sample_dictionary:
                sequence_data.append(sequence)
                labels.append(1)
                sample_dictionary[sequence] = None
                count = count + 1
                to_add_pos_sequence = False
        to_add_neg_sequence = True
        while to_add_neg_sequence:
            rand_index = random.randint(0, len(negative_samples) - 1)
            sequence = negative_samples[rand_index]
            if not sequence in sample_dictionary:
                sequence_data.append(sequence)
                labels.append(0)
                sample_dictionary[sequence] = None
                count = count + 1
                to_add_neg_sequence = False

    data["values"] = np.array(sequence_data)
    data["labels"] = np.array(labels)
    
    return data 
