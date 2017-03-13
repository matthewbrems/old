# ![Logo](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Notebooks and CSVs Lab

For this lab, you are optionally (encouraged!) to submit a publicly viewable notebook via NBViewer. Bear in mind to do so you will have to create a new public repository on your own Github, add this lab's Jupyter notebook to it, and then use the link of that notebook on [NBViewer](nbviewer.jupyter.org).

We'll be working with the infamous [iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set)

Because you're working with a lab that is not in our repo (you're editing the public NBViewer notebook you created in class), you can not submit this via pull request. Instead, submit a link to your notebook [here](https://docs.google.com/a/generalassemb.ly/forms/d/e/1FAIpQLSeaGfpKtEbqaol4E0-C_m171HyCLkVzBS4oVrBD5fGUyCQKDA/viewform?c=0&w=1).

## 1. Read in the iris dataset located in 1.10-notebooks-and-CSVs-lab/data 

Hint: this is related to how we did this in-class:

```python
with open('sales.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
```

But unlike this in-class example, you're going to want to produce a list of lists. Hmmmm...
(Hint 2: you're going to need to initialize a list. We recommend calling that list 'dataset' and adding each row to that list.) 

## 2. Notice the first list in your dataset is the column names. Eliminate it.


## 3. Identify the number of observations in your dataset


## 4. Identify what species is in row four of your dataset


## 5. Calculate the average sepal length in the dataset (sepal is the first entry in each list)


## 6. Calculate the average sepal length of setosa flowers using a loop


### BONUS: Calculate the average sepal length of flowers of any given species
This may be a function that takes species as a parameter.


