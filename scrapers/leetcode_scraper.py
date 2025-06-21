import requests

def fetch_leetcode_data(username):
    headers = {"User-Agent": "CodeMateAI/1.0"}
    try:
        url = f"https://leetcode-stats-api.herokuapp.com/{username}"
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        data = res.json()
        
        if data.get("status") == "error":
            return {"error": data.get("message", "User not found")}
            
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except ValueError as e:
        return {"error": f"Invalid JSON response: {str(e)}"}