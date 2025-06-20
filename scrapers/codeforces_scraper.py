import requests

def fetch_codeforces_data(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    res = requests.get(url)
    if res.status_code != 200:
        return {"error": "Invalid handle or network error"}
    user_info = res.json()['result'][0]
    return {
        "rating": user_info.get("rating", "N/A"),
        "maxRating": user_info.get("maxRating", "N/A"),
        "rank": user_info.get("rank", "N/A")
    }