# import openai

import os
import json
import openai
from dotenv import load_dotenv



# Set the API key in env variable
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI API
openai.api_key = api_key



def callChatCompletion(messages,email):
    messages.append({"role": "user", "content": email})
    response = openai.chat.completions.create(
                                        model="gpt-4o",
                                        messages = messages,
                                        temperature=0
                        
    )
    return response.choices[0].message.content



 
