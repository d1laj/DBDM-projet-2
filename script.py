#!python3

import sklearn
from sklearn.svm import SVC
from numpy import genfromtxt
from sklearn.preprocessing import Imputer
import numpy as np
from write import write_in_file
from sklearn.cross_validation import train_test_split

X_train , y_train = read_train('train.csv')
X_test, ID = read_test('test.csv')

# Remove the NaN values
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp = imp.fit(X_cross_train)
X_train = imp.transform(X_train)
X_test = imp.transform(X_test)

# Split the data
X_cross_train, X_cross_test, y_cross_train, y_cross_test = train_test_split(X_train, X_test, test_size=.4, random_state=42)

clf = SVC(kernel='rbf', gamma=2, C=1, probability=True)
clf.fit(X_cross_train, y_cross_train)

score = clf.score(X_cross_test, y_cross_test)
#result = clf.predict(X_test)

print(score)
"""
my_data = genfromtxt('train.csv', delimiter=',', skip_header=1)
#my_data = my_data[:, np.newaxis]
print(my_data)
answers = my_data[:, 4]
print(answers)
"""
"""
clf = SVC(kernel='rbf', gamma=2, C=1, probability=True)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(my_data, ans, test_size=.4, random_state=42)

clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)

print(score)

y_result = clf.predict(X_test)

for i in range(y_test.size):
    if y_result[i] == y_test[i]:
        print(y_result[i] == y_test[i], y_test[i], y_result[i], classes[y_result[i]-1])
    else:
        print(y_result[i] == y_test[i], y_test[i], y_result[i], "\t\t", classes[y_test[i]-1], " vs ",classes[y_result[i]-1])
"""

write_in_file('submission.csv', ID, results)
