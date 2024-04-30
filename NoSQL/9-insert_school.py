#!/usr/bin/env python3
"""
This module provides insert_school function.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Lists all documents in a collection:
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
