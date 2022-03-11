import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
'''
elements = pd.read_csv('elements.txt', delimiter= ',', on_bad_lines='skip')
metadata = pd.read_csv('metadata.txt', delimiter= ',',  on_bad_lines='skip')
sources = pd.read_csv('sources.txt', delimiter= ',',  on_bad_lines='skip')
stations = pd.read_csv('stations.txt', delimiter= ',',  on_bad_lines='skip')
'''
raw_data = pd.read_csv('/home/damoon/damoon_spiced_academy/07_week/escad_data/TG_STAID002759.txt', delimiter= ',', skiprows=19)
raw_data.head()



raw_data.info

raw_data
#my_command:
#raw_data.rename(columns={'ID':'id', '    DATE':'Date', '   TG':'Temp', ' Q_TG':'Quality'}, inplace=True)
#Diinas command:
raw_data.columns = ['id', 'date', 'temp', 'quality']

#raw_data['id'].unique()
#raw_data['id'].value_counts()
#raw_data['quality'].value_counts()
raw_data.drop(['id', 'quality'], axis=1, inplace=True)
#raw_data.info()

raw_data['date'] = raw_data['date'].astype(str)
raw_data['date'] = pd.to_datetime(raw_data['date'])

#raw_data.head()
#raw_data.info()

data = raw_data.set_index('date')
#data.head()



#data_subset = data.loc['1980':'1982']
#data_subset.head()
#data_subset.info()

data['temp_c'] = data['temp'] * 0.1
#data['temp_c'].plot()

##############################divide to train and test#################################

data_train = data.loc[:'2019']
data_train.info()
data_train.tail()

data_test = data.loc['2020']
data_test.info()
data_test.tail()

data_train.to_csv("temp_train")
data_test.to_csv("temp_test")

#############################################visualisation#############################
data_query = data.loc['1985':'1986']
data_query['temp_c'].plot()

###########################################
data['timestep'] = list(range(len(data)))
X = data[['timestep']]
y = data['temp_c']
model = LinearRegression()
model.fit(X, y)
########################################################################
sns.lineplot(x = data.index, y =data['temp_c'])
sns.lineplot(x = data.index, y=model.predict(X), label = 'trend prediction')
#################################################################
seasonal_dummies = pd.get_dummies(data.index.day, prefix='day', drop_first=True).set_index(data.index)
#seasonal_dummies = pd.get_dummies(data.index.month, prefix='month', drop_first=True).set_index(data.index)
#seasonal_dummies = pd.get_dummies(data.index.week, prefix='week', drop_first=True).set_index(data.index)
data_model = data.join(seasonal_dummies)
################################################################################
X = data_model.drop(columns=['temp', 'temp_c'])
y = data_model['temp_c']
model_new = LinearRegression()
model_new.fit(X, y)
################################################################################
sns.lineplot(x = data_model.index, y =data_model['temp_c'])
sns.lineplot(x = data_model.index, y=model_new.predict(X), label = 'trend prediction')
#######################################################################################
data_model['trend_seasonal'] = model_new.predict(X)
data_model['remainder'] = data_model['temp_c'] - data_model['trend_seasonal']
sns.lineplot(x=data_model.index, y=data_model['remainder'])
####################################################################################