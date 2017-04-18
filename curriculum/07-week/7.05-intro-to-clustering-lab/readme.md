---
title: K Means Clustering Lab
type: lab
duration: "1:25"
creator:
    name: 
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) K-Means Clustering Lab

## Introduction

We know what clustering is, how to setup your data for clustering, and how to evaluate your analysis. Now it's time to put your skills to the test! For this lab session, we are going to complete a full k-means clustering process using Python. 

You're working for a large marketing agency as a data scientist, and we're trying to market a high-end luxury good to consumers. We know that we want to target consumers with large incomes, however we do not know anything else about the demographic makeup of our target market. You're given a [dataset](./assets/datasets/adult.csv) with census information on income size and various other demographic indicators. Your task is to perform a clustering analysis to determine which demographic indicators relate to income size so that we can better target our marketing efforts.

## Exercise

#### Requirements

- Import the data
- Format the data - we've been given some messy census data; your job is to make sense of it
- Perform a K-Means test to inform us about our target market demographics
    - Use Scikit-Learn
- Find a Silhouette Score for the clusters to evaluate your analysis

Just as in a real life scenario, the data and your analysis will not always be clear cut. While you may be wondering when you've succeeded in solving the problem,  we're looking for your best recommendations based on the available data. Work through the process until you and your teammate have enough information to provide an in-depth analysis to the agency.

**Bonus:**
- Perform a K-Means analysis on another subset of the data
- Find the centroids of your clusters (Hint: Use Scikit!)

#### Starter Code & Data

- Download the [data](./assets/datasets/seeds.csv)
- Grab the [starter code](./code/starter-code.ipynb) to get started. 
- Data FYI: http://archive.ics.uci.edu/ml/datasets/seeds

## Additional Resources

- A link to [K-Means Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- Extra relevant [Silhouette Score Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)
