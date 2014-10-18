import numpy as np
from collections import OrderedDict
from word_generator import *

def build_synthetic_data_dictionary(N, char_set, size, cutoff, common_sequence):
    
    synthetic_data = OrderedDict()

    for i in range(N/2):
        string = generate_random_word(char_set, size)
        synthetic_data[string] = 0

    for i in range(N/2):
        string = generate_similar_word(char_set, cutoff, common_sequence)
        synthetic_data[string] = 1

    return synthetic_data

def build_synthetic_data_for_cross_validation(N, char_set, size, cutoff, common_sequence):
    
    data = {}
    synthetic_data = []
    labels = [] 

    for i in range(N):
        if i % 2 == 0:
            string = generate_random_word(char_set, size)
            synthetic_data.append(string)
            labels.append(0)
        else:
            string = generate_similar_word(char_set, cutoff, common_sequence)
            synthetic_data.append(string)
            labels.append(1)

    data["values"] = np.array(synthetic_data)
    data["labels"] = np.array(labels)

    return data 
