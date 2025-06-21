import requests
from bs4 import BeautifulSoup

def fetch_codechef_data(username):
    headers = {"User-Agent": "CodeMateAI/1.0"}
    try:
        url = f"https://www.codechef.com/users/{username}"
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        rating_tag = soup.find("div", class_="rating-number")
        stars_tag = soup.find("span", class_="rating-star")
        solved_section = soup.find("section", class_="rating-data-section problems-solved")
        
        if not all([rating_tag, stars_tag, solved_section]):
            return {"error": "Profile data not found"}
        
        solved = solved_section.find("h5").text if solved_section else "0"
        return {
            "rating": rating_tag.text.strip(),
            "stars": stars_tag.text.strip(),
            "problems_solved": solved.replace("Fully Solved (", "").replace(")", "")
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except Exception as e:
        return {"error": f"Parsing error: {str(e)}"}