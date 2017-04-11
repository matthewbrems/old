---
title: Introduction to Statistics - Part 2
duration: "1:30"
creator:
    name: Matt Brems
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to Statistics - Part 2
Week 2 | Lesson 2.03

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Describe the Normal distribution.
- Generate confidence intervals and interpret the results.
- Execute hypothesis tests and interpret the results.
- State and apply the Central Limit Theorem.
- Differentiate between parametric and nonparametric statistical tests.

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- This should've been completed as pre-work before starting the course, but if you didn't complete it, please complete the course pre-work on statistics.

---

## Introduction
Recall that we use sample statistics to estimate population parameters. Our goal is to calculate sample statistics and then rely on properties of a random sample (and perhaps additional assumptions) to be able to make inferences that we generalize to the larger population of interest. Let's make a table comparing statistics and parameters.

We will also rely on the library scipy (scipy.stats) for much of our work today, so let's import it now as stats.

```python
import scipy.stats as stats
```
Review of mean, standard deviation, correlation:

![table](./stats-table.JPG)

## Normal Distribution
**Discussion:** What do you know about the Normal distribution so far?

The Normal distribution is one of the most commonly used distributions in all of statistics. Normality is an assumption that underlies many statistical tests and serves as a convenient model for the *distribution* of many (but not all!) variables.

**Check:** What is a distribution?

The Normal distribution is parameterized by two parameters: the population mean and the population standard deviation. If a variable follows a Normal distribution exactly, its mean, median, and mode will all be equal.

**Check:** How is my Normal distribution different if I provide the population mean and the population variance?

Intelligence Quotient (IQ) follows a Normal distribution by design. IQ is Normally distributed with a mean of 100 and a standard deviation of 15. (We might say IQ ~ Normal(100,15) or IQ ~ N(100,15).)

**Check:** When we discuss distributions, we generally care about three characteristics. What are these three characteristics and how are they reflected in IQ ~ N(100,15)?

### The 68-95-99.7 Rule
It is often to our benefit to identify how extreme (or far away from the expected value) a particular observation is within the context of a distribution. For example, an extreme stock price might indicate a major shift in the market and thus might dictate a need to buy or sell. An extreme drop in air pressure might indicate a significant weather event, causing a reaction from the National Weather Service. Quantifying just how extreme a particular observation is from the expected value (a.k.a. population mean) may indicate a particular action we should take.

It is possible to show that, for a Normal distribution, 68% of observations from a population will fall within plus or minus one standard deviation of the population mean, that 95% of observations from a population will fall within plus or minus two standard deviations of the population mean, and that 99.7% of observations from a population will fall within plus or minus three standard deviations of the population mean.

**Check:** What percentage of individuals have an IQ between 85 and 115?

**Check:** What percentage of individuals have an IQ above 100?

**Check:** What percentage of individuals have an IQ between 85 and 130?

### Z-Score
While it's nice to have this 68-95-99.7 rule, let's generalize this to calculate the z-score of an observation.

z_i = (x_i - [population mean of x]) / [standard deviation of x]

This measures how many standard deviations an observation x_i is from the population mean. Since X ~ N(mu,sigma), Z ~ (0,1). We call Z the **standard normal distribution** because it has a mean of 0 and standard deviation of 1.

```python
import numpy as np
values = np.array([3,4,5])

from scipy import stats
stats.zscore(values)
```

**Check:** If X is not normal, but we calculate Z by standardizing X using the mean and standard deviation of X as above, is Z ~ N(0,1)?

## Central Limit Theorem
Normality underlies many of the inferential techniques that we seek to use. It is important for us to determine when Normality is a condition we've met.

Consider the random variable X. We can take a sample from this population of size n and find the mean of that sample. Let's call this sample mean 1. We can take another sample from this population, also of size n, and find the mean of that sample. Let's call this sample mean 2. We can do this over and over until we've calculated the mean of every possible sample of size n. If we plotted every sample mean ("little x-bar") on a histogram, we get another distribution - called "the sampling distribution of X-bar."

This distribution, the sampling distribution of X-bar, is sometimes Normally distributed.
- If X ~ N(mu,sigma), then X-bar is exactly N(mu,sigma/sqrt(n)).
- If X is not Normally distributed, then X-bar is approximately N(mu,sigma/sqrt(n)) if the sample size n is at least 30.

If X-bar is Normally distributed, then we can use inferential methods that rely on the sample mean. ("little x-bar")

## Confidence Intervals
Call of Duty / Halo Example: sniper rifle versus rocket launcher?

A confidence interval describes a set of possible values for the parameter based on a statistic. Confidence intervals will be centered at the point estimate and then include +/- a few standard errors. (Standard error is just the standard deviation of a statistic.)

Thus, the structure of a confidence interval will be [point estimate] +/- [multiplier]*[standard error].

We use our sample mean to estimate our population mean. Thus, our sample mean is our "point estimate." (Sniper's bullet.)

Because we know that X-bar is Normally distributed with standard deviation sigma/sqrt(n), we have an estimate of the variability of sample means from sample to sample. As such, our "standard error" will be sigma/sqrt(n).

Similarly, because we know that X-bar is Normally distributed, our "multiplier" for our standard error will be based on critical values of the Normal distribution. If we want our confidence level (how confident we are that the true value of the parameter lies in the confidence interval) to be 90%, our multiplier should be z* = 1.645. If we want our confidence level to be 95%, our multiplier should be z* = 1.96. If we want our confidence level to be 99%, our multiplier should be 2.575.

Putting it all together, our z-based confidence interval is [sample mean] +/- [z multiplier] * [sigma/sqrt(n)].

### Interpretation
Suppose a 95% confidence interval for the mean number of burritos Matt eats in a week is (2.5,5.5). There are two interpretations from this.
- We are 95% **confident** that the true mean of number of burritos Matt eats in a week is between 2.5 and 5.5.
- If we pulled 100 samples and constructed confidence intervals in the same manner, we expect that 95 of the intervals would contain the true mean of number of burritos Matt eats in a week.

**Check:** What is the multiplier for this confidence interval? What is the point estimate? What is the standard error?

### Let's do this in Python!
```python
from scipy import stats

## Interval for N = 1:
stats.norm.interval(confidence_level, loc=mean, scale=sigma)

## Interval for N > 1:
stats.norm.interval(confidence_level, loc=mean, scale=sigma/sqrt(N))

```

### What if we don't know the population standard deviation?
Note that we've always used sigma in our z calculations - that's because we assume that we know the population standard deviation. If we don't have the population standard deviation (which we usually won't), we can generate confidence intervals using the t-distribution instead of the z-distribution. Confidence intervals using the t-distribution will follow similar rules, except that the t-distribution assumes that the population standard deviation is unknown.  Thus, the structure of a confidence interval based on t is [sample mean] +/- [t multiplier] * [s/sqrt(n)], where s is the **sample** standard deviation and the t-multiplier changes based on both the confidence level and the sample size n.

### Let's do this in Python!
```python
from scipy.stats import t

## Interval for any N:
t.interval(confidence_level, degrees_of_freedom, loc=mean, scale=s/sqrt(n))
## Note that degrees_of_freedom should be equal to n-1, where n is the sample size!!

```

## Hypothesis Tests
A hypothesis test is a way to learn more about a parameter of interest.

### Step 1: Construct a null hypothesis that you seek to contradict and its complement, the alternative hypothesis.
Suppose you want to disprove that the mean number of burritos I eat in a week is 4. Then your null hypothesis (H_0) and alternative (H_A or H_1) hypothesis are:
- H_0: mu = 4
- H_A: mu != 4

If you want to show that the mean number of burritos I eat in a week is **less than** 4, then your hypotheses are:
- H_0: mu >= 4
- H_A: mu < 4

Your hypotheses must be mutually exclusive and include all possible values of the parameter. What you **want to show** should be in your alternative hypothesis.

**Check:** Suppose you wanted to show that the mean number of burritos I eat in a week is **more than** 4. What are the hypotheses?

### Step 2: Specify a level of significance.
You may have heard "alpha equals point oh-five!" before. A lower case alpha is used to denote level of significance (or, more cryptically, Type I error). It is the probability of rejecting the null hypothesis given that the null hypothesis is actually true. Canonical levels are 0.01, 0.05, and 0.10. A higher alpha level means that you are likelier to reject your null hypothesis, but this makes it likelier that you **erroneously** reject your null hypothesis. The most common level is 0.05, but check your field's standards!

### Step 3: Calculate your point estimate.
In this case, your point estimate will simply be your sample mean - this should be easy!

### Step 4: Calculate your test statistic.
In this case, your test statistic will be z = (x-bar - mu) / sigma/sqrt(n) - should still be easy!

### Step 5: Find your p-value.
The definition of p-value is "the probability that, given a re-run of your experiment, you get a test statistic that is as extreme or more extreme than the test statistic you just received." Within the context of what we just did in Step 4, your p-value indicates that a re-run of the experiment would yield a z-score that is as extreme or more extreme than the one you just got.

This is a measure of how extreme our experiment's results are. This should make sense - remember above how we talked about quantifying how far observations are from their expected value (a.k.a. population mean). This is the same thing! We're quantifying how far our sample statistic (a summary of our sample observations) is from our expected value of the statistic by seeing how many standard errors (standard deviations) we are from the expected value.

- If that p-value is less than your pre-determined alpha level, then you can reject your null hypothesis and conclude that your alternative hypothesis is indeed correct.
- If that p-value is more than your pre-determined alpha level, then you **fail to reject** your null hypothesis and **cannot conclude that either the null or the alternative is correct**.
- If that p-value is equal to your pre-determined alpha level, then your results are inconclusive. Start a brand new study over or assume that you cannot reject your null hypothesis.

[Let's do this in Python!](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.ttest_1samp.html)

### Discussion of p-hacking.

### But what about proportions or categorical data?
There are certainly other things we can look into - testing whether two proportions are equal, testing whether one mean is greater than another, testing whether or not there is an association between two categorical variables, testing whether your correlation is significantly greater than zero or not. We simply don't have time to go through every individual statistical test.

If you think a statistical test is appropriate, think about what you seek to show, set up your hypotheses, and then go hunting online for the proper test. The SciPy documentation is incredibly robust and there are myriad statistical sites that will help you to identify the proper test. (I'm sure that your classmates and instructors would be willing to help as well!)

### Note on Nonparametric Statistics
Thus far, all of our tests have been **parametric.** That is, we have assumed a certain distribution for our data. However, there are alternatives in the case where we cannot assume a particular distribution for our data. When we make no assumptions about the distribution for our data, we call our data **nonparametric**. For nearly every parametric test, there is a nonparametric analog available.

## Conclusion
- Q & A
- Lab