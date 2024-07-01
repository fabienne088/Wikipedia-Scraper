# You should have a working main.py script that calls the API and creates a JSON file
"""Bundle everything together

Create a scraper that builds a JSON file with the political leaders
 of each country you get from 
 [this API](https://country-leaders.onrender.com/docs).

Include in this file the first paragraph of the 
Wikipedia page of these leaders 
(you'll retrieve the Wikipedia page URL from the API,
 which you then have to scrape yourself).

"""

from src.leaders_scraper import WikipediaScraper
import json

#Call the WikipediaScraper object
scraper = WikipediaScraper()

refresh_cookie = scraper.refresh_cookie()
print(refresh_cookie)

countries = scraper.get_countries(refresh_cookie)
print(countries)

leaders = scraper.get_leaders(countries)
print(leaders)

for leader in leaders:
    url = leader.get("wikipedia_url")
    print(url)

first_paragraph = scraper.get_first_paragraph(url)
print(first_paragraph)

for leader in leaders:
    leader['first_paragraph'] = first_paragraph(leader["wikipedia_url"])



    


    
        
        


#  Save the data into a JSON file 
#scraper.to_json_file(".\.json")







