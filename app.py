import gradio as gr
import chatgpt

block = gr.Blocks()

chatgpt_obj = chatgpt.ChatGPT()

with block:
    gr.Markdown("""<h1><center>🤖 ChatGPT-Assistant 🐍</center></h1>
                   <p><center>ChatGPT-Assistant is a chatbot that uses the gpt-3.5-turbo model</center></p>
    """) 
    chatbot = gr.Chatbot()
    message = gr.Textbox(label="Message", placeholder="Hi, how are things?")
    submit = gr.Button("Send")
    message.submit(chatgpt_obj.update, [message, chatbot], [message, chatbot])
    
    submit.click(chatgpt_obj.update, [message, chatbot], [message, chatbot])

    clear = gr.Button("Clear")
    clear.click(chatgpt_obj.clear, None, chatbot, queue=False)

    gr.Examples(
        examples=["Write a poem about artificial intelligence",
                  "What could the future be like?",
                  "If x+1=20, what is the value of x?",
                  "Write a story that gives a message",
                  "What programming language is the most used in the industry?",
                  "How can I be more productive?",
                  "Create me a training schedule to train from home",
                  "Sums up everything we've talked about",
                  "What is the Apple stock price now?"],
        inputs=message
    )

block.launch(debug=True)