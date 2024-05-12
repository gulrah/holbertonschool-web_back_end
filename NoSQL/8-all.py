#!/usr/bin/env python3
"""
A Python function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from the provided MongoDB collection.
    """
    result = mongo_collection.school.find()
    if result:
        return result
    return []
