"""Code up a WikipediaScraper scraper object that allows you to structurally retrieve data from the API.

The object should contain at least these six attributes:

base_url: str containing the base url of the API (https://country-leaders.onrender.com)
country_endpoint: str → /countries endpoint to get the list of supported countries
leaders_endpoint: str → /leaders endpoint to get the list of leaders for a specific country
cookies_endpoint: str → /cookie endpoint to get a valid cookie to query the API
leaders_data: dict is a dictionary where you store the data you retrieve before saving it into the JSON file
cookie: object is the cookie object used for the API calls
The object should contain at least these five methods:

refresh_cookie() -> object returns a new cookie if the cookie has expired
get_countries() -> list returns a list of the supported countries from the API
get_leaders(country: str) -> None populates the leader_data object with the leaders of a country retrieved from the API
get_first_paragraph(wikipedia_url: str) -> str returns the first paragraph (defined by the HTML tag <p>) with details about the leader
to_json_file(filepath: str) -> None stores the data structure into a JSON file
"""