import text_speech
import speech_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_speech.text_speech("My name is Syar assistant")
        return "My name is Syar assistant"
    
    elif "describe myself" in user_data or "who am i" in user_data:
        text_speech.text_speech("Syarvani Kota is a final-year B.Tech student in Electronics and Telematics Engineering at GNITS, Hyderabad, graduating in May 2025, she is a passionate AI/ML enthusiast with expertise in Python, AI, ML, web development (HTML, CSS, JS, PHP, MySQL), Power BI, Blender, Arduino, and IoT. She has developed innovative projects like FunAudioLLM, an advanced speech AI model for emotion detection and speech synthesis, and Profile Peek, an AI-powered recruitment platform leveraging psychometric assessments and ML predictions. She was a NASA Space Apps 2023 national finalist, ranked 16th at the National Hackathon 2023 (IIIT Hyderabad), and participated in the National Megathon 2023 and a healthcare-focused AI challenge. An active hackathon enthusiast and leader, she has helped organize technical events, workshops, and competitions.")
        return "Syarvani Kota is a final-year B.Tech student in Electronics and Telematics Engineering at GNITS, Hyderabad, graduating in May 2025. She is apassionate AI/ML enthusiast with expertise in Python, AI, ML, web development (HTML, CSS, JS, PHP, MySQL), Power BI, Blender, Arduino, and IoT. She has developed innovative projects like FunAudioLLM, an advanced speech AI model for emotion detection and speech synthesis, and Profile Peek, an AI-powered recruitment platform leveraging psychometric assessments and ML predictions. She was a NASA Space Apps 2023 national finalist, ranked 16th at the National Hackathon 2023 (IIIT Hyderabad), and participated in the National Megathon 2023 and a healthcare-focused AI challenge. An active hackathon enthusiast and leader, she has helped organize technical events, workshops, and competitions."
   
    elif "hello" in user_data or "hi" in  user_data:
        text_speech.text_speech("Hello, How can I help you")
        return "Hello, How can I help you"
    elif "open my github" in user_data:
        webbrowser.open_new("https://github.com/syarkota?tab=repositories")
        text_speech.text_speech("here's your github account")
        return "here's your github account"

    elif "good morning" in user_data:
        text_speech.text_speech("good morning, sir")
        return "good morning, sir"

    elif "time_now" in user_data or "what's time" in user_data:
        current_time = datetime.datetime()
        Time = (str)(current_time) + "Hour :",(str)(current_time.minute) + "Minute"
        text_speech.text_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_speech.text_speech("ok sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://spotify.com/")
        text_speech.text_speech("spotify is ready for you")
        return "Spotify is ready for you"

    elif "open youtube" in user_data:
        webbrowser.open_new_tab("https://youtube.com")
        text_speech.text_speech("Youtube is ready for you")
        return "Youtube is ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_speech.text_speech("hello google here")
        return "hello google here"
        
    elif "weather" in user_data or "what's the weather in hyderabad" in user_data:
        ans = weather.temp
        text_speech.text_speech(ans)
        return ans
    else:
        ("I'm unable to understand")
        return "I'm unable to understand"
