from transformers import pipeline
import wikipedia
import gradio as gr



# mute tensorflow complaints
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"


# A function that returns a page from wikipedia
def get_page(text):
    try:
        page_object = wikipedia.page(text)
        
    except wikipedia.page.exceptions.PageError:
        return 'Page Not Found'
    
    except wikipedia.exceptions.DisambiguationError:
        return 'Ambiguous Search'
    
    # Catch all
    except Exception as e:
        return 'Wrong Search'
    
    else:
        return page_object.content



# Load the Hugging Face Model
model = pipeline("summarization")


def process(text):
    summarizer = pipeline("summarization", model="t5-small")
    result = summarizer(text, max_length=180)
    return result[0]["summary_text"]


# Using gradio to create a web interface to return a summary
iface = gr.Interface(fn=process, inputs=gr.Textbox(lines = 3, placeholder="Enter Wikipedia page ... E.g. House of the Dragons"), outputs='text')



if __name__ == '__main__':
    iface.launch()