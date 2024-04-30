#!/usr/bin/env python3
"""
This module provides
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection:
    """
    documents = mongo_collection.find()

    # Convert the cursor to a list of dictionaries
    document_list = list(documents)
    return document_list
