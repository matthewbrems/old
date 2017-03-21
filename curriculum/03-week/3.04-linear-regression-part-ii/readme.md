---
title: Introduction to Linear Regression - Part 2
duration: "1:30"
creator:
    name: Matt Brems & Marc Harper
    city: DC & LA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to Linear Regression - Part 2
Week 3 | Lesson 3.04

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- List the assumptions for a MLR model.
- Fit SLR and MLR models in statsmodels.
- (if time allows) fit SLR and MLR models in scikit-learn.

---

## SLR to MLR

### Introduction
The TL;DR of MLR is that rather than using one predictor to predict an independent variable, we include others.

## Assumptions of MLR
Just like SLR, there are assumptions in MLR. Luckily, they're really similar to the SLR assumptions.
- **Linearity:** Y must have an approximately linear relationship with each independent X_i.
- **Independence:** Errors (residuals) e_i and e_j must be independent of one another for any i != j.
- **Normality:** The errors (residuals) follow a Normal distribution.
- **Equality of Variances:** The errors (residuals) should have a roughly consistent pattern, regardless of the value of the X_i. (There should be no discernable relationship between X_1 and the residuals.)
- **Independence Part 2:** The independent variables X_i and X_j must be independent of one another for any i != j.

The mnemonic **LINEI** is a useful way to remember these five assumptions. (That's not true.)

## Dummy Variables

We briefly touched on how to convert qualitative variables into "dummy variables" for use in Python. Let's touch on a caution moving forward and interpreting these.

If you convert a qualitative variable to dummy variables, you want to turn a variable with N categories into N-1 variables.

Suppose we're working with the variable "sex" or "gender" with values "M" and "F". You include in your model one variable for "sex = F" which takes on 1 if sex is female and 0 if sex is not female. Rather than saying "a one unit change in X," the coefficient associated with "sex = F" is interpreted as the average change in Y when sex = F relative to when sex = M.

Suppose we're modeling revenue at a bar for each of the days of the week. We might include six variables: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday". The coefficient for Monday is interpreted in the average change in revenue when "day = Monday" relative to "day = Sunday." The coefficient for Tuesday is interpreted in the average change in revenue when "day = Tuesday" relative to "day = Sunday" and so on.

**Turn and Talk:** If we were to include all N predictors, what do you think would happen?

## Interaction Terms

Sometimes we want to include two variables that are highly correlated with one another. This would violate the assumption of independence between X_i and X_j, but by including an interaction term - that is, an additional variable X_i * X_j - we are able to overcome this issue by explicitly modeling the dependence between the two variables.

If your model includes an interaction term X_i * X_j that is "statistically significant," it is customary to include X_i * X_j, X_i, **and** X_j in your final model - even if X_i or X_j are not statistically significant!

## Inference

We can conduct inference on the parameters. The statsmodels library will be particularly helpful for this.

**Check:** Let's refresh our minds about inference.
- Statistical inference is when we use sample statistics to learn more about population parameters.
- A point estimate is the value of a statistic, or a "best guess" for the true value of the parameter. (Call of Duty sniper rifle.)
- A standard error is the standard deviation of a statistic and helps us to quantify the variability of our estimator.
- A p-value is the probability that we get a statistic as extreme or more extreme if we re-ran the experiment. If our p-value is less than alpha, we reject our null hypothesis. Otherwise, we fail to reject the null hypothesis.
- A confidence interval is a set of possible values for the parameter.

## Conclusion
- Q & A
- Lab

## Resources
- [Linear Regression Assumptions Discussed - Duke University](http://people.duke.edu/~rnau/testing.htm)
- [Wikipedia: Mean Squared Error](https://en.wikipedia.org/wiki/Mean_squared_error)
- [Wikipedia: Residual Sum of Squares](https://en.wikipedia.org/wiki/Residual_sum_of_squares)
