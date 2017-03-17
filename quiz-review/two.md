# ![logo](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Quiz Two Review

## Confidence Intervals and Hypothesis Testing



## Boolean Filtering

Boolean filtering is a way to identify subsets of our dataframe.

```python
# boolean filtering: only show users with age < 20
young_bool = users.age < 20         # create a Series of booleans...
users[young_bool]                   # ...and use that Series to filter rows
users[users.age < 20]               # or, combine into a single step
```

Try it yourself: [link](https://github.com/ga-students/DC-DSI4/tree/master/curriculum/02-week/2.09-pandas)

## Methods and Attributes

An attribute is a variable that is looked up on another object using dot syntax: obj.attribute.

A method is, technically, a special type of attribute that also accepts arguments, performs operations, and potentially returns values. Methods are like functions available within Python classes.

More via [Stack Overflow](http://stackoverflow.com/questions/28798781/differences-between-data-attributes-and-method-attributes)