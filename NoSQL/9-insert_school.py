#!/usr/bin/env python3
"""It inserts a documetn"""


def insert_school(mongo_collection, **kwargs):
    """ It insert a school with features """
    document_id = mongo_collection.insert(kwargs)
    return document_id
