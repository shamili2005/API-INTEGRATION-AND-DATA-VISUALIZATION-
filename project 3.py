import random
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"]
}

# Simple intent detection function
def get_intent(user_input):
    doc = nlp(user_input.lower())
    if any(word.text in ["hi", "hello", "hey"] for word in doc):
        return "greeting"
    elif any(word.text in ["bye", "goodbye", "see you"] for word in doc):
        return "goodbye"
    elif "thanks" in user_input or "thank you" in user_input:
        return "thanks"
    else:
        return "unknown"

# Chat loop
print("Chatbot: Hello! I'm your AI assistant. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Bye!")
        break
    
    intent = get_intent(user_input)
    if intent in responses:
        print("Chatbot:", random.choice(responses[intent]))
    else:
        print("Chatbot: I'm not sure I understand. Can you rephrase?")
