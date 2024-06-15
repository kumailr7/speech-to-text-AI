# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key
import os
from dotenv import load_dotenv
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import whisper
import yt_dlp
from pydub import AudioSegment

#### Connecting to microphone #######
def record_audio(duration, sample_rate=44100, channels=2):
    """Record audio from the microphone."""
    print("Recording... Please Talk to save the Audio")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording complete, saving the audio file")
    return audio_data, sample_rate

##### Save the audio file from recording #######
def save_audio_as_mp3(audio_data, sample_rate, filename):
    """Save the recorded audio data as an MP3 file."""
    # Save as a WAV file first
    wav_filename = filename.replace('.mp3', '.wav')
    write(wav_filename, sample_rate, audio_data)
    
    # Convert the WAV file to MP3
    audio = AudioSegment.from_wav(wav_filename)
    audio.export(filename, format='mp3')
    os.remove(wav_filename)  # Remove the intermediate WAV file

if __name__ == "__main__":
    load_dotenv()
    HUME_API_KEY = os.getenv("HUME_API_KEY")

    if not HUME_API_KEY:
        raise ValueError("HUME_API_KEY environment variable not set")

    duration = 10  # Duration in seconds
    audio_data, sample_rate = record_audio(duration)
    save_audio_as_mp3(audio_data, sample_rate, 'recording.mp3')

print("")
print("###############################################################")
print("")

###### Transciption of Audio file ######
def transcribe_audio(file_path):
    # Load the audio file
    audio = AudioSegment.from_file(file_path)

    # Convert audio to WAV format required by whisper
    wav_path = file_path.replace('.mp3', '.wav')
    audio.export(wav_path, format='wav')

    # Load the whisper model
    model = whisper.load_model("base")
    
    print("Transcribing the audio file, please wait...")
    # Transcribe the audio file
    result = model.transcribe(wav_path)
    transcription = result['text']

    return transcription

#### Save the Transcipt of the audio #######
def save_transcription_to_file(transcription, file_path):
    with open(file_path, 'w') as file:
        file.write(transcription)

transcription = transcribe_audio("recording.mp3")
print("Transcription:", transcription)

# Save the transcription to a file
save_transcription_to_file(transcription, "transcript.txt")
print("Transcription saved to transcript.txt")

print("")

print("########################################################")

print("")

print("Wait For the Response From AI")

print("")

# Load environment variables from .env file
load_dotenv()

    # Fetch the Hume API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# Function to read the transcript from a file
def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# File path to the transcript
transcript_file_path = 'transcript.txt'

# Read the transcript from the file
transcript_text = read_transcript(transcript_file_path)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(transcript_text)
print(response.text)

