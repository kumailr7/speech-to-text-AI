import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment

def record_audio(duration, sample_rate=16000, channels=2):
    """Record audio from the microphone."""
    st.info("Recording... Please Talk to save the Audio")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    st.success("Recording complete, saving the audio file")
    return audio_data, sample_rate

def save_audio_as_mp3(audio_data, sample_rate, filename):
    """Save the recorded audio data as an MP3 file."""
    wav_filename = filename.replace('.mp3', '.wav')
    write(wav_filename, sample_rate, audio_data)
    audio = AudioSegment.from_wav(wav_filename)
    audio.export(filename, format='mp3')
    os.remove(wav_filename)

def transcribe_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    wav_path = file_path.replace('.mp3', '.wav')
    audio.export(wav_path, format='wav')
    model = whisper.load_model("base")
    st.info("Transcribing the audio file, please wait...")
    result = model.transcribe(wav_path)
    return result['text']

def save_transcription_to_file(transcription, file_path):
    with open(file_path, 'w') as file:
        file.write(transcription)

def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    st.title("AI Speech to Text Application")
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    duration = st.number_input("Enter duration for recording (in seconds):", min_value=1, max_value=60, value=10)

    if st.button("Record Audio"):
        audio_data, sample_rate = record_audio(duration)
        save_audio_as_mp3(audio_data, sample_rate, 'recording.mp3')
        st.success("Audio recorded and saved as 'recording.mp3'")

    if st.button("Transcribe Audio"):
        transcription = transcribe_audio("recording.mp3")
        st.success("Transcription complete")
        st.text_area("Transcription:", transcription)
        save_transcription_to_file(transcription, "transcript.txt")
        st.success("Transcription saved to transcript.txt")

    if st.button("Get AI Response"):
        transcript_text = read_transcript("transcript.txt")
        response = model.generate_content(transcript_text)
        st.text_area("AI Response:", response.text , height=600)

if __name__ == "__main__":
    main()
