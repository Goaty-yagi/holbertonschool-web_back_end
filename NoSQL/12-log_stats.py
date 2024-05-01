#!/usr/bin/env python3
"""
This module provides get_nginx_stats function
"""

from pymongo import MongoClient

def get_nginx_stats():
    """
    Prints DB logs:
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx
    
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    specific_logs_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{specific_logs_count} status check")

if __name__ == "__main__":
    get_nginx_stats()
