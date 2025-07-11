import os
import time
import uuid
import pygame
import whisper
from gtts import gTTS
import pyttsx3
from agent_logic import agent_decision
from nlp_pipeline import run_nlp_pipeline

# Initialize models and engines
whisper_model = whisper.load_model("base", device="cpu")
tts_engine = pyttsx3.init()
pygame.mixer.init()

# HR questions to be asked
questions = [
    "Please introduce yourself.",
    "What is your experience and skill set?",
    "Where are you currently located?",
    "Are you willing to join immediately?",
    "Do you have any questions for us?"
]

# Function to convert text to speech and play it
def speak(text):
    print("HR:", text)
    filename = f"temp_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text)
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.mixer.init()

    try:
        os.remove(filename)
    except Exception as e:
        print("Could not delete temp file:", filename, e)

# Function to play candidate's audio response
def play_audio(path):
    if os.path.exists(path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print("Audio not found:", path)

# Function to transcribe candidate's response using Whisper
def transcribe(path):
    print("Transcribing:", os.path.basename(path))
    result = whisper_model.transcribe(path)
    print("Transcript:", result["text"])
    return result["text"]

# Main simulation function for a candidate
def simulate_candidate(candidate_number):
    folder_path = os.path.join("sample_audio", f"candidate{candidate_number}")
    if not os.path.isdir(folder_path):
        print("Folder not found:", folder_path)
        return

    print("Starting call simulation for Candidate", candidate_number)
    full_transcript = ""

    for i, question in enumerate(questions):
        speak(question)

        audio_file = f"a{i+1}.wav"
        audio_path = os.path.join(folder_path, audio_file)

        if os.path.exists(audio_path):
            play_audio(audio_path)
            response = transcribe(audio_path)
            full_transcript += response + " "

            # Handle candidate questions in real time
            if "?" in response:
                if "role" in response.lower():
                    speak("This role involves backend development using Python and Django.")
                elif "remote" in response.lower():
                    speak("Currently, this role is hybrid with some flexibility.")
                elif "tech" in response.lower():
                    speak("We primarily use Python, Django, and PostgreSQL.")
                else:
                    speak("That's a good question. We'll share details in the follow-up email.")

            time.sleep(1)
        else:
            print(f"Audio not found for question {i+1}: {audio_file}")
            time.sleep(1)

    # Run NLP and agent logic
    print("Running NLP and agent logic...")
    nlp_result = run_nlp_pipeline(full_transcript)
    decision = agent_decision(nlp_result["sentiment"], nlp_result["keywords"], full_transcript)

    speak("Thank you for your responses. We will get back to you shortly.")

    # Display final output
    print("\nFinal Screening Results")
    print("Transcript:")
    print(full_transcript.strip())
    print("\nNLP Output:")
    print("Sentiment:", nlp_result["sentiment"])
    print("Keywords:", nlp_result["keywords"])
    print("\nAgent Decision:")
    for k, v in decision.items():
        print(f"{k}: {v}")

# Entry point
if __name__ == "__main__":
    candidate_input = input("Enter candidate number (e.g., 1, 2, 3): ").strip()
    simulate_candidate(candidate_input)
