import requests

def recommend_resources():
    skill = input("Enter your skill (e.g., python, data science, web development): ").strip().lower()
    
    api_key = 'api-key-'  # Replace with your API key
    cx = 'id'  # Replace with your Custom Search Engine ID
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {'key': api_key, 'cx': cx, 'q': f"online courses {skill}"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()

        print("\nRecommended resources:")
        for item in results.get('items', []):
            print(f"{item['title']} - {item['link']}")
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching resources: {e}")

# Run the function
recommend_resources()
