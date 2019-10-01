#%%
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import pandas as pd
import os


#%%
client = MongoClient('localhost')
db=client.admin

# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)


#%% Reading data from data source
data = pd.read_csv(os.path.join('data','raw_data', 'bbc-text.csv'))



#%% Data Standarization
data.columns = ['labels', 'text']


#%% Loading to MongoDB
def export_mongodb(df, collection_name, mongodb_instance):
    db_cm = mongodb_instance[collection_name]
    records_=df.to_dict(orient = 'records')
    results = db_cm.insert_many(records_)
    return results

export_mongodb(data, 'sky_hack_data', db)