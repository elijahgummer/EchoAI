import random
import datetime
import re
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

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

# Function to perform arithmetic calculations
def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Sorry, I couldn't perform the calculation. Please provide a valid expression."

# Function to get current date and time
def get_current_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"The current date and time is: {current_time}"

# Function to provide help with general knowledge questions
def provide_help():
    return "I'm here to help! Feel free to ask me anything, and I'll do my best to assist you."

# Function to search for information on Wikipedia
def search_wikipedia(query):
    # API call to Wikipedia to fetch search results
    wikipedia_api_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
    response = requests.get(wikipedia_api_url)
    data = response.json()

    # Extract and return the snippet of the first search result
    if 'query' in data and 'search' in data['query'] and data['query']['search']:
        return data['query']['search'][0]['snippet']
    else:
        return "Sorry, I couldn't find information on that topic."

# Function to process user input and generate AI response
def process_input(user_input, conversation_state):
    user_input = user_input.lower()

    # Determine conversation state based on user input
    if "hello" in user_input:
        conversation_state.greeting_count += 1
    elif "goodbye" in user_input:
        conversation_state.goodbye_count += 1

    # Tokenize user input
    tokens = word_tokenize(user_input)

    # Remove stopwords and perform lemmatization
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [WordNetLemmatizer().lemmatize(token) for token in tokens if token.lower() not in stop_words]

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
    elif any(operator in user_input for operator in ['+', '-', '*', '/']):
        return calculate(user_input)
    elif any(keyword in user_input for keyword in ['time', 'date']):
        return get_current_time()
    elif any(keyword in user_input for keyword in ['help', 'question']):
        return provide_help()
    elif any(keyword in user_input for keyword in ['search', 'wikipedia']):
        query = ' '.join(filtered_tokens)
        return search_wikipedia(query)
    else:
        return "Sorry, I didn't understand that. How can I assist you?"

# Main function to interact with the AI
def main():
    print("Welcome to the Enhanced Echo AI!")

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
