## Project Structure

- `main.py`: This is the main FastAPI application file where we have registered all our endpoints.
- `dependencies.py`: Contains the code for loading environment variables, setting up the MongoDB connection and initializing the llms.
- `prompt_templates.py`: Stores all the template string for the prompts.
- `prompt_examples.py`: Loads all the examples for each prompt from the database.
- `prompts.py`: Creates all the Prompts(LangChain Format) by importing prompt templates from `prompt_templates.py` and examples from `prompt_examples.py`
- `clf_api.py`: This file has the enpoint for classifying the user complaint.
- `rl_apis.py`: This file contains the endpoints for updating the examples for the prompt.
- `translate.py`: This file provides the translation from english to spanish and korean.

## Latest deployment instructions

Commands after SSHing into remote Azure server:

1. cd ssd/sensfix-demo/
2. git pull origin main
3. deactivate
4. rm -rf venv
5. python3.8 -m venv venv
6. source venv/bin/activate
7. pip install -r requirements.txt
8. Inside tmux session:
   ```
   8.1 Ctrl + C
   8.2 deactivate
   8.3 source venv/bin/activate
   8.4 uvicorn main:app --port 9000
   8.5 Ctrl + B. Then D.
   ```
9. deactivate

## How to Run

1. Set up your credentials by creating a `.env` file in the project directory with the following content:

   ```
   MONGO_DB_URI=<your mongo db uri>
   OPENAI_API_KEY=<your api key>
   DB=<database name>
   COLLECTION_CAT_L1=<collection name for category l1>
   COLLECTION_CAT_L1=<collection name for category l2>
   COLLECTION_VALID=<collection name for valid complaint(complete/not complete)>
   COLLECTION_TICKET=<collection name for complaint ticket(ticket/not ticket)>
   COLLECTION_RESP=<collection name for complaint reponse>
   TRANSLATE_KEY=<rapid api key for google translate by google cloud>
   ```
   Translate API link: https://rapidapi.com/googlecloud/api/google-translate1

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/T3xtifyai/sensifix-demo.git
   ```

   and move the .env file into this folder.

3. Navigate to the project directory:

   ```bash
   cd sensifix-demo
   ```

4. There are two ways you can run the app.

   a. Use Docker (recommended)

   first build the docker image
   ```bash
   docker build -t sensfix_image ./
   ```

   second run the docker image
   ```bash
   docker run -d --name sensfix_container -p 80:80 sensfix_image
   ```
   left part in port 80:80 is host port and the right part is the container port.

   b. Virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

   Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   ```bash
   uvicorn main:app
   ```

5. Access the API in your web browser or use a tool like `curl` or `httpie` to make HTTP requests.

## API Endpoints

1. `/ticket_qualification`: Categorize user complaint and generate the appropriate response<br>
<b>inputs</b>: `user_input`: user complaint, `language`, `memory`: previous context.<br>
<b>output</b>: `ticket_status`, `category`, and `response`

2. `/complaint_is_complete`: endpoint to update the valid complaint type(complete/incomplete)<br>
<b>inputs</b>: `text`: complaint text, `correct_class`: could be either ("complete", "incomplete").

3. `/complaint_l1_type`: endpoint to update the correct level 1 category of the complaint<br>
<b>inputs</b>: `text`: complaint text, `correct_class`: could be either ("electrical_it", "cleaning_janitorial", "building_infrastructure", "security").

4. `/complaint_l2_type`: endpoint to update the correct level 2 category of the complaint<br>
<b>inputs</b>: `text`: complaint text, `correct_class`: could be either ("electrical", "it", "cleaning", "janitorial", "building", "infrastructure", "security").

5. `/complaint_response`: endpoint to update the correct response for complaint with the correct category<br>
<b>inputs</b>: `complaint_text`: complaint text, `complaint_response`, `complaint_class`: could be either ("electrical", "it", "cleaning", "janitorial", "building", "infrastructure", "security").

6. `/ticket_clf`: endpoint to update the correct ticket type of the complaint<br>
<b>inputs</b>: `text`: complaint text, `correct_class`: could be either ("ticket", "not_ticket").

## HTTP Status Codes used
- 200: Success
- 430: Incomplete complaint
- 431: Invalid Level 1 classification
- 432: Invalid Level 2 classification
- 504: Project API Gateway Timeout, the request is not completed within time.