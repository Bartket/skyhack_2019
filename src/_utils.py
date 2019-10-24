from pymongo import MongoClient
import pandas as pd



class mongo_db:
    def __init__(self,db_name,**kwargs):
        """Class for dealing with mongodb instance

        Parameters
        ----------
        db_name : [str]
            Name of database
        **kwargs : kwargs
            Additional arguments for MongoClient
        """
        self.mongodb_instance = MongoClient(**kwargs)
        self.db=self.mongodb_instance.get_database(db_name)

    def write_mongo(self, df, collection_name):
        """Saving dataframe to MongoDB
        
        Parameters
        ----------
        df : [dataframe]
            Pandas dataframe to save
        collection_name : [str]
            Name of new collection for df
        
        Returns
        -------
        [str]
            Returns answer from monogdb instance
        """
        db_cm = self.db[collection_name]
        records_=df.to_dict(orient = 'records')
        results = db_cm.insert_many(records_)
        return results


    def read_mongo(self, collection, query={}, no_ID=True):
        """ Read from Mongo and Store into DataFrame """

        # Make a query to the specific DB and Collection
        cursor = self.db[collection].find(query)

        # Expand the cursor and construct the DataFrame
        df =  pd.DataFrame(list(cursor))

        if df.empty:
            raise Exception("Collection {} dosn't exists or it is empty".format(collection))

        if no_ID:
            df.drop(columns='_id', inplace=True)

        return df

mgdb = mongo_db('skyhack')