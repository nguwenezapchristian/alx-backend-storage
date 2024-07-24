#!/usr/bin/env python3
""" 12-log_stats """

from pymongo import MongoClient


def print_log_stats():
    """ Prints statistics about Nginx logs from MongoDB """
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})

    # Methods counts
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in methods}

    # Logs with method=GET and path=/status
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Print results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    print_log_stats()
