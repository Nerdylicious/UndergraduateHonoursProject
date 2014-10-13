import numpy as np
from collections import OrderedDict
from format_sample_data import *
from sklearn.cross_validation import KFold

X = np.array([
"TTTAGTTAAGCTCGGGCAGCGCACCAAAATATGTTGCATT",
"CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATA",
"GAGTAAGGCTTGAGAAATTTCCTCAAACATCAGTCCCCCT",
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGGT",
"GCGCTTAGAACCTTGCTTCGGCCGGCTCATCCTACCCCCT",
"GGTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT",
"TACGCAAGAGCCCGAGCCGTACTCGGGCGATTCTGTGTAA",
"AAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC",
])

Y = np.array([0, 1, 0, 1, 0, 1, 0, 1])

kf = KFold(len(Y), 2, indices=False)
print kf

for train, test in kf:
    print train, test
    X_train, X_test, y_train, y_test = X[train], X[test], Y[train], Y[test]
    
    print "Train:"
    #print X_train, y_train

    training_data = OrderedDict()
    for i in range(len(X_train)):
        training_data[X_train[i]] = y_train[i]

    print training_data

    train_gram_matrix = get_gram_matrix(training_data)
    train_labels = get_label_array(training_data)
    print train_gram_matrix
    print train_labels

    print "Test:"
    #print X_test, y_test

    test_data = OrderedDict()
    for i in range(len(X_test)):
        test_data[X_test[i]] = y_test[i]

    print test_data

    test_gram_matrix = get_gram_matrix(test_data)
    test_labels = get_label_array(test_data)
    print test_gram_matrix
    print test_labels
