from revChatGPT.V1 import Chatbot as openAI
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get('ACCESS_TOKEN')

class OpenAIWrapper:
    
    def __init__(self, token):
        self.token = token,
        config = {"access_token" : f"{token}"}
        self.ChatGPT = openAI(config)

    def conversation(self):
        conversation = ""
        while True:
            question = input("")
            for data in self.ChatGPT.ask(question):
                message = data["message"][len(conversation) :]
                print(message, end="", flush=True)
                conversation = data["message"]

ChatGPT = OpenAIWrapper(token=token)
ChatGPT.conversation()
