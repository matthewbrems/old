# ![logo](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Bias Variance Tradeoff

# Learning Outcomes

By the end of this lession, you should be able to:
* Describe what error due to bias is and what error due to variance is
* Identify the bias-variance tradeoff
* Describe what overfitting and underfitting means in the context of model building


# Key PPT Takeaways
* Bias is error due to the difference between the correct model and our predicted value
* Variance is the error due to the variability of a model for a given data point
* As complexity increases, bias decreases
* As complexity increases, variance increases


# Example in code
```python

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def f(x):
    """ function to approximate by polynomial interpolation"""
    return x * np.sin(x)


# generate points used to plot
x_plot = np.linspace(0, 10, 100)

# generate points and keep a subset of them
x = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
x = np.sort(x[:20])
y = f(x)

# create matrix versions of these arrays
X = x[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]

plt.plot(x_plot, f(x_plot), label="ground truth")
plt.scatter(x, y, label="training points")

for degree in [3, 4, 5]:
    model = make_pipeline(PolynomialFeatures(degree), Ridge())
    model.fit(X, y)
    y_plot = model.predict(X_plot)
    plt.plot(x_plot, y_plot, label="degree %d" % degree)

plt.legend(loc='lower left')

plt.show()



# Credit:
# Author: Mathieu Blondel

```

# Resources

* When you overfit on the training set... [gif](http://i.imgur.com/rbI9bFf.gif)
* Scott Foreman-Roe's [take on the bias-variance tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html) is a classic. Read it.
* One of my favorite [lectures](https://www.youtube.com/watch?v=zrEyxfl2-a8) on the bias variance trade-off
* Play with [different degress](http://arachnoid.com/polysolve/) of fitting a polynomial
* SKLearn's [learning curves](http://www.astroml.org/sklearn_tutorial/practical.html) is a good further analysis of the tradeoff
* A mathematical [deeper dive](https://courses.cs.washington.edu/courses/cse546/12wi/slides/cse546wi12LinearRegression.pdf) on linear regression and the bias variance tradeoff from UW
* A tepid dive into [how ensembling helps solve the bias-variance tradeoff](http://www.hlt.utdallas.edu/~vgogate/ml/2015s/lectures/EnsembleMethods.pdf) (more on this tomorrow)
* Amazon Machine Learning's discussion of over and underfitting [here](http://docs.aws.amazon.com/machine-learning/latest/dg/model-fit-underfitting-vs-overfitting.html)