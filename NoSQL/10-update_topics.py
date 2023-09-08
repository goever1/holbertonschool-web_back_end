#!/usr/bin/env python3
""" It Write a Python function"""


def update_topics(mongo_collection, name, topics):
    """ It changes all topics of a school document based on the name """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
    