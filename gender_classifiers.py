# in this project, we try out different models from the scikit learn package for binary classification
# we only tested our models on our training data set,
# in order to check how they perform in application we should have taken testing data into consideration,
# our models could be prone to overfitting
from sklearn import tree
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# Data : height, weight, shoe size
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
#labels
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

# Classifiers
# using the default values for all the hyperparameters
clf_tree = tree.DecisionTreeClassifier()
clf_svm = SVC()
clf_perceptron = Perceptron()
clf_KNN = KNeighborsClassifier()
clf_logistic = LogisticRegression()

# Training the models
clf_tree.fit(X, Y)
clf_svm.fit(X, Y)
clf_perceptron.fit(X, Y)
clf_KNN.fit(X, Y)
clf_logistic.fit(X, Y)

# Testing using the same data
pred_tree = clf_tree.predict(X)
acc_tree = accuracy_score(Y, pred_tree) * 100
#Result: 100
print('Accuracy for DecisionTree: {}'.format(acc_tree))

pred_svm = clf_svm.predict(X)
acc_svm = accuracy_score(Y, pred_svm) * 100
#Result: 54,54...
print('Accuracy for SVM: {}'.format(acc_svm))

pred_per = clf_perceptron.predict(X)
acc_per = accuracy_score(Y, pred_per) * 100
#Result: 45,45...
print('Accuracy for perceptron: {}'.format(acc_per))

pred_KNN = clf_KNN.predict(X)
acc_KNN = accuracy_score(Y, pred_KNN) * 100
#Result: 72,72...
print('Accuracy for KNN: {}'.format(acc_KNN))

pred_logistic = clf_logistic.predict(X)
acc_logistic = accuracy_score(Y, pred_logistic) * 100
print('Accuracy for logistic regression: {}'.format(acc_logistic))


# The best classifier from svm, per, KNN
# We left out the DecisionTreeClassifier and logistic regression since there is
# a high likelihood of overfitting, which in practice translates into a bad classifier
index = np.argmax([acc_svm, acc_per, acc_KNN]) # Returns the indices of the maximum values along an axis.
classifiers = {0: 'SVM', 1: 'Perceptron', 2: 'KNN'}
print('Best gender classifier is {}'.format(classifiers[index]))
