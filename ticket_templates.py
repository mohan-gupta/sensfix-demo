# response_templates.py

from langchain import PromptTemplate

# Ticket qualification prompt
ticket_prompt = PromptTemplate(
  input_variables=["user_input"],
  template="""
    Classify the below block of text as either a valid ticket or not a ticket, using the examples as a guide.
    Respond in English/Korean/Spanish:
    
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