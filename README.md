# CodeAlpha Python Programming Internship - Task 4: Basic Chatbot

## 📝 Project Overview
This repository contains a simple, interactive, rule-based **Basic Chatbot** developed in Python. The chatbot, named **AlphaBot**, operates in the command console. It recognizes and processes key user intents such as greetings, queries about its status or identity, requests for instructions, and commands to exit, returning randomized natural responses.

## 🎯 Objective
This project demonstrates string tokenization, case-insensitive string parsing, regular expression sanitization (removing punctuation marks to handle input varieties), conditional loops, and modular function architecture.

---

## ✨ Features
- **Punctuation & Capitalization Independence**: Cleans user inputs by stripping symbols (e.g. `!`, `?`, `.`) and standardizing case so queries like `"HELLO?!"`, `"hello"`, or `"Hey!"` all map to the greeting intent.
- **Dynamic Dialogue Responses**: Selects responses randomly from lists of predefined sentences for each intent, avoiding robotic repetition.
- **Continuous Session Loop**: Maintains a live session window that accepts user input continuously.
- **Conversational Triggers Recognized**:
  - `hello` / `hey` / `greetings`
  - `hi`
  - `how are you` / `how is it going`
  - `what is your name` / `who are you`
  - `help` / `commands`
  - `bye` / `exit` (Closes connection)
- **Robust Fallback Engine**: Returns friendly, varied responses when an input doesn't match any triggers.

---

## 🛠️ Technologies Used
- **Language**: Python 3
- **Core Modules**: `re`, `random`

---

## 📂 Folder Structure
```text
CodeAlpha_BasicChatbot/
│
├── chatbot.py          # Core Chatbot Script (Execution Entrypoint)
├── README.md           # Project Documentation
└── screenshots/        # Directory containing sample run previews
```

---

## 🚀 Installation & Getting Started

### Prerequisites
- **Python**: Make sure Python 3.x is installed:
  ```bash
  python --version
  ```

### Installation Steps
1. Navigate to the chatbot project directory:
   ```bash
   cd CodeAlpha_BasicChatbot
   ```

---

## 🎮 How to Run
Run the chatbot script from your terminal:
```bash
python chatbot.py
```

---

## 💬 Sample Conversation Log

Here is a typical console interaction log:

```text
==================================================
         WELCOME TO ALPHABOT ASSISTANT!          
==================================================
Type your message below. Enter 'help' for instructions.
Type 'bye' or 'exit' to end the conversation.
--------------------------------------------------

[AlphaBot]: Hello! I am ready to chat. What's on your mind?

[You]: hello!
[AlphaBot]: Hi there! How is your day going? How can I help?

[You]: what is your name?
[AlphaBot]: I am AlphaBot, your friendly CodeAlpha automated assistant!

[You]: how are you doing today
[AlphaBot]: Fantastic! Ready to chat and help you out. How are you doing today?

[You]: tell me something about programming
[AlphaBot]: I'm a basic chatbot and still learning. Try asking me for 'help'!

[You]: help
[AlphaBot]: Need help? You can say things like 'hello', 'who are you', 'how are you', or type 'bye' to exit.

[You]: bye
[AlphaBot]: Goodbye! It was a pleasure chatting with you. Have a great day!

==================================================
              CHAT SESSION ENDED                 
==================================================
```

---

## 📈 Future Improvements
- **Natural Language Processing (NLP)**: Integrate modern libraries like `nltk`, `spaCy`, or `chatterbot` to identify intents semantically rather than relying on exact keyword matching.
- **Graphical User Interface (GUI)**: Create a modern chat window using Python `tkinter` or build a web client using Streamlit or Flask.
- **External Web APIs**: Integrate APIs to let the chatbot fetch real-world data like weather forecasts, stock prices, or news summaries.
- **Context Management**: Introduce state memory so the chatbot remembers statements across multiple lines of input (e.g., remembering the user's name).
