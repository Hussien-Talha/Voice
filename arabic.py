import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ar-EG")
        with open("text.txt", "w", encoding="utf-8") as file:
            file.write(f"You said: {text}")
        print("Speech recognition result saved to text.txt.")
    except sr.UnknownValueError:
        print("Sorry, couldn't understand audio.")
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")

listen()