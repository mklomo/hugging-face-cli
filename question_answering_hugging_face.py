from huggingface_hub.inference_api import InferenceApi
import os
from dotenv import load_dotenv
import gradio as gr



# Get Keys from .env file
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')



# Instantiate the Inference API
inference = InferenceApi(repo_id="deepset/xlm-roberta-base-squad2", token=API_TOKEN)


def process_question(question: str, context: str):
    """
        This function takes a question and context 
        and generates the answer to the question
    """
    # Get the Question and Context
    QA_input = {
    'question': question,
    'context': context
    }

    # Get the answer
    answer = inference(inputs=QA_input)
    
    return answer['answer']

# Build the interface
interface = gr.Interface(
            fn=process_question,
            inputs=['text', 'text'],
            outputs=['text']
                        )

# Launch the interface
interface.launch()