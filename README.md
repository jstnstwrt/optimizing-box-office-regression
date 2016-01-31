# optimizing-box-office-regression

This repository demonstrates how to scrape weekly box office data from (http://www.boxofficemojo.com/), parse and transform the data so that it can be more easily analyzed, prefrom some descriptive analyses of the data, and build a linear regressin prediction model of how long a movie will remain in theatres using only data available at the time of observation. The analysis is completed using ipython notebooks.

### Using the code

There are 4 main scripts:
  1.  *scraping_movie_data.ipynb* contains the code to actually pull down the desired data from the booxofficemojo website. This uses the requsets and beautiful soup libraries to aqcuire the data, and then store in a pickle file. 
  2.  *data_engineering.ipynb* contains scripts to parse the data pulled down from the web. We clean the data and make it amenable for analysis. 
  3.  *exploratory_data_analysis.ipynb* contains the some analysis to get a better sense of the data with an eye towards using it to create a regression model. We identify some outlier observations and find some distinct classes of observations that we create dummie variables for. 
  4.  *model_selection.ipynb* contains all the code to find and create the linear prediction model. This scritpt also contains functionality to subset the complete feature set on the fly to account for how much data is *observed* (or available to be used for prediction).
