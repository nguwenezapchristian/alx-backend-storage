#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """ Lists all elements in a collection """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
