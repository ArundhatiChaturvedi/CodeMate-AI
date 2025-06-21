from bs4 import BeautifulSoup
import requests

def fetch_gfg_data(username):
    headers = {"User-Agent": "CodeMateAI/1.0"}
    try:
        url = f"https://auth.geeksforgeeks.org/user/{username}/practice"
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        solved = soup.find("div", class_="score_card_value")
        if not solved:
            return {"error": "Profile data not found"}
            
        return {"solved_problems": solved.text.strip()}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except Exception as e:
        return {"error": f"Parsing error: {str(e)}"}