import requests
from bs4 import BeautifulSoup

def fetch_atcoder_data(username):
    headers = {"User-Agent": "CodeMateAI/1.0"}
    try:
        url = f"https://atcoder.jp/users/{username}"
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        tables = soup.find_all("table")
        if len(tables) < 2:
            return {"error": "Profile data not found"}
            
        stats_table = tables[1]
        tds = stats_table.find_all("td")
        if len(tds) < 3:
            return {"error": "Incomplete profile data"}
            
        return {
            "rating": tds[1].text.strip(),
            "highest_rating": tds[2].text.strip()
        }
    except requests.exceptions.Timeout:
        print("Request timed out, retrying...")
        return fetch_atcoder_data(username)
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Error fetching AtCoder data: {e}")
        return {}
