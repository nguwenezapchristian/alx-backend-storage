#!/usr/bin/env python3
""" 102-log_stats """

from pymongo import MongoClient


def print_log_stats():
    """ Prints statistics about Nginx logs from MongoDB with top IPs """
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

    # Top 10 IPs
    ip_counts = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    # Print results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")
    print("IPs:")
    for ip in ip_counts:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    print_log_stats()
