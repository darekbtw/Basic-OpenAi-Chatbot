from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

# Fetches your API key in the .env file
api_key = os.getenv('OPENAI_API_KEY')

# Base URL for the OpenAI API chat completions
url = "https://api.openai.com/v1/chat/completions"

# Headers for the request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Initialize the conversation history
conversation = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]

def ask_openai(question):
    # Append the user's message to the conversation
    conversation.append({
        "role": "user",
        "content": question
    })
    
    # Define the payload with the conversation history
    payload = {
      "model": "gpt-3.5-turbo",
      "messages": conversation
    }
    
    # Make the POST request and process the response
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        message = response_data["choices"][0]["message"]["content"]
        # Append the AI's response to the conversation
        conversation.append({
            "role": "assistant",
            "content": message
        })
        return message
    else:
        return f"Error: {response.status_code}"

# Main loop
while True:
    # Get input from the user
    user_input = input("You: ")
    
    # Check if the user wants to exit
    if user_input.lower() == "exit":
        print("Exiting chat")
        break
    
    # Get the response from OpenAI and print it
    response_message = ask_openai(user_input)
    print("AI:", response_message)
