#!python3

# Imports section
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

# Some parameters
# Putting this to true will include the numbers of day since the begining of the season into the data set
useDates = False
# If True will change the data set to use ratio of odds instead of the odds themselves
useTranformation = False
# If False it will print cross validation results. If True will predict on the tests set
useTests = False
# If True will print a list of matches that didn't go as expected. REQUIRED : useTests = False
usePredictArtefacts = True
# Threshold use in the prediction of artefacts:
artefactsThreshold = 0.1
# Are draws artefacts ?
excludeDraws = True
# Use the following file to return the results. REQUIRED : useTests = True
outFile = "submission.csv"

# We define the model of learning
clf = LogisticRegression()

# We get the datas
ID, X_train, y_train, date = read_train('train.csv')
if useTests:
    ID_test, X_test, date_tests = read_test('test.csv')
    X_test = np.array(X_test)
X_train = np.array(X_train)
y_train = np.array(y_train)

# Remove the NaN values
X_train = remove_nan(X_train)
if useTests:
    X_test = remove_nan(X_test)

# Add the dates to the features if set to True
if useDates:
    date = np.array(transform_date(date))
    date = date[:, np.newaxis]
    X_train = np.hstack((X_train, date))
    if useTests:
        date_tests = np.array(transform_date(date_tests))
        date_tests = date_tests[:, np.newaxis]
        X_test = np.hstack((X_test, date_tests))

if useTranformation:
    X_train = transform_data(X_train)
    if useTests:
        X_test = transform_data(X_test)

if useTests:
    clf.fit(X_train, y_train)
    # Predict the results
    predict = clf.predict(X_test)
    print(clf.predict_proba(X_test))
    # Output the predictions
    write_in_file(outFile, ID_test, predict)
else:
    # We are set to view the score on cross validation
    X_cross_train, X_cross_test, y_cross_train, y_cross_test = train_test_split(X_train, y_train, test_size=.4, random_state=42)
    clf.fit(X_cross_train, y_cross_train)

    score = clf.score(X_cross_test, y_cross_test)
    print("Cross validation score : ", score)

    if usePredictArtefacts:
        # We get the probabilites for each match
        result = clf.predict_proba(X_cross_test)
        for i in range(len(y_cross_test)):
            if excludeDraws and y_cross_test[i] == 1:
                continue
            if result[i][y_cross_test[i]] <= artefactsThreshold:
                print("Artefact :\n\tPrediction: ", result[i])
                if useTranformation:
                    print("\tFeatures : ratio of the odds: team1 / draw , team2 / draw, team1 / team2")
                else:
                    print("\tFeatures : Odds that team1 wins, Odds of draw, Odds that team2 wins (the lower the better)")
                for j in range(6):
                    print("\t", X_cross_test[i][j * 3 + 0], X_cross_test[i][j * 3 + 1], X_cross_test[i][j * 3 + 2])
                print("\tResult = ", y_cross_test[i], " (0 = team1, 1 = draw, 2= team2)")
