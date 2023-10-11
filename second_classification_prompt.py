from langchain import PromptTemplate

def get_second_classification_prompt():
    second_classification_prompt = PromptTemplate(
        input_variables=["user_complain"],
        template="""
    Classify the complaint into one of the following categories (Electrical), (IT), (Cleaning), (Janitorial),  (Building), (Infrastructure), (Security), (Not Enough Information) using the examples below. 
    If there is not enough information, respond with 'Not enough information'.

    Examples:

Electrical:
The lights are flickering.
The power is out.
The circuit breaker is tripped.
The outlet is not working.
The fuse is blown.
The breaker is humming.
The wiring is exposed.
The electrical panel is hot.
The generator is not working.
The lightning protection system is not working.
The fire alarm is not working.

IT:
The computer is not turning on.
The internet is down.
The printer is not working.
The software is not working.
The data is lost.
The virus is spreading.
The firewall is not working.
The network is not secure.
The server is down.
The website is not working.

Cleaning:
The trash cans are overflowing.
The floors are dirty.
The bathrooms are not clean.
There is graffiti on the walls.
The carpets are stained.
The windows are dusty.
The tables are sticky.
The chairs are covered in crumbs.
The desks are cluttered.
The appliances are dirty.
The equipment is dusty.

Janitorial:
The floors need to be mopped.
The trash needs to be taken out.
The bathrooms need to be cleaned.
The graffiti needs to be removed.
The carpets need to be vacuumed.
The windows need to be cleaned.
The tables need to be wiped down.
The chairs need to be dusted.
The desks need to be organized.
The appliances need to be cleaned.
The equipment needs to be dusted.

Building:
The roof is leaking.
The windows are broken.
The doors are sticking.
The stairs are creaky.
The walls are peeling.
The floors are uneven.
The plumbing is backed up.
The electrical wiring is faulty.
The HVAC system is not working properly.
The fire alarm is not working.
The security system is not working.

Infrastructure:
The roads are cracked.
The bridges are rusting.
The sewers are overflowing.
The water pipes are leaking.
The power lines are down.
The cell phone towers are not working.
The internet is down.
The train tracks are damaged.
The airport runway is cracked.
The harbor is polluted.

Security:
"There has been a security breach in the office."
"Someone has been vandalizing the property."
"There have been reports of theft in the building."

Not enough information:
"The service is terrible."
"Something is not working."

Complaint: {user_complain}
    """
)

    return second_classification_prompt
