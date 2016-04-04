#!python3

import sklearn
from sklearn.svm import SVC
from numpy import genfromtxt
import numpy as np

my_data = genfromtxt('train.csv', delimiter=',', dtype=type(1.), skip_header=1)
#my_data = my_data[:, np.newaxis]

answers = mydata[4, :]
print(answers)

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
