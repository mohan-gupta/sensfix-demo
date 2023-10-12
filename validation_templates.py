#validation_templates.py
from langchain import PromptTemplate

validation_prompt = PromptTemplate(
  input_variables=["user_input"],
  template="""
  Classify the block of text into "complete complaint" or "incomplete complaint" using the examples below. Give your response in the format below:

 [complaint classification]

 Examples:

  Complete complaint:
  "The pump in the machine room is not working. It is making a loud noise and leaking water."
  "The air conditioning system in the office is not working properly. It is too hot and stuffy." 
  "The fire alarm system in the building is not working. It is not beeping when there is a fire."
  "The security system in the parking garage is not working. The gates are not opening when I press the button."
  "The water heater in the break room is not working. The water is not getting hot."
  "The elevator in the west wing is frequently getting stuck between floors with people inside."
  "The lights in the hallway keep flickering and some bulbs have burnt out."
  "The toilet sink is messy"

  Incomplete complaint: 
  "Hi, My name is Mike."
  "Hello there!"
  "I am feeling sad"

  Block of text: {user_input}
  """
)
