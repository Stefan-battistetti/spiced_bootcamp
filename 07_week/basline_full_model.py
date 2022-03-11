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
###################################reading data##############################################
temp_train = pd.read_csv('/home/damoon/damoon_spiced_academy/07_week/escad_data/temp_train.csv', parse_dates=True, index_col='date')
temp_train.drop(columns=['temp'], axis=1, inplace=True)
temp_train.rename(columns={'temp_c':'temp'},  inplace=True)
#####################################plot functions##################################
def plot_timeseries (df, title=" ", ylim=True):
    df.plot()
    plt.title(title)
    if ylim:
        plt.ylim(ymin=0)
    plt.ylabel("Temperature in C")
    plt.show()
##############################################################################
temp_train['timestep'] = list(range(len(temp_train)))
temp_train['month'] = temp_train.index.month_name()
temp_train = pd.get_dummies(temp_train, drop_first=True, prefix='', prefix_sep='')
#######################################################
X = temp_train.drop(columns=['temp'], axis=1)
y = temp_train['temp']
m_trend_s = LinearRegression()




