import gradio as gr
import chatgpt

block = gr.Blocks()

chatgpt_obj = chatgpt.ChatGPT()

def update(name):
    return f"Welcome to Gradio, {name}!"

with block:
    gr.Markdown("""<h1><center>🤖 ChatGPT-free 🐍</center></h1>
                   <p><center>ChatGPT-free has web access and uses the gpt-3.5-turbo model</center></p>
                   <p><center>View <a href="https://github.com/leezhongjun/ChatGPT-free">source on GitHub</a></center></p>""") 
    if chatgpt_obj.show_commands:
        show_commands_txt = gr.Markdown(f"""<p><center>Commands and command responses are <b>shown</b></center></p>""")
        btn_text = "Hide commands and command responses"
    else:
        show_commands_txt = gr.Markdown(f"""<p><center>Commands and command responses are <b>hidden</b></center></p>""")
        btn_text = "Show commands and command responses"

    chatbot = gr.Chatbot()
    message = gr.Textbox(label="Message", placeholder="Hi, how are things?")
    submit = gr.Button("Send")
    message.submit(chatgpt_obj.update, [message, chatbot], [message, chatbot])
    
    submit.click(chatgpt_obj.update, [message, chatbot], [message, chatbot])

    clear = gr.Button("Clear")
    clear.click(chatgpt_obj.clear, None, chatbot, queue=False)

    toggle_commands = gr.Button(btn_text)
    toggle_commands.click(chatgpt_obj.toggle_commands, chatbot, [chatbot, show_commands_txt, toggle_commands], queue=False)

    gr.Examples(
        examples=["What is the Apple stock price now?",
                  "Who is the CEO of Apple now?",
                  "Write a poem about artificial intelligence",
                  "What could the future be like?",
                  "If x+1=20, what is the value of x?",
                  "Write a story that gives a message",
                  "What programming language is the most used in the industry?",
                  "How can I be more productive?",
                  "Create me a training schedule to train from home",
                  "Sums up everything we've talked about",
                  ],
        inputs=message
    )

block.launch(debug=True)