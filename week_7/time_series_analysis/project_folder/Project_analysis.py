import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.ar_model import AutoReg, ar_select_order
from statsmodels.tsa.arima.model import ARIMA
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error

# Set the figure size to (14,6)
plt.rcParams['figure.figsize'] = (14,6)

# ignore warnings
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('remainder_temp.csv', index_col=0, parse_dates=True)
df.plot()
plt.title('Remainder')
plt.show()
df.mean()

# apply the augmented Dicky-Fuller stationarity test

# recap: The null hypothesis is that the time series is NOT-stationary
# i.e. a small p value, less than 0.05, means that you have a stationary series

def print_adf(data):
    """ 
    Prints the results of the augmented Dickey Fuller Test
    """
    adf_stats, p, used_lag, n_obs, levels, information_criterion = adfuller(data)
    
    print(f""" 
              adf_stats: {adf_stats}
              p: {p} 
              used lag: {used_lag} 
              number of observations: {n_obs}
            
              CI 99%: {levels['1%']}
              CI 95%: {levels['5%']}
              CI 90%: {levels['10%']}
              information criterion (AIC): {information_criterion}
            """)

print_adf(df['remainder'])

# Plot the partial autocorrelation function
plot_pacf(df['remainder']);
plt.show()

# Use ar_select_order - brute force method that tries different models and takes the best one
order = ar_select_order(df, maxlag=20, old_names=False)

# How many lags does ar_select_order suggest?
print(order.ar_lags)

# Fit a statsmodels AutoReg model
ar_model = AutoReg(df['remainder'], lags=4, old_names=False).fit()

# Plot the prediction
df.plot()
plt.plot(ar_model.predict(), label='ar_predictions')
plt.legend()
plt.show()

# Fit an ARIMA model
arima_model = ARIMA(df['remainder'], order=(1,0,1)).fit()

# Plot all time series
df.plot()
plt.plot(ar_model.predict(), label='ar_predictions')
plt.plot(arima_model.predict(), label='arima_predictions')
plt.legend()
plt.show()

# Plot the autocorrelation between lags
plot_acf(df)
plt.show()

# Plot the partial autocorrelation between lags
plot_pacf(df)
plt.show()

auto_arima_model = auto_arima(df['remainder'], start_p=0, start_q=0, max_p=10, max_q=10)
print(auto_arima_model)

# Building the model on our train data
data_train = pd.read_csv('temp_train.csv', parse_dates=True, index_col=0)
data_train = data_train[['temp_c']]

data_train.plot()
plt.show()

data_train.mean()
data_train['diff1'] = data_train['temp_c'].diff()
print_adf(data_train['diff1'].dropna())

station_data_train = data_train[['diff1']].dropna()
station_data_train.plot()
plt.show()

auto_arima_model = auto_arima(data_train['temp_c'], start_p=0, start_q=0, max_p=15, max_q=15, max_d=3)
auto_arima_model

model = ARIMA(data_train['temp_c'], order=(15,0,1)).fit()

plt.plot(data_train['temp_c'], label='train_data')
plt.plot(model.predict(), label='arima_predictions')  # this is called in-sample predictions, predictions on test data
plt.legend()

plt.show()

seasonal_dummies = pd.get_dummies(data_train.index.month,
                                  prefix='month',
                                  drop_first=True).set_index(data_train.index)

data_train = data_train.join(seasonal_dummies)

model_season = ARIMA(data_train['temp_c'], order=(15,0,1), exog=seasonal_dummies).fit()
plt.plot(data_train['temp_c'], label='temp_data')
plt.plot(model.predict(), label='arima predictions -- no seasnonality')
plt.plot(model_season.predict(), label='arima predictions -- seasonality')
plt.legend()

plt.show()

rmse_no_seasonality = np.sqrt(mean_squared_error(data_train['temp_c'], model.predict()))

rmse_seasonality = np.sqrt(mean_squared_error(data_train['temp_c'], model_season.predict()))

model.forecast()
model_season.forecast(exog=seasonal_dummies.iloc[0])
model.predict(start='2021-01-01', end='2021-12-01')
model_season.predict(start='2021-01-01', end='2021-12-01', exog=seasonal_dummies.iloc[0:335])

# on the test data

temp_test = pd.read_csv('temp_test.csv', parse_dates=True, index_col=0)

# add predictions from both models

temp_test['predictions'] = model.predict(start='2021-01-01', end='2021-12-01')

temp_test['predictions_season'] =  model_season.predict(start='2021-01-01', 
                                                           end='2021-12-01', exog=seasonal_dummies.iloc[0:335])

plt.plot(temp_test['temp_c'], label='temp_test.csv_data')
plt.plot(temp_test['predictions'], label='arima predictions -- no seasnonality')
plt.plot(temp_test['predictions_season'], label='arima predictions -- seasonality')
plt.legend()

plt.show()

model.predict(start='2021-01-01', end='2021-12-01').iloc[-1]
rmse_no_seasonality_t = np.sqrt(mean_squared_error(temp_test['temp_c'], temp_test['predictions']))

rmse_seasonality_t = np.sqrt(mean_squared_error(temp_test['temp_c'], temp_test['predictions_season']))

