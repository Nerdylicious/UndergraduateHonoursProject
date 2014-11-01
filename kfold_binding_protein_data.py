import numpy as np
from build_binding_protein_data import *
from collections import OrderedDict
from format_sample_data import *
from sklearn import cross_validation, preprocessing, svm
from sklearn.cross_validation import KFold

data = build_binding_protein_data_for_cross_validation()

X = data["values"]
Y = data["labels"]

folds = 2
kf = KFold(len(Y), folds, indices=False)

training_data = OrderedDict()
for i in range(len(X)):
    training_data[X[i]] = Y[i]

gram_matrix = get_gram_matrix(training_data)
print gram_matrix
