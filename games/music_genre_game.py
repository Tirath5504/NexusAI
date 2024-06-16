from gradio_client import Client, handle_file
import os
import random

client = Client("Tirath5504/NexusMusicGenreClassification")

def classify_audio(file_path):
    result = client.predict(
        filepath=handle_file(file_path),
        api_name="/predict"
    )
    return result

def get_audio():
    folder_path = "./songs/"
    audio_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3") or f.endswith(".wav")]
    if not audio_files:
        return None
    return os.path.join(folder_path, random.choice(audio_files))
