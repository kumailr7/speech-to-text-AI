### Speech-to-Text (AI) Project
This project is a Python-based application that utilizes advanced AI models for speech recognition and text processing. It allows users to record speech, convert it to text (transcript), and then interact with Google Gemini to obtain AI-generated responses based on the transcript.

## Features
-- *Real-time Speech Recognition:* Converts spoken words into text using OpenAI's Whisper.

-- *Audio Recording:* Captures user speech input via microphone.

-- *Transcript Saving:* Saves the converted speech into a text file.

-- *Integration with Google Gemini:* Uses Google Gemini for AI-driven responses based on the user's speech transcript.

-- *Integration with Streamlit:* It has now a UI based Interaction using streamlit UI.

-- *Increase the duration of Recording audio:* Now user can increase the durations of recording , it will be helpful in recording long audio file. 


## Dependencies

`openai-whisper`

`sounddevice`

`scipy`

`pydub`

`google-generativeai`

`python-dotenv`

`streamlit`

## Setup

1. Clone the repository:

```
git clone https://github.com/yourusername/speech-to-text-AI.git
```

2. Create an virtual environment:

```
python -m venv venv
```

3. Activate the Virtual Environment:

```
source venv/bin/activate
```

4. Install Dependencies:

Ensure you have Python 3.6 or later installed. Install the required dependencies using `pip`

```
pip install -r requirements.txt
```

5. Set up environment variables:

Create a .env file in the project directory with the following content:

```
# Google Gemini API key
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key_here
```

6. Run the application:

```
streamlit run streamlit.py
```

## Usage

*Recording Speech:*

Speak into your microphone when prompted. The application will record your speech.

*Saving Transcript:*

After recording, the speech will be converted into text (transcript) and saved in a file.

*Interacting with Google Gemini:*

The transcript is used as input for Google Gemini. The application sends the transcript to Google Gemini API and displays the AI-generated response.

*Getting AI Responses:*

You will see the response from Google Gemini based on the speech transcript provided.

## Example

Here's a brief example of how to use the application:

-- User speaks into the microphone.

-- The application records the speech and converts it into text.

-- The text (transcript) is saved in a file.

-- The transcript is sent to Google Gemini.

-- Google Gemini processes the transcript and generates an AI response.

-- The application displays the AI response.

-- Below you can see an image of the application.

![alt text](<Screenshot from 2024-07-24 01-04-58.png>)


