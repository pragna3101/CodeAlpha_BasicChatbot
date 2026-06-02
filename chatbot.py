#!/usr/bin/env python3
"""
CodeAlpha Python Internship
Task 4: Basic Chatbot

A simple rule-based console chatbot that recognizes various user intents,
normalizes inputs (punctuations, capitalization), and provides dynamic
predefined responses from a curated dictionary.
"""

import random
import re

# Dictionary mapping intent keywords to lists of dynamic responses
INTENT_RESPONSES = {
    "hello": [
        "Hello! Great to meet you. How can I assist you today?",
        "Hi there! How is your day going? How can I help?",
        "Hey! Welcome. What can I do for you today?"
    ],
    "hi": [
        "Hi! Hope you are having a wonderful day. What's on your mind?",
        "Hello! How can I help you today?",
        "Hey! Good to see you. How can I assist you?"
    ],
    "how_are_you": [
        "I'm just a computer script, but I'm operating at 100% efficiency! How are you?",
        "I am doing great, thank you for asking! How are things with you?",
        "Fantastic! Ready to chat and help you out. How are you doing today?"
    ],
    "what_is_your_name": [
        "I am AlphaBot, your friendly CodeAlpha automated assistant!",
        "My friends call me AlphaBot. I'm a simple rule-based Python chatbot.",
        "I'm AlphaBot, built using standard Python logic for your internship task!"
    ],
    "help": [
        "Sure! I can answer greetings, tell you my name, or say goodbye. Just type away!",
        "I'm here to demonstrate basic chatbot interactions! Try asking: 'how are you' or 'what is your name'.",
        "Need help? You can say things like 'hello', 'who are you', 'how are you', or type 'bye' to exit."
    ],
    "bye": [
        "Goodbye! It was a pleasure chatting with you. Have a great day!",
        "Bye! Take care and happy coding!",
        "Farewell! Hope to talk to you again soon."
    ]
}

# Fallback responses when the chatbot doesn't understand the user
FALLBACK_RESPONSES = [
    "Hmm, I'm not sure I understand that. Could you try rephrasing?",
    "I'm a basic chatbot and still learning. Try asking me for 'help'!",
    "Interesting point! Unfortunately, my programming doesn't cover that yet. Try another question.",
    "I didn't quite catch that. Try greetings like 'hello', 'hi', or ask 'what is your name?'."
]


def clean_input(user_input):
    """
    Cleans user input by:
    1. Converting text to lowercase.
    2. Stripping leading/trailing whitespace.
    3. Removing common punctuations (e.g., ?, !, ., ,).
    """
    # Convert to lowercase
    cleaned = user_input.lower().strip()
    # Remove punctuation using regex
    cleaned = re.sub(r'[?!.,:;\'"-]', '', cleaned)
    return cleaned.strip()


def determine_response(cleaned_text):
    """
    Checks the cleaned user input text against predefined intent keywords
    and returns a matching response. Returns a fallback response if no match is found.
    """
    # Check for 'bye' first
    if "bye" in cleaned_text or "exit" in cleaned_text:
        return random.choice(INTENT_RESPONSES["bye"]), True

    # 1. Match 'how are you' (check this before 'you')
    if "how are you" in cleaned_text or "how is it going" in cleaned_text:
        return random.choice(INTENT_RESPONSES["how_are_you"]), False

    # 2. Match 'what is your name' / 'who are you'
    if "name" in cleaned_text or "who are you" in cleaned_text or "what is your name" in cleaned_text:
        return random.choice(INTENT_RESPONSES["what_is_your_name"]), False

    # 3. Match 'hello'
    if "hello" in cleaned_text or "hey" in cleaned_text or "greetings" in cleaned_text:
        return random.choice(INTENT_RESPONSES["hello"]), False

    # 4. Match 'hi' (simple check)
    if "hi" in cleaned_text.split():
        return random.choice(INTENT_RESPONSES["hi"]), False

    # 5. Match 'help'
    if "help" in cleaned_text or "commands" in cleaned_text or "what can you do" in cleaned_text:
        return random.choice(INTENT_RESPONSES["help"]), False

    # No matches found - return a random fallback response
    return random.choice(FALLBACK_RESPONSES), False


def start_chatbot():
    """
    Starts and manages the continuous conversation loop with the user.
    """
    print("\n" + "=" * 50)
    print("         WELCOME TO ALPHABOT ASSISTANT!          ")
    print("=" * 50)
    print("Type your message below. Enter 'help' for instructions.")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("-" * 50)
    
    print("\n[AlphaBot]: Hello! I am ready to chat. What's on your mind?")
    
    while True:
        # Get input from user
        try:
            user_raw = input("\n[You]: ")
        except (KeyboardInterrupt, EOFError):
            print("\n\n[AlphaBot]: Session interrupted. Goodbye!")
            break
            
        # Ignore empty inputs
        if not user_raw.strip():
            continue
            
        # Clean input
        cleaned_text = clean_input(user_raw)
        
        # Determine response and exit status
        response, should_exit = determine_response(cleaned_text)
        
        # Display response
        print(f"[AlphaBot]: {response}")
        
        if should_exit:
            break
            
    print("\n" + "=" * 50)
    print("              CHAT SESSION ENDED                 ")
    print("=" * 50 + "\n")


def main():
    """
    Entry point for the chatbot application.
    """
    start_chatbot()


if __name__ == "__main__":
    main()
