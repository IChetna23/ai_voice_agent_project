import pyttsx3
import os

def generate_wav(text, path):
    engine = pyttsx3.init()
    engine.save_to_file(text, path)
    engine.runAndWait()

# Create sample_audio/hr_questions if not exists
os.makedirs("sample_audio/hr_questions", exist_ok=True)

# Generate questions
questions = [
    "Please introduce yourself.",
    "What are your key skills?",
    "How many years of experience do you have?",
    "Where are you currently located?",
    "Are you open to relocating for the job?"
]

for i, q in enumerate(questions):
    generate_wav(q, f"sample_audio/hr_questions/q{i+1}.wav")
