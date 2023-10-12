#first_classification_prompt.py
from langchain import PromptTemplate

def get_first_classification_prompt():
    first_classification_prompt = PromptTemplate(
        input_variables=["user_input"],
        template="""
Classify the block of text into the following categories: (Electrical / IT), (Cleaning/ Janitorial),  (Building/ Infrastructure) , (Security) only using the examples below -

Give your response in the format below:

[complaint classification]

Examples:

Electrical/IT:
"The lights in the break room are flickering."
"The computer system is down."
"The security cameras are not working."
"The fire alarm is going off for no reason."
"The air conditioning is not working."

Cleaning/Janitorial:
"The trash cans are overflowing."
"The floors are dirty."
"The bathrooms are not clean."
"There is graffiti on the walls."
"The carpets are stained."

Building/Infrastructure:
"The roof is leaking."
"The windows are broken."
"The doors are sticking."
"The stairs are creaky."
"The parking lot is cracked."

Security:
"There is a security breach."
"Someone has been vandalizing the property."
"There have been reports of theft."
"The security guards are not doing their job."
"The security cameras are not working."


Block of Text: {user_input}
"""
)
    return first_classification_prompt
