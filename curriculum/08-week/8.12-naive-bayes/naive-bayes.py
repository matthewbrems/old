from sklearn.naive_bayes import GaussianNB
import numpy as np

# Import data into a numpy array
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

#Initialize a variable as the Guassian Naive Bayes classifier and fit it with the data
clf = GaussianNB()
clf.fit(X, Y)
GaussianNB()

# Predict a few instances
print(clf.predict([[-0.8, -1]]))
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
GaussianNB()
print(clf_pf.predict([[-0.8, -1]]))
