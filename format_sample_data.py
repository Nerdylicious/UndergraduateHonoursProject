#Purpose: Given a dictionary of strings and its corresponding classification, return the gram matrix and array of classifications
from collections import OrderedDict
from gram_matrix import *

def get_gram_matrix(sample_data):
    strings = sample_data.keys()
    return calculate_gram_matrix(strings)

def get_label_array(sample_data):
    labels = sample_data.values()
    return labels

#format for sample data is (string, classification) for (key, value)
sample_data = OrderedDict([
    ("ACCTGCGGATATTAATTAACTGACC", 1),
    ("TCCTCTATTAATCGGTGGATGTCGG", 0),
    ("AGAATTAATTACTGATATTCTTTCA", 1),
    ("CATAGTCGGCAGCCGTCACGACCCT", 0)
])

print get_gram_matrix(sample_data)
print get_label_array(sample_data)
