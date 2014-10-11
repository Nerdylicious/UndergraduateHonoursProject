import numpy as np
from build_synthetic_data import *
from collections import OrderedDict
from format_sample_data import *
from sklearn import svm

N = 500 
char_set = ['A', 'T', 'C', 'G']
size = 100
random_proportion = 0.1
common_proportion = 0.9
random_size = int(size * random_proportion) 
common_size = int(size * common_proportion)
cutoff = random_size 
common_sequence = 'A' * common_size

synthetic_data = build_synthetic_data_dictionary(N, char_set, size, cutoff, common_sequence)

gram_matrix = get_gram_matrix(synthetic_data)
print gram_matrix

labels = get_label_array(synthetic_data)
print "Labels:"
print labels

clf = svm.SVC(kernel='precomputed')
print clf.fit(gram_matrix, labels)
print "Prediction:"
print clf.predict(gram_matrix)   
