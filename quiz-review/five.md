# ![logo](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Quiz Five Review

## Classes

Classes are what power object-oriented programming in Python.

Classes are blueprints for objects. (A blueprint for a house)
Objects are instanitiated classes. (A house with 4 rooms)
Objects have methods and attributes. Methods are functions within an object (a function that calculates the prices of a home). Attributes are variables within objects (whether the house has a chimney, yes/no)

Classes enable us to write modular, efficient, DRY (don't repeat yourself) code. Every time we instatiante a `LinearRegression()` or a `DecisionTreeClassifier()`, we are utilizing classes.

For you:
https://github.com/ga-students/DC-DSI4/blob/master/curriculum/06-week/6.10-python-classes/PythonClassesSlides.pdf On slide 10, what word is used to refer to the yellow? What word refers to the red? What word refers to the blue?

## Bootstrapping

Bootstrap resampling is a technique we use to find true point statistic estimates of populations.

I'll start with an example. Imagine we're trying to identify the true median height of all people that come to GA. While we could, in theory, ask for everyone's time, it's unrealistic we would have the ability to do so. Thus, we take a sample of people at GA (we'll say n=50), we measure their heights, and we take the median of that sample.

This method will generally work. However, imagine that a couple of the Washington Wizards happen to be on campus one day because they're starting some company in 1776. If our sample includes a couple of those guys, it's going to be positively skewed.

Now, imagine we have this same n=50 sample, and instead of strictly taking the median of it, we want to bootstrap for the median. We, thus, resample our 50 people (with replacement). In this resampling, it is increasingly less likely that we select one of the two Washington Wizard outlier players. We are *implicitly down-weighting the impact of their skew on our median.*

Now, to generalize a bit, this works because we're utilizing the central limit theorem to approach a theoretical true median. (Remember playing with our tool [here](http://onlinestatbook.com/stat_sim/sampling_dist/index.html) (click "Begin"))

So, big picture: bootstrap resampling helps _minimize_ skewed samples as compared to not doing any resampling at all. To directly answer your question, it depends a bit on _how bad_ our sample is in the first place. On balance, we don't necessarily know how bad our sample is compared to the true population median, and because bootstrap resampling generally helps (like the above example), it is a highly effective tactic.

(For more info, I recommend [this podcast](https://dataskeptic.com/blog/episodes/2016/the-bootstrap ) by data skeptic for an intuitive refresher at a high level)

The bootstrapping pseduo code reads like the following:

```
for specified number of bootstrap iterations
    create a bootstrap sample by randomly selecting observations with replacement from your sample 
        (same size as sample)
    calculate the statistic of interest on bootstrap sample

calculate lower and upper percentile bounds of bootstrap statistics according to threshold
```

You should be prepared to write a bootstrap function by hand. Review [our lesson](https://github.com/ga-students/DC-DSI4/tree/master/curriculum/06-week/6.09-bootstrapping) for doing so.

