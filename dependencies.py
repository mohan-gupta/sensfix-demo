# dependencies.py

from fastapi import FastAPI
from langchain import OpenAI, LLMChain
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

openai_key1 = os.getenv("OPENAI_API_KEY_1")
openai_key2 = os.getenv("OPENAI_API_KEY_2")
openai_key3 = os.getenv("OPENAI_API_KEY_3")

llm1 = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_key1, temperature=1)
llm2 = OpenAI(model_name="gpt-3.5-turbo-0301", openai_api_key=openai_key2, temperature=1)
llm3 = OpenAI(model_name="gpt-3.5-turbo-0613", openai_api_key=openai_key3, temperature=1)

# Import get_first_classification_prompt and get_second_classification_prompt
from first_classification_prompt import get_first_classification_prompt
from second_classification_prompt import get_second_classification_prompt

# Import PromptTemplates from separate files
from response_templates import response_prompt
from ticket_templates import ticket_prompt
from validation_templates import validation_prompt

# LLMChains
ticket_chain = LLMChain(llm=llm1, prompt=ticket_prompt)
response_chain = LLMChain(llm=llm2, prompt=response_prompt) 
validation_chain = LLMChain(llm=llm3, prompt=validation_prompt)
