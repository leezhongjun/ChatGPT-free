import requests, json, config
from duckduckgo_search import ddg
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

def search(query):
    r = ddg(query, max_results=config.max_search_results)
    return json.dumps(r, indent=4)

def scrape_text(url: str) -> str:
    """Scrape text from a webpage

    Args:
        url (str): The URL to scrape text from

    Returns:
        str: The scraped text
    """
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        error_message = f"Error: Could not scrape text from {url} because of {e}"
        return error_message
        
    if not response:
        return "Error: Could not get response"

    soup = BeautifulSoup(response.text, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = "\n".join(chunk for chunk in chunks if chunk)

    return text