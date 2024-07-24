#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of documents that contain the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
