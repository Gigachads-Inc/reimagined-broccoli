from revChatGPT.V1 import Chatbot as openAI
from dotenv import load_dotenv as env
import os
env()

token = os.environ.get('ACCESS_TOKEN')

class OpenAIWrapper:

    prompts = {
        "summary": "Please make a short summary in total of 50 letters from the following text: ",
        "hello world": "say Hello World!"
    }

    def __init__(self, token):
        self.token = token,
        config = {"access_token" : f"{token}"}
        self.ChatGPT = openAI(config)

    def promptGenerator(self, flag):
        match flag:
            case 'summary':
                prompt = self.prompts.get('summary')
                return prompt
            case _:
                raise KeyError("Prompt codename doesn't exist")

    def ask(self, prompt):
        response = ""
        for data in self.ChatGPT.ask(prompt):
            response = data["message"]
        print(response)

    def conversation(self):
        conversation = ""
        while True:
            question = input("")
            for data in self.ChatGPT.ask(question):
                message = data["message"][len(conversation):]
                print(message, end="", flush=True)
                conversation = data["message"]
