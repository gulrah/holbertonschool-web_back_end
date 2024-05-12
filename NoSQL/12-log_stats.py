#!/usr/bin/env python3
"""
Statistics
"""

def log_stats(mongo_collection):
    """
    Provides statistics about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
        print(f"{status_check_count} status check")
