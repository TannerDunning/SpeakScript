import os
from google.cloud import texttospeech
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the service account key file path from the environment variable
key_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

# Create a Text-to-Speech client using the service account key
client = texttospeech.TextToSpeechClient.from_service_account_json(key_path)

# Set the input and output file paths
input_file = "text_files/input.txt"
output_file = "audio_files/output.wav"

# Load the input text from the input file
with open(input_file, "r") as f:
    input_text = f.read()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=input_text)

# Build the voice request
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16

)

# Perform the text-to-speech request
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Save the audio file to the output path
with open(output_file, "wb") as out:
    out.write(response.audio_content)
