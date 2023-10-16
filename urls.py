from fastapi import APIRouter

from langchain import LLMChain

from dependencies import llm1, llm2, llm3

from prompts import (
    validation_prompt,
    category_l1_prompt,
    category_l2_prompt,
    ticket_prompt,
    response_prompt
)

from prompt_example import get_valid, get_category_l1, get_category_l2, get_ticket, get_response

router = APIRouter()

@router.get("/ticket_qualification")
async def categorize_and_respond(user_input: str):
    # Validation
    valid_eg = get_valid()
    validation_chain = LLMChain(llm=llm3, prompt=validation_prompt)
    validation_result = validation_chain.run(examples = valid_eg, user_input=user_input)

    if validation_result == "incomplete":
        return {"status": "incomplete"}

    # First classification
    category_l1_eg = get_category_l1()
    category_l1_chain = LLMChain(llm=llm2, prompt=category_l1_prompt)
    category_l1 = category_l1_chain.run(examples=category_l1_eg, user_input=user_input)

    # # Second classification
    category_lst = list(map(str.title, category_l1.split("/")))
    categories = " or ".join(category_lst)
    category_l2_eg = get_category_l2(category_lst)
    category_l2_chain = LLMChain(llm=llm3, prompt=category_l2_prompt)
    category_l2 = category_l2_chain.run(categories=categories, examples=category_l2_eg, user_input=user_input)

    # Ticket generation
    ticket_eg = get_ticket()
    ticket_chain = LLMChain(llm=llm1, prompt=ticket_prompt)
    ticket_result = ticket_chain.run(examples=ticket_eg, user_input=user_input)

    # # Response generation
    response_eg = get_response("electrical")
    response_chain = LLMChain(llm=llm2, prompt=response_prompt)
    response = response_chain.run(examples=response_eg, user_input=user_input)

    return {
        "ticket_status": ticket_result,
        "category": category_l2,
        "response": response
    }