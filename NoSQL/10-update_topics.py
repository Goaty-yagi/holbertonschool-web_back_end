#!/usr/bin/env python3
"""
This module provides update_topics function.
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    query = {'name': name}
    new_values = {'$set': {'topics': topics}}
    result = mongo_collection.update_one(query, new_values)
