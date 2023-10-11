from langchain import PromptTemplate

validation_prompt = PromptTemplate(
  input_variables=["user_complain"],
  template="""
  Classify the block of text into "complete complaint" or "incomplete complaint" using only the examples below. Respond in English/Korean/Spanish:

  Examples:

  Complete complaints:
  "The pump in the machine room is not working. It is making a loud noise and leaking water."
  "The air conditioning system in the office is not working properly. It is too hot and stuffy." 
  "The fire alarm system in the building is not working. It is not beeping when there is a fire."
  "The security system in the parking garage is not working. The gates are not opening when I press the button."
  "The water heater in the break room is not working. The water is not getting hot."
  "The elevator in the west wing is frequently getting stuck between floors with people inside."
  "The lights in the hallway keep flickering and some bulbs have burnt out."

  Incomplete complaints: 
  "The pump is not working."
  "The air conditioning is not working."
  "The fire alarm is not working."
  "The security system is not working."
  "The water heater is not working."
  "The elevator is not working."
  "The lights are not working."
  "Hi, My name is Mike."
  "Hello there!"

  Block of text: {user_complain}
  """
)