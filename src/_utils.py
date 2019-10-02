from pymongo import MongoClient
import pandas as pd

class md_utils:
    def __init__(self,db_name,**kwargs):
        self.mongodb_instance = MongoClient(**kwargs)
        self.db=self.mongodb_instance.db_name

    def export_mongodb(self, df, collection_name):
        db_cm = self.mongodb_instance[collection_name]
        records_=df.to_dict(orient = 'records')
        results = db_cm.insert_many(records_)
        return results

    def import_mongodb_coll(self, collection_name):
        #select the collection within the database
        test = self.db.test
        #convert entire collection to Pandas dataframe
        test = pd.DataFrame(list(test.find()))