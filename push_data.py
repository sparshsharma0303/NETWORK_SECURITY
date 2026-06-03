import os
from dotenv import load_dotenv
import json
import sys
import pymongo 
load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL')
print(MONGODB_URL) 

import certifi
ca = certifi.where()

import numpy as np
import pandas as pd
from networksecurity.exception.exception import NetworkSecuriyException
from networksecurity.logging.logger import logging

class NetworkData_Extract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecuriyException(e,sys)

    def csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict(orient='records')
            return records
        except Exception as e:
            raise NetworkSecuriyException(e, sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGODB_URL,
                                                    tlsCAFile=certifi.where()
                                                    )
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecuriyException(e,sys)

if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = 'SPARSHS'
    Collection = 'NetworkData'
    networkobj = NetworkData_Extract()
    records = networkobj.csv_to_json(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)