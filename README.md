# 🎙️ Voice Assistant Desktop Application

A simple Python-based **Voice Assistant** desktop application using speech recognition, text-to-speech, and a graphical interface.  
The assistant listens to voice commands and performs actions such as opening websites and responding with voice feedback.

---

## 📌 Project Overview

This project implements a basic AI voice assistant that can:
- Recognize voice commands using a microphone
- Convert text to speech (TTS)
- Play audio responses
- Open websites using voice commands
- Display recognized input and responses in a GUI

---

## 🧠 Features

- 🎤 Voice input using microphone  
- 🗣️ Speech recognition (Google Speech API)  
- 🔊 Text-to-speech responses  
- 🖥️ GUI using Tkinter  
- 🌐 Website automation  
- 🔔 Sound effects integration  
- 🧩 Command-based logic system  

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter** (GUI)
- **SpeechRecognition**
- **pyttsx3** (Text-to-Speech)
- **winsound** (Audio playback)
- **OS module**
- **Google Speech API**

---

## 📂 Project Structure

```text
voice-assistant/
│
├── assistant.py
├── OPen-Google.wav
├── Welcome.wav
├── Good-Morning.wav
├── Good-Evening.wav
├── Help.wav
└── dist/
🎯 Supported Voice Commands
Command Keyword	Action
google	Opens Google in Chrome
facebook	Opens Facebook in Chrome
welcome	Plays welcome response
morning	Good morning greeting
evening	Good evening greeting
help	Help response
unknown	Error response
🧪 Example Commands
"open google"
"open facebook"
"good morning"
"welcome"
"help"
🚀 How to Run
Install dependencies:

pip install pyttsx3 SpeechRecognition pyaudio
Make sure audio files are in the same directory:

OPen-Google.wav
Welcome.wav
Good-Morning.wav
Good-Evening.wav
Help.wav
Run the program:

python assistant.py
🖥️ Interface
🎤 Microphone button for voice input

📥 Input text display (recognized speech)

📤 Output text display (assistant response)

📦 Executable Build
Executable version generated in:

C:\Users\SkyTop\python\dist
🔒 Platform Support
✅ Windows (Fully supported)

⚠️ Linux/Mac: Requires replacing winsound module

📈 Future Improvements
NLP-based intent detection

Custom command training

AI chatbot integration

Multi-language support

Smart home integration

API integrations (Weather, Time, Search)

Wake-word detection

👩‍💻 Author
Shereen Alaa
Machine Learning Engineer

GitHub: https://github.com/shreenalaa

LinkedIn: https://www.linkedin.com/in/shreen-alaa/

✨ A simple foundation for building intelligent voice-based desktop assistants.
