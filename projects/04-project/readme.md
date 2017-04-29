# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: Predicting Terrorism / Bayesian Inference (Mini)

Over the course of the last week, we've been investigating Bayesian methods to understand various populations. This project calls on you to apply Bayesian inference (and other tactics) to a fascinating dataset: the Global Terrorism Database.

## About the Dataset

From Kaggle:
> The Global Terrorism Database (GTD) is an open-source database including information on terrorist attacks around the world from 1970 through 2015 (with annual updates planned for the future). The GTD includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period and now includes more than 150,000 cases. The database is maintained by researchers at the National Consortium for the Study of Terrorism and Responses to Terrorism (START), headquartered at the [University of Maryland](http://start.umd.edu/gtd/). 

> Geography: Worldwide

> Time period: 1970-2015, except 1993 (2016 in progress, publication expected June 2017)

> Unit of analysis: Attack

> Variables: >100 variables on location, tactics, perpetrators, targets, and outcomes

> Sources: Unclassified media articles (Note: Please interpret changes over time with caution. Global patterns are driven by diverse trends in particular regions, and data collection is influenced by fluctuations in access to media coverage over both time and place.)

> Definition of terrorism:

> "The threatened or actual use of illegal force and violence by a non-state actor to attain a political, economic, religious, or social goal through fear, coercion, or intimidation."

You will need to make use of the [codebook](http://start.umd.edu/gtd/downloads/Codebook.pdf) that functions as a data dictionary.

Moreover, this [2007 paper by LaFree (UMD)](https://ccjs.umd.edu/sites/ccjs.umd.edu/files/pubs/FTPV_A_224594.pdf) introduces the dataset very well.

You must download the 28MB zip file, unzip it, and work with the 128MB csv on your machine.


## Goal

While there are fewer requirements of this project, the open-ended nature of the ask should force you to think about your approach and research methods. When assessing your performance on this project, we are equally interested in the method and questions you are asking as much as the implementation of those methods.

In the process of maintaining the GTD, you'll note that the year 1993 has zero recorded instances. Due to the many actors maintaining the dataset, this year has been lost.

Your goal is to impute the number of bombing/exposions that occured in 1993. (You'll note that **even we** do not have the answer. That increases our focus on your methods.)

The structure of your project must include four components: exploratory data analysis, Bayesian inference to examine the the difference in incidences across the globe, a model to impute the missing values, and a brief description of your methods. 


### Part One: EDA

You should gain an understanding of the attacks (focus on `attacktype1`), their distribution across the world, and their frequency.

You will discover different things than your classmates on this portion. Your presentation should include compelling visualizations describing terror incidents around the world.

You are **required** to produce at least one visualization that is indexed by time. For example, the number of bombings that occurred by year over time.


### Part Two: Bayesian Inference

Terror attacks are a ripe area of research for Bayesian inference. Given their infrequency, it is (thankfully) difficult for us to assume a high number of samples that approach some normal distribution.

Because of this, we should construct a prior about the amount of terror a given area has seen and update that prior with new information (like a new year of attacks or a contrasting country from within the same region). 

You should compare two populations of your choosing using Bayesian inference. We want to know if the amount of terror one area has seen differs in a significant way than another area (or time period!)

For example, if you are interested in knowing if one country in South America differs in a significant way from another area, you may make your prior  assume that some country is a country in South America with μ average attacks and σ variation across South American countries. You would then update that prior with the information of a single country in South America as well as a separate country in South America. How significantly do the resulting posteriors differ? (An important assumption made here is that the time periods are being held constant, perhaps a single year.)

You should structure your own test of populations rather than using the above example. If you're unable to setup a different test, brainstorm with your squad in the Slack chat.

You must justify the prior you selected and interpret your results (use credible intervals.) Remember you can attempt to use different priors (but don't "prior hack" to affect your output!)


### Part Three: 1993

The year 1993 is missing from our dataset! Given there is a wealth of information across different types of attacks, we will focus analysis on `attacktype1` bombings (category 3, as per the codebook)

For this section, you should determine a methodology that allows you to best fill in the missing values. Perhaps you want to consider hemispheres to be separate models, for example. (That's the only hint you'll receive - and even that hint is not an optimal option.)

Once you've created your methodology and imputed the number of bombings in 1993, you should feel free to apply your methodology to **OTHER** attack categories. (Bonus opportunity: turn your method into a pipeline. Use that pipeline to fill in other missing attack values.)


### Part Four: Methods

Please draft a max two page (or four pages double spaced) report discussing your methodology and findings. Visualizations may be included in an appendix.

Your write-up should have two parts: the Bayesian test you constructed and the values you imputed for 1993 attacks.

In your Bayesian inference section, be sure to defend your prior. Comment on your results of the differing populations.

In your missing value imputation modelling portion, justify the model or tactic you used. Bear in mind simply averaging by hemisphere can, theoretically, be a solution. Err on the side of simple and elegant rather than complex to be complex.


## Other

If you're enjoying this research (and want to go further), get in touch with Joseph. Your results can be shared with UMD START and academics. ([Gary LaFree](http://www.start.umd.edu/people/gary-lafree) or [Erin Miller](http://www.start.umd.edu/people/erin-miller))

Moreover, if you want to dig into the literature, check out [Dr. Schrodt's](http://parusanalytics.com/about.html) Bayesian approach to understanding terror.

Thank you to [Dr. Joseph Young](http://fs2.american.edu/jyoung/www/) for his thoughts on this research.

