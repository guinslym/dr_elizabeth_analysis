import datetime
from collections import Counter

import pymongo
import pandas as pd
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['test-database']

import pprint
pprint.PrettyPrinter(indent=4)


one_tweet = db.tweets.find_one({"user.id_str": "524901955"})
one_tweet2 = db.tweets.find_one({"user.id_str": "524901955"})
def number_of_documents():
    return db.tweets.count()