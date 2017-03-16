---
title: Introduction to Inferential Statistics - Part 1
duration: "1:30"
creator:
    name: Matt Brems
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to Inferential Statistics - Part 1
Week 2 | Lesson 2.05

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Define target population, sampled population, sample, sampling unit, observation unit, sampling frame, probability sampling, and non-probability sampling, and identify these within the context of a real-world situation.
- Differentiate between descriptive and inferential statistics.
- Calculate, interpret, and apply properties of univariate and bivariate descriptive statistics.


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- This should've been completed as pre-work before starting the course, but if you didn't complete it, please complete the course pre-work on statistics.

---

## Introduction
When I say "statistics," what comes to mind?

<details><summary> **How do we define statistics?**
</summary>
- "Statistics is the study of the collection, analysis, interpretation, presentation, and organization of data." - Wikipedia
- "A branch of mathematics dealing with the collection, analysis, interpretation, and presentation of masses of numerical data." - Merriam-Webster
- "Statistics is the science of data." - The Ohio State University, STAT 1450
- "Statistics is a method of solving problems through data-driven quantitative reasoning." - Matt Brems
</details>

## Sampling

Before we get to work on data, we must consider how data will be collected. It is important to collect data in a manner that is theoretically proper and that your analysis will account for the "real-world" issues that will naturally arise when working.

It is often expensive, time-consuming, and/or impossible to take measurements on every person or observation of interest. Recall last week's example where we tried to find the true average height of all undergraduate women at Ohio State. In order to overcome this, statisticians have developed a variety of methods to collect data from a subset of these observations of interest in an intentional manner and then extrapolate those findings to the larger group of interest.

Speaking broadly, in statistics we will take measurements on a sample to learn about the population. We must, however, be *very* careful about how we define this population, as any inferences we make based on a sample are extended only to the sampled population.

### Sampling Terms
- **Sample:** A subset of a population.
- **Target Population:** The population about which we want to make inferences; the population of interest.
- **Sampled Population:** The population about which we *can* make inferences; the population from which we sample.
- **Sampling Unit:** A unit that can be selected for a sample.
- **Observation Unit:** An object on which a measurement is taken.
- **Sampling Frame:** A specification of sampling units in the population from which a sample may be selected.

A lot of my work at 0ptimus revolved around survey design and analysis. My goal is to estimate the proportion of people in New Hampshire who plan to vote for each candidate in the Republican and Democratic Presidential primaries. I have a voter file containing the names, contact information, and demographic data of everyone registered to vote within the state of New Hampshire - roughly 900,000 people. I choose to call about 10,000 people. Of those called, about 6% responded the question "For whom do you plan to vote in the upcoming Presidential primary?"

- Describe the sample.
- Describe the target population.
- Describe the sampled population.
- Describe the sampling unit.
- Describe the observation unit.
- Describe the sampling frame.

<details><summary> **Let's try this together.**
</summary>
Let's go back to our example from earlier. I am interested in finding the true average height of all undergraduate women enrolled at Ohio State. Rather than taking a census of all 25,000 undergraduate women, I decide to sample fewer than 25,000 women. I contact the Ohio State Registrar for a list of names and contact information for all undergraduate women. I identify 1,000 women whose height I wish to measure and reach out to them. 249 women show up on the proper date and time to have their heights taken.
- Describe the sample.
- Describe the target population.
- Describe the sampled population.
- Describe the sampling unit.
- Describe the observation unit.
- Describe the sampling frame.
</details>

<details><summary> **Your turn to practice!**
</summary>
(Taken from ["Sampling: Design and Analysis", 2nd ed., Sharon Lohr, 2010.](http://evalenzu.mat.utfsm.cl/Docencia/2016/Primer%20semestre/Metodos%20Estadisticos%20en%20Ingenieria/Apunte1.pdf)) Many scholars and policy makers are interested in the proportion of homeless people who are mentally ill. Wright (1988) estimates that 33% of all homeless people are mentally ill by sampling homeless persons who received medical attention from one of the clinics in the Health Care for the Homeless (HCH) project.
- Describe the sample.
- Describe the target population.
- Describe the sampled population.
- Describe the sampling unit.
- Describe the observation unit.
- Describe the sampling frame.
</details>


### Three last notes about sampling...
#### When sampling, one can conduct probability samples or non-probability samples. 
In a probability sample, the probability of getting a particular sample can be calculated. (Equivalently, each unit in the population has a known probability of selection.) In a non-probability sample, this is not the case. When we want to conduct standard inference, one of the first assumptions made is that observations come from a random probability sample. (Only recently is research diving into methods of conducting inference from nonprobability samples.) Whenever you generate a confidence interval or execute a hypothesis test, you rely on the assumption that your data comes from a random probability sample. (It is far more common to see "random sample," where the "probability" is implied.)

#### There are multiple types of random probability samples - we list the basic ones here:
- **Simple Random Sample (SRS):** A sample is a simple random sample when every possible subset of n units in the population has the same chance of being the sample.
- **Stratified Random Sample:** A sample is a stratified random sample when the population is broken into subgroups (sometimes called strata), a simple random sample is pulled within each subgroup, and those simple random samples are combined into one larger "stratified" sample.
- **Cluster Random Sample:** A sample is a cluster sample when observation units are grouped into larger sampling units (sometimes called clusters), a sample of larger sampling units are selected, and then observation units within the selected larger sampling units are selected.

#### Replication
Whether it be for an academic journal, needing to replicate results for your supervisor, or in-house testing among peers, it is often desirable to be able to replicate your work. When drawing a random sample, however, the computer relies on randomness and this is difficult to replicate.

However, computers cannot do anything that is *truly* random. They can, however, generate pseudorandom numbers. Because of this, you can actually set what is called a "seed" so that you can return the computer to a particular state before generating a random number. Thus, if you set your seed to be 6, then generate a random sample, set your seed to be 6 again, and generate another random sample, you'll notice that the exact same random sample was generated! 

```python
import random ## This is exactly like when we imported math - actually, it's from the same place!
random.seed(insert_integer_here)
random.sample(list_or_series_to_be_sampled,sample_size)
```

## Descriptive vs. Inferential Statistics
<details><summary> **How would you define descriptive statistics? Inferential statistics?**
</summary>
Loosely speaking:
- Descriptive statistics is the branch of statistics that deals with summarizing available information.
- Inferential statistics is the branch of statistics that deals with generalizing available information to a larger population.
</details> 

**Discussion:** In what cases would we want to use descriptive statistics? In what cases would we want to use inferential statistics? Does it make sense to use one without the other?

## Univariate and Bivariate Statistics and Parameters
Formally, a statistic is a function of the data. You can think about this like the standard deviation function we developed last week - we used every data point as an input and the output was the value of the sample standard deviation.

Formally, a parameter is a characteristic of the population. This might be the true average height of all undergraduate women at Ohio State, the true median salary in the United States, or the true standard deviation of hours of Netflix watched among those between 18 and 35 years old. Unless we have access to every observation in the population and the ability to measure each observation, it will be impossible to know the true value of the parameter of interest. However, we can draw a sample and calculate a statistic which, assuming our sample and measurements are done properly, should be a relatively accurate and precise estimate of our parameter.

More succinctly, we might say that "statistics estimate parameters."

### Univariate Statistics and Parameters
Recall that in the univariate case (one variable), we are interested in describing the distribution of a variable, where distribution is the set of all possible values the variable can take on and how frequently it takes on those values.

<details><summary> **Remember the questions we asked that addressed the most important aspects of a variable's distribution:**
</summary>
- What is the center of the distribution? (Mean, Median, Mode*)
- What is the spread about the center of the distribution? (Standard Deviation/Variance, Range/IQR)
- What is the shape of the distribution? (Skewed/Symmetric, Unimodal/Multimodel)
</details>

**Check:** Can measures of spread be zero? If so, when? If not, why not? Can measures of spread be negative?

**Check:** For skewed data, which measure(s) of center and spread is/are most appropriate? Why?

**Check:** For symmetric data, which measure(s) of center and spread is/are most appropriate? Why?

### Bivariate Statistics and Parameters
When working within the univariate case, we're interested in knowing what the distribution of a particular variable looks like. In the bivariate (two variable) case, however, we're more interested in the relationship between two variables. The most common measures are the correlation (Pearson correlation coefficient) and the covariance.

#### Pearson's Correlation
Correlation (the Pearson correlation coefficient) measures the *strength* and *direction* of the *linear* relationship between two variables and can take on any value between -1 and +1. The sample correlation is denoted by r, while the population correlation is denoted by rho.

Values close to -1 or +1 indicate a strong and linear relationship between the two variables. Values close to 0 indicate a weak and/or nonlinear relationship between the two variables. Values above 0 indicate a positive relationship between the two variables. Values below 0 indicate a negative relationship between the two variables.

# ![](https://upload.wikimedia.org/wikipedia/commons/d/d4/Correlation_examples2.svg)
Graphic pulled from [Wikipedia's article on correlation and dependence.](https://en.wikipedia.org/wiki/Correlation_and_dependence)


If you want to calculate the correlation between two variables in Python, use the following code:
```python
import numpy as np
np.corrcoef(var1,var2)
```

##### Properties of Pearson's Correlation
- -1 <= Corr(X,Y) <= 1
- Corr(X,Y) = Corr(Y,X)
- If X and Y are independent, then Corr(X,Y) = 0. (The converse does not hold!)
- Corr(a + bX,c + dY) = Corr(X,Y) if bd > 0
- Corr(a + bX,c + dY) = -Corr(X,Y) if bd < 0

#### Covariance
Covariance is a generalization of correlation that measures how significantly two variables change together and can take on any value. Taking on any value means that interpreting covariance by itself is difficult to do. It makes more sense to compare two correlations than two covariances.

If you want to calculate the covariance between two variables in Python, use the following code:
```python
import numpy as np
np.cov(var1,var2)
```

##### Properties of Covariance
- Cov(X,X) = Var(X)
- Cov(X,Y) = Cov(Y,X)
- Cov(a + bX,c + dY) = bdCov(X,Y)

## Conclusion
- Q & A
- Lab

## Resources
- ["Sampling: Design and Analysis", 2nd ed., Sharon Lohr, 2010, online .pdf](http://evalenzu.mat.utfsm.cl/Docencia/2016/Primer%20semestre/Metodos%20Estadisticos%20en%20Ingenieria/Apunte1.pdf)
- [Stats Cookbook](https://github.com/mavam/stat-cookbook)