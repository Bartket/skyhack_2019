#%%
import pandas as pd
from pymongo import MongoClient

import src._utils as uts
#%%
client = MongoClient('localhost')
db=client.admin

#%% Load


#%% Filter tha data
# PASS

#%% Split dataset to train and test

#%% Save split into mongo