from langchain import PromptTemplate

def get_first_classification_prompt():
    first_classification_prompt = PromptTemplate(
        input_variables=["user_input"],
        template="""
Classify the block of text into the following categories (Electrical / IT), (Cleaning/ Janitorial),  (Building/ Infrastructure) , (Security/Not Enough Information) using the examples below -

Examples:

Electrical/IT:
"The lights in the break room are flickering."
"The computer system is down."
"The security cameras are not working."
"The fire alarm is going off for no reason."
"The air conditioning is not working."

Cleaning/janitorial:
"The trash cans are overflowing."
"The floors are dirty."
"The bathrooms are not clean."
"There is graffiti on the walls."
"The carpets are stained."

Building/infrastructure:
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

 Not enough information:
"The service is terrible."
"Something is not working."
"Hi."
"Hello, my name is Mike."

Block of Text:
{user_input}
"""
)
    return first_classification_prompt

