## Project Structure

- `main.py`: This is the main FastAPI application file where we have registered all our endpoints.
- `dependencies.py`: Contains the code for loading environment variables, setting up the MongoDB connection and initializing the llms.
- `prompt_templates.py`: Stores all the template string for the prompts.
- `prompt_examples.py`: Loads all the examples for each prompt from the database.
- `prompts.py`: Creates all the Prompts(LangChain Format) by importing prompt templates from `prompt_templates.py` and examples from `prompt_examples.py`
- `clf_api.py`: This file has the enpoint for classifying the user complaint.
- `rl_apis.py`: This file contains the endpoints for updating the examples for the prompt.

## How to Run

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/T3xtifyai/sensifix-demo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sensifix-demo
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up your OpenAI API key by creating a `.env` file in the project directory with the following content:

   ```
   MONGO_DB_URI=<your mongo db uri>
   OPENAI_API_KEY=<your api key>
   DB=<database name>
   COLLECTION_CAT_L1=<collection name for category l1>
   COLLECTION_CAT_L1=<collection name for category l2>
   COLLECTION_VALID=<collection name for valid complaint(complete/not complete)>
   COLLECTION_TICKET=<collection name for complaint ticket(ticket/not ticket)>
   COLLECTION_RESP=<collection name for complaint reponse>
   ```

6. Run the FastAPI application:

   ```bash
   uvicorn main:app
   ```

7. Access the API in your web browser or use a tool like `curl` or `httpie` to make HTTP requests.