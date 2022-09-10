import os
import gradio as gr
from dotenv import load_dotenv

# # Load the .env file
# load_dotenv()

# API_TOKEN = os.getenv('API_TOKEN')




iface = gr.Interface.load("huggingface/Helsinki-NLP/opus-mt-en-es",
  examples=[["Hello! My name is Marvin"]]
)

iface.launch()