import pandas as pd
NHL = pd.read_csv('https://raw.githubusercontent.com/josephofiowa/GA-DSI/master/NHL_Data_GA.csv')

# check it out
NHL.head()
NHL.describe()
NHL.shape

# what is rank?
NHL.Rank            # ok...
NHL.Rank.nunique()  # how many diff values?
NHL.Rank.unique()   # and what are they, anyway?

NHL.isnull().sum()

'''
K-Nearest Neighbors Classification
'''

# store feature matrix in "X"
feature_cols = ['CF%', 'GF', 'Sh%', 'PDO']
X = NHL[feature_cols]

# store response vector in "y"
y = NHL.Rank

# check X's type
print type(X)
print type(X.values)

# check y's type
print type(y)
print type(y.values)


# check X's shape (n = number of observations, p = number of features)
print X.shape

# check y's shape (single dimension with length n)
print y.shape

from sklearn.neighbors import KNeighborsClassifier
# make an instance of a KNeighborsClassifier object
knn = KNeighborsClassifier(n_neighbors=1)
type(knn)

print knn

knn.fit(X, y)

# predict the response values for the observations in X ("test the model")
knn.predict(X)

# store the predicted response values
y_pred_class = knn.predict(X)

# compute classification accuracy
from sklearn import metrics
print metrics.accuracy_score(y, y_pred_class)

# what are we observing from the above accuracy?

'''
Train, test, split
'''

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# STEP 1: split X and y into training and testing sets (using random_state for reproducibility)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=99)

# STEP 2: train the model on the training set (using K=1)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# STEP 3: test the model on the testing set, and check the accuracy
y_pred_class = knn.predict(X_test)
print metrics.accuracy_score(y_test, y_pred_class)

# test with 50 neighbors
knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(X_train, y_train)
y_pred_class = knn.predict(X_test)
print metrics.accuracy_score(y_test, y_pred_class)

# test with 64 neighbors
knn = KNeighborsClassifier(n_neighbors=64)
knn.fit(X_train, y_train)
y_pred_class = knn.predict(X_test)
print metrics.accuracy_score(y_test, y_pred_class)

# examine the class distribution
y_test.value_counts()