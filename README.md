

https://github.com/user-attachments/assets/af93b56f-075b-4de5-b4af-dcd91c531d56

# SYAR-s-AI-Assistant

SYAR-Assistant is a voice-activated AI assistant built using Python and Tkinter, integrated with speech recognition and text-to-speech capabilities. It can recognize voice commands, respond with text and speech, open websites, provide weather updates, and execute basic tasks like playing music or opening Google/Youtube.

## Features
- **Voice and Text Interaction**: Supports both text input and voice commands.
- **Speech Recognition**: Converts user speech into text.
- **Text-to-Speech (TTS)**: Responds with spoken output.
- **Basic AI Responses**: Answers greetings, tells time, and provides personal descriptions.
- **Web Automation**: Opens YouTube, Google, GitHub, and Spotify on request.
- **Weather Updates**: Fetches weather data for Hyderabad.
- **Shutdown Command**: Closes the application on specific commands.

## Technologies Used
- **Python**: Core programming language.
- **Tkinter**: GUI development.
- **SpeechRecognition**: Converts speech to text.
- **Pyttsx3**: Text-to-Speech conversion.
- **Webbrowser**: Opens websites on command.
- **PIL (Pillow)**: Image processing for displaying assistant image.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/syarkota/SYAR-Assistant.git
   cd SYAR-Assistant
   ```
2. Install dependencies:
   ```sh
   pip install speechrecognition pyttsx3 pillow pyaudio lxml
   ```
3. Run the assistant:
   ```sh
   python assistant.py
   ```

## Usage
- Click the **ASK** button for voice input.
- Type a message and press **Send** to interact.
- Click **Delete** to clear the chat history.
- Say commands like:
  - "Open my GitHub"
  - "Describe myself"
  - "What's the weather in Hyderabad?"
  - "Play music"

## Future Enhancements
- Add NLP for better AI responses.
- Improve GUI with more features.
- Expand to support multiple languages.

## Author
Developed by **Syarvani Kota**, a final-year B.Tech student passionate about AI and Machine Learning.

## License
This project is open-source under the MIT License.

