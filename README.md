## Project Structure

The project is organized into several files and directories:

- `main.py`: This is the main FastAPI application file where the API endpoints are defined.
- `dependencies.py`: Contains the setup and configuration of FastAPI and the integration with the language model.
- `categorize_templates.py`: Stores the `PromptTemplate` for classifying complaints.
- `response_templates.py`: Stores the `PromptTemplate` for generating responses to user complaints.
- `ticket_templates.py`: Stores the `PromptTemplate` for qualifying text as a valid ticket.

## How to Run

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/fastapi-language-model.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-language-model
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
   OPENAI_API_KEY=your_api_key_here
   ```

6. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

7. Access the API in your web browser or use a tool like `curl` or `httpie` to make HTTP requests.

## API Endpoints

- `/ticket_qualification`: Classifies user input as a valid ticket or not, generates responses, and categorizes the complaints into specific categories.

## Multilingual Support

To support multiple languages, each prompt template includes a language instruction, such as "Respond in English/Korean/Spanish." You can customize the supported languages according to your requirements.

## Example Usage

Here's an example of how to use the API endpoint `/ticket_qualification`:

- **Request:**

  ```http
  GET http://localhost:8000/ticket_qualification?user_complaint=The roof is leaking.
  ```

- **Response:**

  ```json
  {
    "ticket_status": "Ticket",
    "category": "Electrical",
    "response": "I apologize for the leak. I will send someone to assess the damage and make any necessary repairs as soon as possible. Please let me know if there is any additional damage."
  }
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python.
- [OpenAI](https://beta.openai.com/): GPT-3.5-based language model used for natural language processing.

---

Feel free to customize this README to include additional information specific to your project or any other details you'd like to highlight.
