#%%
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import pandas as pd
import os

import src._utils as utils

#%% Reading data from data source
data = pd.read_csv(os.path.join('data','raw_data', 'bbc-text.csv'))



#%% Data Standarization
data.columns = ['label', 'text']


#%% Loading to MongoDB
utils.mgdb.write_mongo(data, 'raw_data')