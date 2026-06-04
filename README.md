# Voice to Diary 🗣️➡️📔

A Streamlit-based diary application that converts voice recordings into written diary entries using OpenAI Whisper. Users can record their thoughts, convert speech to text, save diary entries by date, and listen to previously saved notes using text-to-speech.

## Features

* 🎙️ Record audio directly in the browser
* 📝 Convert speech to text using Whisper AI
* ✏️ Edit diary entries before saving
* 💾 Save diary notes with date-based organization
* 🔍 Search diary entries by date
* 🔊 Read saved diary entries aloud using Text-to-Speech
* ♻️ Re-record audio with the clear audio option
* 🎨 Simple and user-friendly Streamlit interface

## Tech Stack

* Python
* Streamlit
* OpenAI Whisper
* gTTS (Google Text-to-Speech)
* FFmpeg

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/voice-to-diary.git
cd voice-to-diary
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit openai-whisper gtts torch
```

### 4. Install FFmpeg

Whisper requires FFmpeg.

Download and install FFmpeg:

https://ffmpeg.org/download.html

Verify installation:

```bash
ffmpeg -version
```

## Running the Application

```bash
streamlit run app.py
```

The application will open in your browser automatically.

## Project Structure

```text
voice-to-diary/
│
├── app.py
├── diary_notes/
│   ├── 04-06-26.txt
│   └── ...
├── requirements.txt
├── README.md
└── audio.mp3
```

## How It Works

### Add Diary

1. Record audio using the microphone.
2. Click **Convert to Diary**.
3. Whisper transcribes the speech into text.
4. Edit the generated diary note if needed.
5. Click **Save Diary Note**.

### Search Diary

1. Select a date.
2. Click **Search**.
3. View the saved diary entry.
4. Click **Read Diary** to hear the note spoken aloud.

## Dependencies

```text
streamlit
openai-whisper
gtts
torch
ffmpeg
```

## Future Improvements

* Multi-language transcription
* User authentication
* Cloud storage integration
* Emotion and sentiment analysis
* Diary entry categorization
* Download diary entries as PDF

## Screenshots

Add screenshots of the application here.

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Author

Developed with ❤️ using Streamlit, Whisper, and Python.
