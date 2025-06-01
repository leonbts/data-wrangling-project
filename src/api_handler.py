import requests
import pandas as pd

def fetch_spacex_launches():
    """
    Fetch SpaceX launch data from the SpaceX v4 API.
    Returns a pandas DataFrame with launch details, including payload and rocket info.
    """
    url = "https://api.spacexdata.com/v4/launches/query"
    
    query = {}
    options = {
        "populate": ["payloads", "rocket"],
        "pagination": False
    }
    payload = {
        "query": query,
        "options": options
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    
    launches = data['docs']
    df_launches = pd.json_normalize(launches, max_level=2)
    return df_launches


def fetch_spacex_launchpads():
    url = "https://api.spacexdata.com/v4/launchpads"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    df_launchpads = pd.DataFrame(data)[['id', 'name', 'region']]
    return df_launchpads