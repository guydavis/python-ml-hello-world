#!/usr/bin/env python3
"""Basic SKLearn Hello-World to verify a successful installation.
   http://scikit-learn.org/stable/tutorial/basic/tutorial.html"""

from sklearn import svm
from sklearn import datasets

def main():
    """ Classification using support-vector machine. """
    iris = datasets.load_iris()
    digits = datasets.load_digits()
    print(digits.data)
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])
    prediction = clf.predict(digits.data[-1:])
    print(prediction)

if __name__ == "__main__":
    main()
