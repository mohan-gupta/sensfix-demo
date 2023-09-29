from fastapi import FastAPI
from langchain import OpenAI, LLMChain, PromptTemplate 
from dotenv import load_dotenv
import os
import asyncio

app = FastAPI()

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_key, temperature=0.2)

prompt = PromptTemplate(
  input_variables=["user_complain"],
  template="""
    Classify the complaint into one of the following categories:

    Electrical:
    "The lights are flickering."
    "The power is out."
    "The circuit breaker is tripped."
    "The outlet is not working."
    "The fuse is blown."

    IT:
    "The computer is not turning on."
    "The internet is down."
    "The printer is not working."
    "The software is not working."
    "The data is lost."

    Cleaning:
    "The trash cans are overflowing."
    "The floors are dirty." 
    "The windows are dusty."
    "The tables are sticky."
    "The chairs are covered in crumbs."

    Janitorial:
    "The floors need to be mopped."
    "The trash needs to be taken out."
    "The windows need to be cleaned."
    "The tables need to be wiped down."
    "The chairs need to be dusted."

    Building:  
    "The roof is leaking."
    "The windows are broken."
    "The doors are sticking."
    "The walls are peeling."
    "The floors are uneven."

    Infrastructure:
    "The roads are cracked."
    "The bridges are rusting." 
    "The sewers are overflowing."
    "The water pipes are leaking."
    "The power lines are down."

    Security:
    "There is a security breach."
    "Someone has been vandalizing the property."
    "There have been reports of theft."
    "The security guards are not doing their job."
    "The security cameras are not working."

    Complaint: {user_complain}
  """
)

# Response generation prompt
response_prompt = PromptTemplate(
  input_variables=["user_complaint"],
  template="""
    Create a resolution for a Building complaint using the examples below:

    Examples:

    Complaint: The roof is leaking.
    Response: I apologize for the leak. I will send someone to assess the damage and make any necessary repairs as soon as possible. Please let me know if there is any additional damage.

    Complaint: The windows are broken.  
    Response: Thank you for bringing this to my attention. I will send someone to replace the broken windows right away. Please let me know if there are any other issues with the windows that need to be addressed.

    Complaint: The doors are sticking.
    Response: I apologize for the inconvenience. I will send someone today to lubricate the doors and make sure they are opening and closing properly. Please let me know if the issue persists.

    Complaint: The stairs are creaky.
    Response: Thank you for letting me know about the creaky stairs. I will have someone inspect them and make any necessary repairs to fix the creaking. Please let me know if the noise continues after the repairs.

    Complaint: The walls are peeling.
    Response: I appreciate you bringing the peeling walls to my attention. I will have someone assess the walls and make repairs to any damaged areas. Please let me know if you notice the walls peeling in any other locations.

    Complaint: The floors are uneven.
    Response: Thank you for alerting me to the uneven floors. I will send someone to inspect the floors and level out any uneven areas to ensure they are safe to walk on. Please let me know if you notice any other tripping hazards.

    Complaint: The plumbing is backed up.
    Response: I apologize for the backed up plumbing. I will send someone immediately to clear any blockages and get the pipes flowing properly again. Please let me know if you experience any other plumbing issues.

    Complaint: The electrical wiring is faulty.
    Response: Thank you for bringing the faulty wiring to my attention. I will have an electrician inspect all wiring and make any necessary repairs right away. Please let me know if you experience any other electrical problems.

    Complaint: The HVAC system is not working properly.
    Response: I apologize for the issues with the HVAC system. I will send someone to thoroughly inspect it and make any repairs needed to get it working properly again. Please let me know if temperature problems persist.

    Complaint: The fire alarm is not working.
    Response: This is a major concern, thank you for bringing it to my attention. I will send someone to inspect the fire alarm system immediately and make any repairs needed to get it fully operational. Please let me know if any other issues arise.

    Building Complaint: {user_complaint}
  """
)

# Ticket qualification prompt
ticket_prompt = PromptTemplate(
  input_variables=["user_input"],
  template="""
    Classify the below block of text as either a valid ticket or not a ticket, using the examples as a guide:
    
    Examples:
    
    The elevator is not working. (Ticket)  
    The coffee machine is not working. (Not a ticket)
    The toilet is overflowing. (Ticket)
    The trash cans are overflowing. (Not a ticket) 
    The hallway is dirty. (Not a ticket)
    The carpet is stained. (Not a ticket)
    The window is broken. (Ticket)
    The door is sticking. (Ticket)  
    The light bulb is out. (Ticket)
    The fire alarm is going off. (Ticket)
    There is a security breach. (Ticket)
    Someone has been vandalizing the property. (Ticket)   
    There have been reports of theft. (Ticket)
    The security guards are not doing their job. (Ticket) 
    The security cameras are not working. (Ticket)
    I received a suspicious email. (Not a ticket)
    I think my computer has been hacked. (Ticket)
    I am concerned about the security of our data. (Ticket)
    I am not sure who to contact about a security issue. (Not a ticket)  
    I am unhappy with the service I received. (Not a ticket)
    I think the price is too high. (Not a ticket)
    I am not satisfied with the product I received. (Not a ticket)
    
    Block of text:
    {user_input}
  """
)

# Ticket qualification chain 
ticket_chain = LLMChain(llm=llm, prompt=ticket_prompt)
#Response Chain
response_chain = LLMChain(llm=llm, prompt=response_prompt)
#...
categorize_chain = LLMChain(llm=llm, prompt=prompt)

@app.get("/categorize")
async def categorize_and_respond(user_complaint: str):

  if not user_complaint:
    return {"status": "incomplete"} 

  # Run chains
  ticket_result = await asyncio.to_thread(ticket_chain.run, user_complaint)
  category_text = await asyncio.to_thread(categorize_chain.run, user_complaint)
  response = await asyncio.to_thread(response_chain.run, user_complaint)

  # Process outputs
  category_name = category_text.split(":")[0].strip() 
  response = response.split("Response:")[1].strip()

  # Clean ticket status
  ticket_result = ticket_result.strip("\n")

  return {
    "ticket_status": ticket_result,
    "category": category_name,
    "response": response
  }
