#!/usr/bin/env python3
""" It is a phython scrypt"""


def schools_by_topic(mongo_collection, topic):
    """ It returns the list of school having a specific topic """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [i for i in documents]
    return list_docs
