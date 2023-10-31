from fastapi import APIRouter
from enum import Enum

from langchain import LLMChain

from dependencies import llm1, llm2, llm3
from prompts import (
    summary_prompt,
    validation_prompt,
    category_l1_prompt,
    category_l2_prompt,
    ticket_prompt,
    response_prompt
)
from prompt_example import (
    l1_category_lst,
    l2_category_lst,
    get_valid,
    get_category_l1,
    get_category_l2,
    get_ticket,
    get_response
    )

from translate import get_translation

router = APIRouter()

class Language(Enum):
    en = "english"
    es = "spanish"
    ko = "korean"

@router.get("/ticket_qualification")
async def categorize_and_respond(user_input: str, language: Language, memory: str = ""):
    # Combine the user's input and memory
    context = f"{memory}\n{user_input}"
    
    summarize_chain = LLMChain(llm=llm3, prompt=summary_prompt)
    summarized_context = summarize_chain.run(context=context)
    
    # Validation
    valid_eg = get_valid()
    validation_chain = LLMChain(llm=llm3, prompt=validation_prompt)
    validation_result = validation_chain.run(examples=valid_eg, user_input=summarized_context)

    if validation_result == "incomplete":
        return {"status": "incomplete"}

    # Level 1 classification
    category_l1_eg = get_category_l1()
    category_l1_chain = LLMChain(llm=llm2, prompt=category_l1_prompt)
    category_l1 = category_l1_chain.run(examples=category_l1_eg, user_input=summarized_context)

    # Level 2 classification
    l1_categories = l1_category_lst()
    if category_l1.lower().replace("/", "_") not in l1_categories:
        return {'response': "undefined level 1 category"}
    
    category_lst = list(map(str.title, category_l1.split("/")))
    categories = " or ".join(category_lst)

    category_l2_eg = get_category_l2(category_lst)
    category_l2_chain = LLMChain(llm=llm3, prompt=category_l2_prompt)
    category_l2 = category_l2_chain.run(categories=categories, examples=category_l2_eg, user_input=summarized_context)
    
    l2_categories = l2_category_lst()
    if category_l2.lower() not in l2_categories:
        return {'response': "undefined level 2category"}

    # Ticket generation
    ticket_eg = get_ticket()
    ticket_chain = LLMChain(llm=llm1, prompt=ticket_prompt)
    ticket_result = ticket_chain.run(examples=ticket_eg, user_input=summarized_context)

    # Response generation based on language choice
    response_eg = get_response(category_l2)
    response_chain = LLMChain(llm=llm2, prompt=response_prompt)
    response = response_chain.run(examples=response_eg, user_input=summarized_context)
    
    if language.value == "english":
        return {
            "complaint_summary":summarized_context,
            "ticket status": ticket_result,
            "category": category_l2,
            "response": response
        }
    
    to_translate = [
        "complaint summary", summarized_context,
        "ticket status", ticket_result,
        "category", category_l2,
        "response",response
        ]
    
    if language.value == "spanish":
        translations = get_translation(to_translate, language.value)
        
    elif language.value == "korean":
        translations = get_translation(to_translate, language.value)

    result = {}
    for idx in range(1, len(translations), 2):
        result[translations[idx-1]['translatedText']] = translations[idx]['translatedText'] 

    return result