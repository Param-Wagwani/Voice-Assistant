import speech_recognition as sr
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Microphone initialized successfully.")
        print("Listening...")
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=8,phrase_time_limit=8)
            
            print("Audio captured.")
            text = recognizer.recognize_google(audio)
            print("Recognized:", text)
            return text
        except sr.WaitTimeoutError:
            print("Timeout waiting for audio.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return ""
        except sr.RequestError:
            print("Sorry, could not request results.")
            return ""
        
        
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Greeting the user:
print("Hello! How can I assist you today?")
speak("Hello! How can I assist you today?")
while True:
    input_text = recognize_speech()
    if input_text.lower() == "stop":
        speak("Goodbye!")
        break
    if input_text:
        print("You said:", input_text)
        speak("You said: " + input_text)
   
