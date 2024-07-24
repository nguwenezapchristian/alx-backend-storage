#!/usr/bin/env python3
""" 10-update_topics """


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.
        name (str): The name of the school.
        topics (list): The new list of topics.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
