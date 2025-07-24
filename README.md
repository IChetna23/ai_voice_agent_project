# ai_voice_agent_project
Voice AI Agent for Telephonic screening of Candidates - This is an automated calling agent that is capable of asking general screening questions like: Basic Introduction, Skillset, experience, etc. The agent transcribes, analyzes, reasons, and screens-in the candidates based on their responses

**Features:**

Voice-based HR Questioning using **gTTS** and **pygame**

Candidate Response Playback via pre-recorded **.wav files**

Automatic Transcription using **OpenAI Whisper**

**NLP Pipeline for:**

Sentiment Analysis

Keyword Extraction

WH-Question Detection

**Rule-Based Reasoning Engine (agent_logic.py) to:**

Flag candidates

Prompt for more information

Auto-respond to candidate queries

Final Recommendation based on sentiment, content, and question handling

**Folder Structure:**

project-root/

│

├── stimulate_call.py                # Main simulation logic

├── agent_logic.py         # Rule-based reasoning

├── nlp_pipeline.py        # NLP pipeline using spaCy/textblob/etc.

├── sample_audio/          # Contains folders: candidate1, candidate2, candidate3

│   └── candidate1/

│       ├── a1.wav

│       ├── a2.wav

│       └── ...

└── README.md              # This file

**How It Works?**

1. HR Agent speaks predefined questions one by one, waiting for candidate' response.

2. Candidate's voice reply (pre-recorded .wav) is played.

3. Whisper AI transcribes the audio to text.

4. NLP pipeline analyzes the transcript:

5. Extracts tone and key information

6. Detects WH-questions asked by candidate

7. Agent logic evaluates: Whether to flag, prompt, or proceed

8. Auto-responses are triggered for candidate questions like:

   “What tech stack do you use?”

   “Is this a remote role?”

**Sample Questions Asked:**

1. Please introduce yourself.

2. What is your experience and skill set?

3. Where are you currently located?

4. Are you willing to join immediately?

5. Do you have any questions for us?

**Run the Simulation (stimulate_call.py):**

1. Install Requirements

pip install pygame gTTS openai-whisper pyttsx3

2. Run the Agent

python stimulate_call.py
Then enter:

Enter candidate number (e.g., 1, 2, 3): 1

Make sure candidate audio files exist in sample_audio/candidate1/ as a1.wav, a2.wav, etc.

**Technologies Used**

Python

Whisper by OpenAI (for transcription)

Hugging Face Transformers (for NLP tasks- Sentimental Analysis and NER)

gTTS + Pygame (for TTS + audio)

Custom rule-based logic explained via .png file

