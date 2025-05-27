import requests
import pandas as pd

def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v4/launches/query"
    query = {}
    options = {"populate": ["payloads", "rocket"], "pagination": False}
    payload = {"query": query, "options": options}
    
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    
    launches = data['docs']
    df = pd.json_normalize(launches, max_level=2)
    
    return df