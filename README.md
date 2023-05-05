# ChatGPT (gpt-3.5-turbo) with web access and web UI for free
Currently live at [huggingface.co/spaces/leezhongjun/chatgpt-free](https://huggingface.co/spaces/leezhongjun/chatgpt-free)

This is a web interface for ChatGPT that provides it with web access with simple commands for searching the web (with DuckDuckGo) and scraping websites (with BeautifulSoup4). 

This uses the free reverse proxy provided by [PawanOsman/ChatGPT](https://github.com/PawanOsman/ChatGPT)

---

### Demo: Latest news as of 5 May 2023
![screencapture-127-0-0-1-7860-2023-05-05-21_06_17](https://user-images.githubusercontent.com/80515759/236465580-410778a9-976a-4fba-a763-78f073c1e423.png)

---

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