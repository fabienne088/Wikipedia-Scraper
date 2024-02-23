# You should have a working main.py script that calls the API and creates a JSON file
"""Bundle everything together in a main.py file that 
calls the WikipediaScraper object 
and saves the data into a JSON file.

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

WikipediaScraper.get_countries
WikipediaScraper.refresh_cookie
WikipediaScraper.get_leaders
WikipediaScraper.get_first_paragraph
WikipediaScraper.to_json_file



