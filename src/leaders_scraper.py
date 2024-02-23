import requests
from bs4 import BeautifulSoup
import re
import json

class WikipediaScraper:
# the object has 6 attributes
    def __init__(self):    
        self.base_url = "https://country-leaders.onrender.com"  # the base url of the API 
        self.country_endpoint = "https://country-leaders.onrender.com/countries"    # list of supported countries
        self.leaders_endpoint = "https://country-leaders.onrender.com/leaders"  # list of leaders for a specific country
        self.cookies_endpoint = "https://country-leaders.onrender.com/cookie"   # valid cookie to query the API
        self.leaders_data = {}      # to store the data before saving it into the JSON file
        self.cookie = requests.get(self.cookies_endpoint).cookies.get_dict()    # cookie object used for the API calls

    def refresh_cookie(self): # object returns a new cookie if the cookie has expired
        req_cookie = requests.get(self.cookies_endpoint)
        cookie = req_cookie.cookies.get_dict()
        return cookie

    def get_countries(self): # list returns a list of the supported countries from the API
        # Query the "/countries" endpoint
        req_countries = requests.get(self.country_endpoint, cookies=self.cookie)
        countries = req_countries.json()
        return countries

    def get_leaders(self, country: str): # None, populates the leader_data object with the leaders of a country retrieved from the API
        # loop over the countries
        leaders_per_country = {}

        for country in countries:

            params= {"country" : country}
            req_leaders = requests.get(self.leaders_endpoint, params=params, cookies=self.cookie)
            leaders = req_leaders.json()
        
            leaders_per_country[country] = leaders
        
        return leaders_per_country

    def get_first_paragraph(wikipedia_url: str, get_leaders): # str returns the first paragraph (defined by the HTML tag <p>) with details about the leader 

        req_wikipedia = requests.get(wikipedia_url)
        content = req_wikipedia.content
        soup = BeautifulSoup(content, "html.parser")
    
        all_paragraphs = soup.find_all("p", attrs={"class": None}) # find "p" without class attributes

        first_paragraph = " "

        for paragraph in all_paragraphs: 
            if len(paragraph) < 18: # find paragraph that is long enough
                pass    # do nothing
            else:
                break   # exit the loop

        first_paragraph = first_paragraph + (paragraph.text) # store text inside variable

        reg_par1 = re.sub(r"\s\[[^\]]*\]\[[^\]]*\]\s*", " ", first_paragraph)
        reg_par2 = re.sub(r"\bÉcouter\b\s*|\n","", reg_par1)
            
        return(reg_par2)

    get_first_paragraph(get_leaders())
    
    def to_json_file(filepath: str, leaders_per_country): # None, stores the data structure into a JSON file
        
        with open("./leaders.json", "w") as outfile: 
            json.dump(leaders_per_country, outfile, indent=2)