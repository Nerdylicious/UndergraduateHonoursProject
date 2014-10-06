import numpy as np
from collections import OrderedDict
from format_sample_data import *
from sklearn import svm

synthetic_data = OrderedDict([
    ("GTCTGCTTCCCTTCTAACAGTGGTCATCAAGGCGTAATCAGTGAACCGGGCGACTGTACTATGTAGTCAAAAGATCCCTAAGCTACAGAACCCACGCGCC", 0),
    ("TCACCGAAAGAGGGTTTCATCCGTAACCAGCAACAAGCTATTACCATCCTTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGGACGCCTTGCTGGTCTCA", 1),
    ("CGAGGTGTATTTGATCTTTGTTCGCGTTGCCAACCTCCGGATCCTTGTACTTGCCTTAGTATGGCGCATACTGCCTATATAAAACTGCTCCTTTACATCT", 0),
    ("GGCCCTGGAGGAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGACTATGCAGCAACAACCCTTAGACTCCTTTGGTTGGGACTTAGTCCAGGCCCATTC", 1),
])

gram_matrix = get_gram_matrix(synthetic_data)
print gram_matrix

labels = get_label_array(synthetic_data)
print labels

clf = svm.SVC(kernel='precomputed')
clf.fit(gram_matrix, labels)
print clf.predict(gram_matrix)
