# ChatGPT (gpt-3.5-turbo) with web access and web UI for free
Currently live at [huggingface.co/spaces/leezhongjun/chatgpt-free](https://huggingface.co/spaces/leezhongjun/chatgpt-free)

## What is this
This is a web interface for ChatGPT that provides it with web access with simple commands for searching the web (with DuckDuckGo) and scraping websites (with BeautifulSoup4). 
This uses the free reverse proxy provided by [PawanOsman/ChatGPT](https://github.com/PawanOsman/ChatGPT)

## How to use
1. Install the requirements with `pip install -r requirements.txt`
2. Create `.env` file with the following content:
```
OPENAI_API_KEY=<your openai api key>
OPENAI_API_BASE=<http://my-reverse-proxy/v1>
```

### To do
- [ ] Add more commands
- [ ] Add streaming
- [x] Add option to show/hide commands and command responses