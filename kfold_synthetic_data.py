import numpy as np
from build_synthetic_data import *
from collections import OrderedDict
from format_sample_data import *
from sklearn import cross_validation, preprocessing, svm
from sklearn.cross_validation import KFold

def scale(scaler, matrix):

    scaled_matrix = scaler.fit_transform(matrix)
    return scaled_matrix

N = 100
char_set = ['A', 'T', 'C', 'G']
size = 100
random_proportion = 0.1
common_proportion = 0.90
random_size = int(size * random_proportion)
common_size = int(size * common_proportion)
cutoff = random_size
common_sequence = "CGCTCCACAACCCCGCCCTTCCTGGATGTGGCGCCATGGGGCGACTTTGAATGGAACATAGTGGTCCACGCTCGACCTCGCGAGCGTGGT"

data = build_synthetic_data_for_cross_validation(N, char_set, size, cutoff, common_sequence)
X = data["values"]
Y = data["labels"]

folds = 2
kf = KFold(len(Y), folds, indices=False)

scores = [] 
is_scaled = False 

for train, test in kf:
    
    scaler = preprocessing.MinMaxScaler()
    X_train, X_test, y_train, y_test = X[train], X[test], Y[train], Y[test]

    training_data = OrderedDict()
    for i in range(len(X_train)):
        training_data[X_train[i]] = y_train[i]

    train_gram_matrix = get_gram_matrix(training_data)
    if is_scaled:
        train_gram_matrix = scaler.fit_transform(train_gram_matrix)
    train_labels = get_label_array(training_data)

    test_data = OrderedDict()
    for i in range(len(X_test)):
        test_data[X_test[i]] = y_test[i]

    test_gram_matrix = get_gram_matrix(test_data)
    if is_scaled:
        test_gram_matrix = scaler.transform(test_gram_matrix)
    test_labels = get_label_array(test_data)

    clf = svm.SVC(kernel='precomputed')
    clf.fit(train_gram_matrix, train_labels)

    print "Score:"
    score = clf.score(test_gram_matrix, test_labels)
    scores.append(score)
    print score

print "Accuracy: %0.2f (+/- %0.2f)" % (np.mean(scores), np.std(scores) * 2)
