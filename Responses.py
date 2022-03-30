from datetime import datetime

def sample_response(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ['hi', 'hello', 'hey', 'hola', 'bonjour', 'hey there']:
        return "Hello User!"
    if user_message in ['who are you', 'what is your name', 'what is your name?']:
        return "I am a bot created by the developers of the AI-Chatbot project. I am currently in development and will be updated soon."
    if user_message in ['time', 'what time is it', 'what is the time', 'what is the time now', 'what is the time now?']:
        now = datetime.now()
        date_time = now.strftime("%d:%m:%y, %H:%M:%S")
        return "The time is " + date_time
    return "I don't understand what you are saying."
    
     