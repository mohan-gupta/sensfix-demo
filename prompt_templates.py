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

# Spanish response template
spanish_response_template = """
Genera una resolución para una queja del usuario utilizando los ejemplos a continuación:
Utilice los ejemplos en inglés y genere la respuesta en español.
Ejemplos:

{examples}

Queja: {user_input}
Respuesta:
"""

# Korean response template
korean_response_template = """
사용자의 불만에 대한 해결책을 아래 예시를 사용하여 생성하세요:
영어로 된 예시를 사용하고 스페인어로 응답을 생성하세요.

예시:

{examples}

불만: {user_input}
응답:
"""
