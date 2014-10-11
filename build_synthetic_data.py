from collections import OrderedDict
from word_generator import *

def build_synthetic_data_dictionary(N, char_set, size, cutoff, common_sequence):
    
    synthetic_data = OrderedDict()

    for i in range(N/2):
        string = generate_random_word(char_set, size)
        print string
        synthetic_data[string] = 0

    for i in range(N/2):
        string = generate_similar_word(char_set, cutoff, common_sequence)
        print string
        synthetic_data[string] = 1

    return synthetic_data
