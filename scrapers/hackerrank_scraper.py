import requests
from bs4 import BeautifulSoup

def fetch_hackerrank_data(username):
    headers = {"User-Agent": "CodeMateAI/1.0"}
    try:
        url = f"https://www.hackerrank.com/{username}"
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        badges = soup.find_all("div", class_="hacker-badge")
        if not badges:
            return {"error": "No badges found or private profile"}
            
        domains = [badge.text.strip() for badge in badges]
        return {"badges": domains}
    except requests.exceptions.Timeout:
        print("Request timed out, retrying...")
        return fetch_hackerrank_data(username)
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Error fetching Hackerrank data: {e}")
        return {}