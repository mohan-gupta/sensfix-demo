#main.py
from fastapi import FastAPI
import asyncio
from langchain import LLMChain
from dependencies import (app, llm1, llm2, llm3, response_chain, validation_chain, ticket_chain)
from ticket_templates import ticket_prompt
from validation_templates import validation_prompt
from response_templates import response_prompt

from first_classification_prompt import get_first_classification_prompt
from second_classification_prompt import get_second_classification_prompt

@app.get("/ticket_qualification")
async def categorize_and_respond(user_input: str):
    # Validation
    validation_result = validation_chain.run(user_input)

    if validation_result == "output:Incomplete":
        return {"status": "incomplete"}

    # First classification
    first_classification_prompt = get_first_classification_prompt()
    first_category_chain = LLMChain(llm=llm2, prompt=first_classification_prompt)
    first_category = await asyncio.to_thread(first_category_chain.run, user_input)

    # Second classification
    second_classification_prompt = get_second_classification_prompt()
    second_category_chain = LLMChain(llm=llm3, prompt=second_classification_prompt)
    second_category = await asyncio.to_thread(second_category_chain.run, user_input=first_category)

    # Ticket generation
    ticket_chain = LLMChain(llm=llm1, prompt=ticket_prompt)
    ticket_result = await asyncio.to_thread(ticket_chain.run, user_input)

    # Response generation
    response_chain = LLMChain(llm=llm2, prompt=response_prompt)
    response = await asyncio.to_thread(response_chain.run, user_input=user_input)

    return {
        "ticket_status": ticket_result,
        "category": second_category,
        "response": response
    }
