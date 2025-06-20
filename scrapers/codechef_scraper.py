import requests
from bs4 import BeautifulSoup

def fetch_codechef_data(username):
    url = f"https://www.codechef.com/users/{username}"
    res = requests.get(url)
    if res.status_code != 200:
        return {"error": "Invalid handle or network error"}
    
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        rating_tag = soup.find("div", class_="rating-number")
        stars_tag = soup.find("span", class_="rating-star")
        fully_solved_tag = soup.find_all("section", class_="rating-data-section problems-solved")[0]
        
        rating = rating_tag.text.strip()
        stars = stars_tag.text.strip()
        solved = fully_solved_tag.find_all("h5")[0].text.strip()
        
        return {
            "rating": rating,
            "stars": stars,
            "problems_solved": solved
        }
    except:
        return {"error": "Parsing error – layout may have changed"}
