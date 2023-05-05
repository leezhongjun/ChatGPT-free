# ChatGPT (gpt-3.5-turbo) with web access and web UI for free

## What is this
This is a web interface for ChatGPT that provides it with web access with simple commands for searching the web (with DuckDuckGo) and scraping websites (with BeautifulSoup4). 

## How to use
1. Install the requirements with `pip install -r requirements.txt`
2. Create `.env` file with the following content:
```
OPENAI_API_KEY=<your openai api key>
OPENAI_API_BASE=<https://api.openai.com/v1 - use official OR use your own reverse proxy>
```

### To do
- [ ] Add more commands
- [ ] Add streaming 
- [ ] Add option to show/hide commands and command responses