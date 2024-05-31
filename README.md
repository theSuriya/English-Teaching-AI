# English Teaching AI
English Teaching AI is an application that assists in translating Tamil or Tanglish queries into correct English sentences with proper grammar. It utilizes Google's GenerativeAI and Hugging Face's models to generate responses and even provides audio output for the translated sentences.

# How it Works
The application takes a Tamil or Tanglish query as input and generates a correct English sentence with proper grammar as output. It uses Google's GenerativeAI model to understand and respond to the queries. Additionally, it utilizes Hugging Face's text-to-speech model to provide audio output for the translated sentences.

# Deployment
The application is deployed using Hugging Face Spaces. You can access it here.

# Usage
To use the application, follow these steps:

1. Visit the deployment link: English Teaching AI.
2. Enter your Tamil or Tanglish query in the provided text area.
3. Click on the "Analyze" button to generate the English translation.
4. The application will display the translated English sentence along with an audio output option.

# Project Structure
The project structure is as follows:

1. main.py: Contains the main code for the Streamlit web application.
2. README.md: Provides information about the project.
3. requirements.txt: Lists all the dependencies required to run the application.
4. audio_answer.mp3: Stores the audio output for the translated sentences.
# Setup
To set up the project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/Mr-Vicky-01/English-Teaching-AI.git
```
2. **Install Dependencies**: Install the required dependencies by running `pip install -r requirements.txt`.

3. **Google API KEY**:Go to this site to generate api key [HERE](https://aistudio.google.com) You can see left side generate api thn click and copy. Once you have the api key, locate the .env file in your project directory. Open it and paste your aoi key like this:
  ```dotenv
  GOOGLE_API_KEY = "paste the api key here"
  ```
4. **Run the Application**: Run the application locally using Streamlit by executing `streamlit run app.py`.

5. **Access the Application**: Access the application in your web browser at `http://localhost:8501`.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Gemini API](https://developers.google.com/gemini)
- [Hugging Face Spaces](https://huggingface.co/spaces)
