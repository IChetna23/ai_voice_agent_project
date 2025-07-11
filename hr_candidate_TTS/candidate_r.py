import pyttsx3
import os

def generate_wav(text, path):
    engine = pyttsx3.init()
    engine.save_to_file(text, path)
    engine.runAndWait()

# Create sample_audio/candidate1 if not exists
os.makedirs("sample_audio/candidate1", exist_ok=True)

candidate_responses = {
    "candidate1": [
        "Hi, I’m Alex. I'm currently working at a startup and I’m open to new opportunities.",
        "I know Python, Django, and SQL. Can you tell me more about the role?",
        "I live in Bangalore.",
        "Surely, I will be available to join.",
        "Right now, I am not having any questions but will let you know if I do."
    ],
    "candidate2": [
        "Hi! Sam this side. I am CSE graduate from IPU.",
        "I interned for 6 months and I use Python sometimes",
        "Currently in Mumbai. Can you explain what tech stack you're using?",
        "May be. I have a few projects to finish.",
        "Is there any option for remote work?"
    ],
    "candidate3": [
        "Hey, I don’t want to talk much.",
        "I just do coding.",
        "No experience worth talking about.",
        "I'm somewhere in Delhi. Will join if you pay well.",
        "I don’t know, maybe."
    ]
}

for cname, responses in candidate_responses.items():
    folder = f'sample_audio/{cname}'
    os.makedirs(folder, exist_ok=True)
    for i, ans in enumerate(responses):
       generate_wav(ans, f"{folder}/a{i+1}.wav")
