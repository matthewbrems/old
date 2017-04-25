# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Case Study in Bayesian Analysis 1
Week 8 | 8.08

## Introduction

In the 2012 US presidential electoral cycle, Nate Silver of [538](http://fivethirtyeight.com) won acclaim for utilizing a Bayesian approach to successful poll prediction. In particular, he used a method called a *Monte Carlo Markov Chain* (MCMC). (Get excited for tomorrow!)

We're going to start our nascent data science careers in this lab with something slightly less ambitious but no less relevant to the material we've gone through so far.


## Exercise

This table provides the likelihood/prior conjugate prior combinations that ensure computational tractability for calculation of posterior distributions.

| Prior  | Likelihood  |
|---|---|
| Beta  | Binomial  |
| Dirichlet  | Multinomial   |
| Gamma  | Gaussian |
| Gaussian  | Gaussian |


#### Requirements
Some background:

We are  going to use the `Beta Function` today to do our first real computational Bayesian exercise! See the following:
`$\frac{1}{B(\alpha, \beta)}x^{\alpha-1}(1-x)^{\beta-1}$.`

Wait, what's `B`? We can define `B` as the following:

`$$B(a,b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$$`

Your task is now (in part) to compute that in Python!!

**Bonus:**
- Write 300 words about how Bayesian Analysis is different from a traditional approach
- Include at least one *additional* way to implement the Beta function that could be computationally tractable. Challenge accepted!

#### Starter code

[Use the starter code found here to get going](starter-code.ipynb)

#### Deliverable

Complete the lab and provide a solution!

#### Additional Resources

For those of you who want to read further:

- [Here is a more detailed treatment on campaign/polling/votes and how Bayesian analysis is applied](http://www.stat.columbia.edu/~gelman/presentations/gelman_ieor.pdf)

- [This is an interesting analysis of the possible determinants of voter political preferences in the United States](http://www.stat.columbia.edu/~gelman/presentations/redbluetalkubc.pdf)
