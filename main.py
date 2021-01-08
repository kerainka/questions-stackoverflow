import requests

from datetime import datetime, timedelta

today = datetime.now()
two_days_before = today - timedelta(2)

API_URL = "https://api.stackexchange.com/2.2/questions"
TAG = "Python"


response = requests.get(API_URL, params={"fromdate": int(two_days_before.timestamp()),
                                         "order": "desc",
                                         "sort": "activity",
                                         "tagged": TAG,
                                         "site": "stackoverflow"})
response.raise_for_status()
items = response.json()["items"]
for item in items:
    print(item["title"])