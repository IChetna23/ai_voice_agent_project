# ai_voice_agent_project
Voice AI Agent for Telephonic screening of Candidates - This is an automated calling agent that is capable of asking general screening questions like: Basic Introduction, Skillset, experience, etc. The agent transcribes, analyzes, reasons, and screens-in the candidates based on their responses

✨ Features
🎤 Voice-based HR Questioning using gTTS and pygame

🔊 Candidate Response Playback via pre-recorded .wav files

🧠 Automatic Transcription using OpenAI Whisper

🧪 NLP Pipeline for:

Sentiment Analysis

Keyword Extraction

WH-Question Detection

⚙️ Rule-Based Reasoning Engine (agent_logic.py) to:

Flag candidates

Prompt for more information

Auto-respond to candidate queries

Final recommendation based on sentiment, content, and question handling

🗂️ Folder Structure
graphql
Copy
Edit
project-root/
├── stimulate_call.py        # Main simulation logic
├── agent_logic.py           # Rule-based reasoning
├── nlp_pipeline.py          # NLP pipeline using spaCy/textblob/etc.
├── sample_audio/            # Contains folders: candidate1, candidate2, candidate3
│   ├── candidate1/
│   │   ├── a1.wav
│   │   ├── a2.wav
│   │   └── ...
│   └── candidate2/
│       └── ...
└── README.md                # This file
🛠️ How It Works
The HR Agent speaks predefined questions one by one.

The candidate's voice reply (pre-recorded .wav) is played.

Whisper AI transcribes the audio to text.

The NLP pipeline analyzes the transcript:

Extracts tone and key information

Detects WH-questions asked by the candidate

Agent logic evaluates:

Whether to flag, prompt, or proceed

Auto-responses are triggered for candidate questions like:

“What tech stack do you use?”

“Is this a remote role?”

🗣️ Sample Questions Asked
Please introduce yourself.

What is your experience and skill set?

Where are you currently located?

Are you willing to join immediately?

Do you have any questions for us?

▶️ Run the Simulation (stimulate_call.py)
1. Install Requirements
bash
Copy
Edit
pip install pygame gTTS openai-whisper pyttsx3
2. Run the Agent
bash
Copy
Edit
python stimulate_call.py
Then enter:

bash
Copy
Edit
Enter candidate number (e.g., 1, 2, 3): 1
🎧 Make sure candidate audio files exist in sample_audio/candidate1/ as a1.wav, a2.wav, etc.

🧰 Technologies Used
Python

Whisper by OpenAI (for transcription)

Hugging Face Transformers (for NLP tasks - Sentiment Analysis and NER)

gTTS + Pygame (for Text-to-Speech and audio)

Custom Rule-Based Logic
