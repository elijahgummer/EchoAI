import random

# Define conversation states
class ConversationState:
    def __init__(self):
        self.greeting_count = 0
        self.goodbye_count = 0

# Dictionary mapping user input patterns to AI responses
response_patterns = {
    "greeting": ["Hello! How can I assist you today?", "Hi there!", "Hey!"],
    "how_are_you": ["I'm doing well, thank you!", "I'm good, thanks for asking.", "Pretty good!"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Farewell!"],
    "thank_you": ["You're welcome!", "No problem!", "Anytime!"],
    "weather": ["The weather is sunny today.", "It's raining outside.", "Expect some snow later."],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!", 
             "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.", 
             "I told my wife she was drawing her eyebrows too high. She looked surprised!"],
    "favorite_color": ["My favorite color is blue.", "I don't have eyes to see colors, but blue sounds nice!"]
}

# Function to process user input and generate AI response
def process_input(user_input, conversation_state):
    user_input = user_input.lower()

    # Determine conversation state based on user input
    if "hello" in user_input:
        conversation_state.greeting_count += 1
    elif "goodbye" in user_input:
        conversation_state.goodbye_count += 1

    # Match user input to response patterns
    if conversation_state.greeting_count == 1:
        return random.choice(response_patterns["greeting"])
    elif conversation_state.goodbye_count == 1:
        return random.choice(response_patterns["goodbye"])
    elif "thank you" in user_input:
        return random.choice(response_patterns["thank_you"])
    elif "weather" in user_input:
        return random.choice(response_patterns["weather"])
    elif "joke" in user_input:
        return random.choice(response_patterns["joke"])
    elif "favorite color" in user_input:
        return random.choice(response_patterns["favorite_color"])
    else:
        return "Sorry, I didn't understand that."

# Main function to interact with the AI
def main():
    print("Welcome to the Enhanced AI!")

    conversation_state = ConversationState()  # Initialize conversation state

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("AI:", process_input(user_input, conversation_state))
            break

        ai_response = process_input(user_input, conversation_state)
        print("AI:", ai_response)

# Run the main function
if __name__ == "__main__":
    main()
