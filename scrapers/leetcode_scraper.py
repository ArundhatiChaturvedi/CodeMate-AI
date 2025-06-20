import requests

def fetch_leetcode_data(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "User not found or API limit reached."}