import requests

API_KEY = 'AIzaSyCEl8I3lOftyn966djQicsEXUBQuGKs0Vs'
CSE_ID = '73c8fbdb27a1442b0'

def recommend_resources(skill):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": CSE_ID,
        "q": f"online courses for {skill}"
    }

    response = requests.get(url, params=params)
    data = response.json()

    for item in data.get("items", []):
        print(item["title"])
        print(item["link"])
        print()
