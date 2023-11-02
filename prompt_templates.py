summary_template = """
Summarize the given user problem to a pertinent complaint as short as possible
without loosing the context of the problem. If no complaint or problem is mentioned then just write:
"No Specific Complaint"

User Complaint: {context}

Summary: 
"""

validation_template ="""
Classify the block of text into "complete complaint" or "incomplete complaint" using the examples below. Give your response in the format below:

[complaint classification]

Examples:

{examples}

Block of text: {user_input}
"""

category_l1_template = """
Classify the block of text into the following categories: (Electrical / IT), (Cleaning/ Janitorial),  (Building/ Infrastructure) , (Security) only using the examples below -

Examples:

{examples}

Block of Text: {user_input}
Category:
"""

category_l2_template = """
Classify the complaint into {categories} using the examples below. 

Give your response in the format below:

[complaint classification]

Examples:

{examples}

Block of Text: {user_input}
"""

ticket_template = """
Classify the below block of text as either "ticket" or "not a ticket" using the examples below:

Examples:

{examples}
    
Block of text: {user_input}
"""

response_template = """
Generate a resolution for a user complaint using the examples below:

Examples:

{examples}

Complaint: {user_input}
Response:
"""