# response_templates.py

from langchain import PromptTemplate

# Response generation prompt
response_prompt = PromptTemplate(
  input_variables=["user_complaint"],
  template="""
    Create a resolution for a user complaint using the examples below, If there is not enough information to classify, respond with 'Not enough information'. 
    Respond in English/Korean/Spanish:
    
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

    Resolving Complaint: {user_complaint}
  """
)