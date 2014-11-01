import numpy as np
from collections import OrderedDict
from format_sample_data import *
from sklearn import cross_validation, preprocessing, svm
from sklearn.cross_validation import KFold

def cross_validate(data, folds, is_scaled):

    X = data["values"]
    Y = data["labels"]

    kf = KFold(len(Y), folds, indices=False)

    scores = []

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
