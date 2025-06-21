import requests

def fetch_codeforces_data(handle):
    headers = {"User-Agent": "CodeMateAI/1.0"}
    try:
        url = f"https://codeforces.com/api/user.info?handles={handle}"
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()  # Raises HTTPError for bad responses
        data = res.json()
        
        if not data.get("result"):
            return {"error": "User not found"}
            
        user_info = data["result"][0]
        return {
            "rating": user_info.get("rating", "N/A"),
            "maxRating": user_info.get("maxRating", "N/A"),
            "rank": user_info.get("rank", "N/A")
        }
    except requests.exceptions.Timeout:
        print("Request timed out, retrying...")
        return fetch_codeforces_data(username)
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Error fetching Codeforces data: {e}")
        return {}