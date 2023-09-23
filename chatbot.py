
import random
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm just a bot, but I'm here to help.", "I'm doing well, how about you?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "Sorry, I can't help with that."],
}
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])
print("Chatbot: Hello! How can I assist you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
