import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from statsmodels.tsa.ar_model import  AutoReg, ar_select_order
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# set figure size to (14, 6)
plt.rcParams['figure.figsize'] = (14, 6)
#########################################################################################
#reading data
temp_train = pd.read_csv('/home/damoon/damoon_spiced_academy/07_week/escad_data/temp_train.csv', parse_dates=True, index_col='date')
temp_train.head()
temp_train.info()
temp_train.shape
temp_train.drop(columns=['temp'], axis=1, inplace=True)
########################################################################################
def plot_timeseries (df, title=" ", ylim=True):
    df.plot()
    plt.title(title)
    if ylim:
        plt.ylim(ymin=0)
    plt.ylabel("Temperature in C")
    plt.show()
#######################################################################################
plot_timeseries(temp_train, title="average temperature over time")
#######################################################################################
temp_train['timestep'] = list(range(len(temp_train)))
temp_train.head()
#####################################################################################
m_trend = LinearRegression()
X = temp_train[['timestep']]
y = temp_train[['temp_c']]
m_trend.fit(X, y)
####################################################################################
temp_train['trend'] = m_trend.predict(X)
temp_train.head()
plot_timeseries(temp_train[['temp_c', 'trend']], title="average temprature over time vs Trend")
##################################################################################
temp_train['year'] = temp_train.index.year
temp_train['month'] = temp_train.index.month
temp_train['month_name'] = temp_train.index.month_name()

temp_train.head()
temp_train.info()
#####################################################################################
fig, ax = plt.subplots()

temp_1998 = temp_train[temp_train['year']==1998]
temp_1999 = temp_train[temp_train['year']==1999]
temp_2000= temp_train[temp_train['year']==2000]



ax.plot(temp_1998['month_name'].drop_duplicates(), temp_1998.groupby(['month']).mean()['temp_c'], label='1998')
ax.plot(temp_1999['month_name'].drop_duplicates(), temp_1999.groupby(['month']).mean()['temp_c'], label='1999')
ax.plot(temp_2000['month_name'].drop_duplicates(), temp_2000.groupby(['month']).mean()['temp_c'], label='2000')

plt.title("1998 vs 1999 vs 2000")
plt.ylabel  ("temp in C")
plt.legend()
plt.show()

############################################################################################
temp_train.info()
temp_train.head()

back_up = temp_train.copy()

#pd.get_dummies(temp_train['temp_c', 'timestep', 'month_name', 'trend'], prefix= '', prefix_sep= '')



temp_train = pd.get_dummies(temp_train, drop_first=True, prefix='', prefix_sep='')
temp_train.head()


##########################################################################################################
X = temp_train.drop(columns=['trend', 'temp_c', 'year', 'month'], axis=1)
y = temp_train['temp_c']
m_trend_s = LinearRegression()
m_trend_s.fit(X,y)
temp_train['trend_seasonal'] = m_trend_s.predict(X)
temp_train.head()
plot_timeseries(temp_train[['temp_c', 'trend', 'trend_seasonal']], title= "average month temp vs tend vs trend and seasonality")
##################################################################################################
temp_train['remainder'] = temp_train['temp_c'] - temp_train['trend_seasonal']
temp_train.head()
##########################################################################################
plt.hist(temp_train['remainder'], bins=20)
plt.show()
############################################################################
sns.histplot(temp_train['remainder'], kde=True )
plt.show()
#############################################################################
temp_train['remainder'].std(), temp_train['remainder'].mean()
###############################################################################
temp_train['random'] = np.random.normal(loc=0, scale=4, size=temp_train.shape[0])
###############################################################################
plot_timeseries(temp_train[['remainder', 'random']], ylim=False)
##############################################################################
fig, ax = plt.subplots()
ax.plot(temp_train.index, temp_train['remainder'], marker='o')
plt.show()
###############################################################################
remainder = temp_train[['remainder']].copy()
remainder.head()
remainder['lag1'] = remainder.shift(1)
remainder.head()
################################################################################
sns.scatterplot(x='remainder', y='lag1', data=remainder)
plt.show()
###############################################################################
remainder['remainder'].corr(remainder['lag1'])
################################################################################
sns.heatmap(round(remainder.corr(), 2), annot=True)
plt.show()
##############################################################################
sns.regplot(x = remainder['remainder'], y = remainder['lag1'], fit_reg=True, scatter=True )
plt.show()
#################################################################################
###################AR(1)
remainder.head()
remainder_copy = remainder.copy()
remainder.dropna(inplace=True)
remainder.head()
X = remainder[['lag1']]
y = remainder['remainder']
m_ar = LinearRegression()
m_ar.fit(X, y)
remainder['prediction_ar1'] = m_ar.predict(X)
remainder.head()
################################################################################
plot_timeseries(remainder[['remainder', 'prediction_ar1']], title= "Remainder(LR) vs AR1", ylim=False)
plt.show()
###############################################################################
remainder['residual'] = remainder['remainder'] - remainder['prediction_ar1']
plot_timeseries(remainder['residual'], title='Residual', ylim=False)
##########################################################################
plt.hist(remainder['residual'], bins=15)
remainder['residual'].mean()
##########################################################################
remainder_copy['lag2'] = remainder['lag1'].shift(1)
remainder_copy.head()
remainder_copy['remainder'].corr(remainder_copy['lag2'])
sns.scatterplot(x)