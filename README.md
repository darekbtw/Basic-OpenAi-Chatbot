# Basic-OpenAi-Chatbot

This project demonstrates a simple chatbot built with Python, utilizing OpenAI's GPT models via the OpenAI API. The chatbot engages in a text-based conversation, maintaining context through multiple exchanges.

## Prerequisites

- Python 3.6+
- An OpenAI API key

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/darekbtw/Basic-OpenAi-Chatbot.git
cd Basic-OpenAi-Chatbot
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install requests python-dotenv
```

### 3. Setup your .env File

Create a .env file in the root directory of the project. This file will store your OpenAI API key securely.

```bash
OPENAI_API_KEY='your_api_key_here'
```

### 4. Run the Chatbot

To start the chatbot, run the script from the command line:

```bash
python chatbot.py
```