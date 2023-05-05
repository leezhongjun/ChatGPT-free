import openai, json, os, web, config
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = os.getenv('OPENAI_API_BASE')

def summarise_url(url, qn):
  text = web.scrape_text(url)

  max_len = config.max_len
  res = []
  segements = max(len(text) // max_len, 1)
  max_tokens = min(config.upper_token_limit - max_len, config.upper_token_limit // segements)

  while len(text) > 0:
      if len(text) < max_len:
          t = text
          text = ''
      else:
          t = text[:max_len]
          text = text[max_len:]

      prompt = f'''
      {t}
      
      Using the above text, answer the following question: "{qn}" -- if the question cannot be answered using the text: "summarise the text" '''
      response = openai.Completion.create(
          model="text-davinci-003",
          prompt=prompt,
          temperature=0.7,
          max_tokens=max_tokens,
          n=1,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
      )
      
      res.append(response.choices[0].text.strip())

  return str(res)


class ChatGPT:
  def __init__(self) -> None:
    self.messages = [{"role": "system", "content": config.system_prompt}]
    self.qn = ''
    self.history = []

  def update(self, message, history, is_user=True):
    if is_user:
      self.qn = message

    self.messages.append(dict(role='user', content=message))

    res = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=self.messages,
      max_tokens=config.max_chat_tokens,
    )
    
    self.messages.append(dict(res['choices'][0]['message']))
    history.append((message, self.messages[-1]['content']))

    if 'SEARCH ' in history[-1][1]:
      message = 'RES: ' + web.search(history[-1][1].replace('SEARCH ', ''))
      self.update(message, history, is_user=False)
    
    elif 'SCRAPE ' in history[-1][1]:
      message = 'RES: ' + summarise_url(history[-1][1].replace('SCRAPE ', ''), self.qn)
      self.update(message, history, is_user=False)

    return '', history
    

  def user(self, message, history, is_user=True):

    history += [[message, None]]
    self.history = history
    self.update(history)

    return "", history


  def bot(self, history):
      self.send_message(history[-1][0])
      bot_message = self.messages[-1]['content']
      history[-1][1] = ""
      for character in bot_message:
          history[-1][1] += character
          yield history


  def clear(self):
    self.messages = [{"role": "system", "content": config.system_prompt}]
    self.qn = ''
    return None
