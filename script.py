#!python3

import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Imputer
import numpy as np
from write import *
from read import *
from transform import *
from sklearn.cross_validation import train_test_split

models = [
    ('Knn 5', KNeighborsClassifier(5)),
    ('Naive Bayes', GaussianNB()),
    ('Logistic Regression', LogisticRegression()),
#    ('Linear SVM', SVC(kernel='linear', probability=True)),
#    ('Poly SVM', SVC(kernel='poly', degree=2, probability=True)),
    ('RBF SVM', SVC(kernel='rbf', gamma=2, C=1, probability=True)),
    ('Classification Tree', DecisionTreeClassifier(max_depth=5)),
    ('Random Forest', RandomForestClassifier(max_depth=5, n_estimators=50))
]

ID, X_train, y_train, date = read_train('train.csv')
# X_test, ID = read_test('test.csv')
X_train = np.array(X_train)
y_train = np.array(y_train)

# Remove the NaN values
# imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
# imp = imp.fit(X_train)

# X_train = imp.transform(X_train)
X_train = remove_nan(X_train)
"""date = np.array(transform_date(date))
date = date[:, np.newaxis]
print(date.shape, X_train.shape)
X_train = np.hstack((X_train, date))"""
print(X_train)
# X_test = imp.transform(X_test)

X_cross_train, X_cross_test, y_cross_train, y_cross_test = train_test_split(X_train, y_train, test_size=.4, random_state=42)


for model in models:
    clf = model[1]
    print('\n', model[0])
    clf.fit(X_cross_train, y_cross_train)

    score = clf.score(X_cross_test, y_cross_test)
    print(score)

X_train = transform_data(X_train)
print(X_train)

# Split the data
print(X_train.shape, y_train.shape)
X_cross_train, X_cross_test, y_cross_train, y_cross_test = train_test_split(X_train, y_train, test_size=.4, random_state=42)

for model in models:
    clf = model[1]
    print('\n', model[0])
    clf.fit(X_cross_train, y_cross_train)

    score = clf.score(X_cross_test, y_cross_test)
    print(score)

# result = clf.predict(X_test)

# write_in_file('submission.csv', ID, results)
