from bs4 import BeautifulSoup
import requests

def fetch_gfg_data(username):
    url = f"https://auth.geeksforgeeks.org/user/{username}/practice"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        solved = soup.find("div", class_="score_card_value").text.strip()
        return {"solved_problems": solved}
    except:
        return {"error": "Invalid GFG handle or layout issue"}