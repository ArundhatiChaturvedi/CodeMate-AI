import requests
from bs4 import BeautifulSoup

def fetch_atcoder_data(username):
    url = f"https://atcoder.jp/users/{username}"
    res = requests.get(url)
    if res.status_code != 200:
        return {"error": "Invalid handle or network error"}
    
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        tables = soup.find_all("table")
        stats_table = tables[1]  # User rating table
        rating = stats_table.find_all("td")[1].text.strip()
        highest = stats_table.find_all("td")[2].text.strip()
        
        return {
            "rating": rating,
            "highest_rating": highest
        }
    except:
        return {"error": "Parsing error – layout may have changed"}
