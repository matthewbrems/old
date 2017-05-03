
# REQUIRES DEV VERSION OF STATSMODELS
# git clone git://github.com/statsmodels/statsmodels.git
# python setup.py install

import pandas as pd
%matplotlib inline

url = 'https://raw.githubusercontent.com/ga-students/DC-DSI4/master/curriculum/09-week/9.07-arima/euretail.csv?token=ANUte61i5c3U9OvhEX-KQttIr8qJ-eiKks5ZEiXjwA%3D%3D'

df = pd.read_csv(url)
df = df.set_index(['Year'])
df.head()
df.stack().plot()

# define Dickey-Fuller test
from statsmodels.tsa.stattools import adfuller
from matplotlib import pyplot as plt
def test_stationarity(timeseries):

    #Determing rolling statistics
    rolmean = timeseries.rolling(window=12).mean()
    rolstd = timeseries.rolling(window=12).std()

    #Plot rolling statistics:
    fig = plt.figure(figsize=(12, 8))
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    
    #Perform Dickey-Fuller test:
    print 'Results of Dickey-Fuller Test:'
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print dfoutput 

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df.diff(periods=4)[4:]

# regular diff
# every 4th thing is minus the 4th thing prior
# so q4 minus prior q4
diff0 = df.stack().diff(periods=4)[4:]
diff0.plot(title='European Retail Trade Differenced')
plot_acf(diff0, lags=30)
plt.show()
plot_pacf(diff0, lags=30)
plt.show()
test_stationarity(diff0)

# additional diff
diff1 = diff0.diff()[1:]
diff1.plot(title='European Retail Trade Differenced Twice')
plot_acf(diff1, lags=30)
plt.show()
plot_pacf(diff1, lags=30)
plt.show()
test_stationarity(diff1)

import statsmodels.api as sm
data = df.stack().values
model = sm.tsa.statespace.SARIMAX(data, order=(0,1,1), seasonal_order=(0,1,1,4)) ## seasonal_order(p,d,q,m)
results = model.fit()
print results.summary()

# Don't plot the first 5 values, to account for data loss when differencing (d=1 + D=5)
residuals = results.resid[5:]
plt.plot(residuals)

plot_acf(residuals, lags=30)
plot_pacf(residuals, lags=30)


model = sm.tsa.statespace.SARIMAX(data, order=(0,1,2), seasonal_order=(0,1,1,4))
results = model.fit()
print results.summary()

import numpy as np
# forecasting
res = model.fit()
preds = res.forecast(12)
fcast = np.concatenate((data, preds), axis=0)

plt.figure();
plt.plot(data, 'o' , fcast, 'r--');

