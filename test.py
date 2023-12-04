import speech_recognition as sr
from transformers import pipeline

def initialize_chatbot(model_name="microsoft/DialoGPT-medium"):
    return pipeline("conversational", model=model_name)

def initialize_chatbot():
    return pipeline("conversational")

def get_response(chatbot, user_input):
    response = chatbot(user_input)
    return response[0]['generated_responses'][0]

def listen_and_respond(chatbot):
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say something:")
            audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Goodbye!")
                break
            response = get_response(chatbot, user_input)
            print("Assistant:", response)
        except sr.UnknownValueError:
            print("Sorry, couldn't understand audio.")
        except sr.RequestError as e:
            print(f"Error connecting to Google Speech Recognition service: {e}")

if __name__ == "__main__":
    chatbot = initialize_chatbot()
    print("You can say 'exit', 'quit', or 'bye' to end the conversation.")
    listen_and_respond(chatbot)