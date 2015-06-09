# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 20:46:46 2015

@author: Home
"""

def run_queries():
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.milwaukee
    milwaukee = db.milwaukee
    
    #Unique users
    users = len(milwaukee.distinct("created.user"))
    print 'milwaukee.distinct("created.user").length'
    print 'number of unique users - {}\n'.format(users)
    
    #Users having more than one post
    users_over_one = db.milwaukee.aggregate([{"$group":{"_id":"$created.user","posts":{"$sum":1}}},{"$match":{"posts":{"$gt":1}}},\
                                            {"$group":{"_id":"users","count":{"$sum":1}}}])
    print 'db.milwaukee.aggregate([{"$group":{"_id":"$created.user","posts":{"$sum":1}}},{"$match":{"posts":{"$gt":1}}},'\
                                            '{"$group":{"_id":"users","count":{"$sum":1}}}])'
    for user in users_over_one:
        print '{} users have more than one entry'.format(user['count'])
    print ''
        
    #Top 10 most active users
    users = db.milwaukee.aggregate([{"$match":{"created.user":{"$exists":1}}},{"$group":{"_id":"$created.user","count":{"$sum":1}}}\
                           ,{"$sort":{"count":-1}},{"$limit":10}])
    print 'db.milwaukee.aggregate([{"$match":{"created.user":{"$exists":1}}},{"$group":{"_id":"$created.user","count":{"$sum":1}}}'\
                           ',{"$sort":{"count":-1}},{"$limit":10}])'
    for user in users:
        print '{0} made {1} updates'.format(user["_id"], user["count"])
    print ''
    
    #Top 5 store types
    stores = milwaukee.aggregate([{"$match":{"shop":{"$exists":1}}},{"$group":{"_id":"$shop","count":{"$sum":1}}},{"$sort":{"count":-1}},{"$limit":5}])
    print 'milwaukee.aggregate([{"$match":{"shop":{"$exists":1}}},{"$group":{"_id":"$shop","count":{"$sum":1}}},{"$sort":{"count":-1}},{"$limit":5}])'
    for el in stores:
        print '{0} {1} stores'.format(el["count"], el["_id"])
    print ''
    
    #Top 5 types of amenities
    amenities = db.milwaukee.aggregate([{"$match":{"amenity":{"$exists":1}}},\
                                        {"$group":{"_id":"$amenity","count":{"$sum":1}}},\
                                        {"$sort":{"count":-1}},{"$limit":5}])
    print 'db.milwaukee.aggregate([{"$match":{"amenity":{"$exists":1}}}, {"$group":{"_id":"$amenity","count":{"$sum":1}}},{"$sort"'\
            ':{"count":-1}},{"$limit":5}])'
    for amenity in amenities:
        print '{0} {1}'.format(amenity['count'],amenity['_id'])
    print ''
    
if __name__ == "__main__":
    run_queries()