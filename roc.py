import numpy as np
import pylab as pl
from build_synthetic_data import *
from collections import OrderedDict
from format_sample_data import *
from sklearn import cross_validation, preprocessing, svm, datasets
from sklearn.cross_validation import KFold
from sklearn.metrics import roc_curve, auc

N = 200
char_set = ['A', 'T', 'C', 'G']
size = 200
random_proportion = 0.9
common_proportion = 0.1
random_size = int(size * random_proportion)
common_size = int(size * common_proportion)
cutoff = random_size
common_sequence = "GCTCCACAAC"

data = build_synthetic_data_for_cross_validation(N, char_set, size, cutoff, common_sequence)
X = data["values"]
Y = data["labels"]

kf = KFold(len(Y), 2, indices=False)
half = int(len(Y)/2)

scaler = preprocessing.MinMaxScaler()
to_scale = True

X_train, X_test, y_train, y_test = X[:half], X[half:], Y[:half], Y[half:]

training_data = OrderedDict()
for i in range(len(X_train)):
    training_data[X_train[i]] = y_train[i]

train_gram_matrix = get_gram_matrix(training_data)
train_labels = get_label_array(training_data)
if to_scale:
    train_gram_matrix = scaler.fit_transform(train_gram_matrix)

test_data = OrderedDict()
for i in range(len(X_test)):
    test_data[X_test[i]] = y_test[i]

test_gram_matrix = get_gram_matrix(test_data)
test_labels = get_label_array(test_data)
if to_scale:
    test_gram_matrix = scaler.transform(test_gram_matrix)

classifier = svm.SVC(kernel='precomputed', probability=True)
probas_ = classifier.fit(train_gram_matrix, train_labels).predict_proba(test_gram_matrix)

print probas_
print "Test Labels:"
print test_labels
print "Prediction:"
print classifier.predict(test_gram_matrix)

fpr, tpr, thresholds = roc_curve(test_labels, probas_[:, 1])
roc_auc = auc(fpr, tpr)
print "Area under the ROC curve: %f" % roc_auc

pl.clf()
pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver operating characteristic (common sequence length=10)')
pl.legend(loc="lower right")
pl.show()
