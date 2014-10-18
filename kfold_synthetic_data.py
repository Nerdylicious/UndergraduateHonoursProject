import numpy as np
from build_synthetic_data import *
from collections import OrderedDict
from format_sample_data import *
from sklearn import cross_validation, preprocessing, svm
from sklearn.cross_validation import KFold

def scale(scaler, matrix):

    scaled_matrix = scaler.fit_transform(matrix)
    return scaled_matrix

N = 200
char_set = ['A', 'T', 'C', 'G']
size = 100
random_proportion = 0.1
common_proportion = 0.90
random_size = int(size * random_proportion)
common_size = int(size * common_proportion)
cutoff = random_size
common_sequence = "CGCTCCACAACCCCGCCCTTCCTGGATGTGGCGCCATGGGGCGACTTTGAATGGAACATAGTGGTCCACGCTCGACCTCGCGAGCGTGGT"
#common_sequence = "A" * 5 

data = build_synthetic_data_for_cross_validation(N, char_set, size, cutoff, common_sequence)
X = data["values"]
Y = data["labels"]

#print X
#print Y

kf = KFold(len(Y), 2, indices=False)
#print kf

scores = [] 

#need to use the same instance of the scaler used on the train data to the test data as well
scaler = preprocessing.MinMaxScaler()

is_scaled = False 

for train, test in kf:
    #print train, test
    X_train, X_test, y_train, y_test = X[train], X[test], Y[train], Y[test]

    #print "Train:"

    training_data = OrderedDict()
    for i in range(len(X_train)):
        training_data[X_train[i]] = y_train[i]

    #print training_data

    train_gram_matrix = get_gram_matrix(training_data)
    if is_scaled:
        scaled_train_matrix = scale(scaler, train_gram_matrix)
    train_labels = get_label_array(training_data)
    #print train_gram_matrix
    #print "Scale:"
    #print scaled_train_matrix
    #print train_labels

    #print "Test:"

    test_data = OrderedDict()
    for i in range(len(X_test)):
        test_data[X_test[i]] = y_test[i]

    #print test_data

    test_gram_matrix = get_gram_matrix(test_data)
    if is_scaled:
        scaled_test_matrix = scale(scaler, test_gram_matrix)
    test_labels = get_label_array(test_data)
    #print test_gram_matrix
    #print "Scaled:"
    #print scaled_test_matrix
    #print test_labels

    clf = svm.SVC(kernel='precomputed')
    if is_scaled:
        clf.fit(scaled_train_matrix, train_labels)
    else:
        clf.fit(train_gram_matrix, train_labels)

    #test_labels.reverse()
    #print test_labels

    print "Score:"
    if is_scaled:
        score = clf.score(scaled_test_matrix, test_labels)
    else:
        score = clf.score(test_gram_matrix, test_labels)
    scores.append(score)
    print score

    #print "Prediction:"
    #print clf.predict(test_gram_matrix)
    #print clf.predict(scaled_test_matrix)

print "Accuracy: %0.2f (+/- %0.2f)" % (np.mean(scores), np.std(scores) * 2)
