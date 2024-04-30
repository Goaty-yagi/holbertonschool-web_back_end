#!/usr/bin/env python3
"""
This module provides schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """
    Lists all documents in a collection:
    """
    query = {"topics": topic}
    result = mongo_collection.find(query)

    searched_list = list(result)
    return searched_list
