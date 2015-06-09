# -*- coding: utf-8 -*-

from pymongo import MongoClient
import json

def get_db(database, data):
    client = MongoClient('localhost:27017') #get client
    db = client[database] #build database
    for item in data:  
        db.milwaukee.insert(item)  #insert data
    return db

def load_data(filename):
     data = []
     with open(filename) as f:
        for line in f:
            while True:
                try:
                    jfile = json.loads(line.encode("utf-8"))
                    break
                except ValueError:
                    line += next(f)
            data.append(jfile)
     print "Load data successfully"
     return data
     
def insert_data():
    data = load_data("milwaukee_wisconsin.osm.json")
    get_db("milwaukee", data)
    print "Insert data to database completed"
    
if __name__ =="__main__":
    insert_data()
