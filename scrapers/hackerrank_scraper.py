import requests
from bs4 import BeautifulSoup

def fetch_hackerrank_data(username):
    url = f"https://www.hackerrank.com/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return {"error": "Invalid handle or profile inaccessible"}
    
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        badges = soup.find_all("div", class_="hacker-badge")
        domains = [badge.text.strip() for badge in badges]
        return {
            "badges": domains if domains else "No badges found"
        }
    except:
        return {"error": "Could not extract data – layout issue or private profile"}
