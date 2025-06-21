import requests

def fetch_leetcode_data(username):
    headers = {"User-Agent": "CodeMateAI/1.0"}
    try:
        url = f"https://leetcode-stats-api.herokuapp.com/{username}"
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()
        data = res.json()
        
        if data.get("status") == "error":
            return {"error": data.get("message", "User not found")}
            
        return data
    except requests.exceptions.Timeout:
        print("Request timed out, retrying...")
        return fetch_leetcode_data(username)
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Error fetching Leetcode data: {e}")
        return {}