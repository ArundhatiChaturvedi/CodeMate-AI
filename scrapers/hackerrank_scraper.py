import requests
from bs4 import BeautifulSoup

def fetch_hackerrank_data(username):
    headers = {"User-Agent": "CodeMateAI/1.0"}
    try:
        url = f"https://www.hackerrank.com/{username}"
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        badges = soup.find_all("div", class_="hacker-badge")
        if not badges:
            return {"error": "No badges found or private profile"}
            
        domains = [badge.text.strip() for badge in badges]
        return {"badges": domains}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except Exception as e:
        return {"error": f"Parsing error: {str(e)}"}