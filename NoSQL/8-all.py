#!/usr/bin/env python3
"""
A Python function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from the provided MongoDB collection.
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
