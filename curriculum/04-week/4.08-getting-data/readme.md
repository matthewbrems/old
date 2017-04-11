---
title: Getting Data
duration: "2:30"
creator:
 name: Joseph Nelson
 city: DC
---

# ![logo](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Getting Data

This is a big lesson. And it's important.

## Learning Objectives

At the end of this session, you will:
- Have a clear understanding of how APIs work, and why they are increasingly prevalent
- Know how HTTP protocol works
- Gain first hand experience using your very first API

## Overview of APIs

We'll first run through this [deck](./intro-to-apis.pdf) on why APIs are increasingly prevalent, and their value.

### HTTP

Our discussion of how HTTP works is [here](https://github.com/josephofiowa/GA-DSI/blob/master/intro-to-apis-python/HTTP-protocol.md)

## Using Our First API!

Visit the API we'll be using here: www.omdbapi.com

The script we'll follow to make requests and use our very first API (gasp!) is available [here](.code/api-usage-example.py)

## Webscraping 101

Now, we'll take a look at collecting data when things are so neatly structured for us. This is where webscraping comes in.

We'll first be scraping [this](.code/example.html) page. Our script for doing so is available [here](.code/webscraping.py)

### Independent Practice

Finally, let's build our **very own** scraper on data from out in the wild.

I'd like you to scrape the first page of quotes from this Lincoln page: http://www.abrahamlincolnonline.org/lincoln/speeches/quotes.htm

Alternatively, scrape from here: http://www.successories.com/iquote/author/291/abraham-lincoln-quotes/1 (preferred)

Add all the quotes to a list.


## Additional Resources

- [Blog post on json with pandas](https://www.dataquest.io/blog/using-json-data-in-pandas/)
- [API article Wikipedia](https://en.wikipedia.org/wiki/Application_programming_interface)
- [Programmable web](http://www.programmableweb.com/)
- Please also download [Anaconda with Python 2.7 (not 3.5)](https://www.continuum.io/)
- A [discussion](https://medium.com/ggv-capital/a-tale-of-2-api-platforms-39f8dfd77436#.92bwnnahv) on APIs used properly for development (Slack) vs improperly (Twitter)