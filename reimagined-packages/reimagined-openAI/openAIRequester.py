from revChatGPT.V1 import Chatbot as openAI
from dotenv import load_dotenv as env
import os
env()

token = os.environ.get('ACCESS_TOKEN')

class OpenAIWrapper:

    prompts = {
        "summary": "Please make a short summary from the following text: ",
        "hello world": "say Hello World!"
    }

    def __init__(self, token, context):
        self.context = context,
        self.token = token,
        config = {"access_token" : f"{token}"}
        self.ChatGPT = openAI(config)

    def promptGenerator(self, codename):
        match codename:
            case 'summary':
                prompt = self.prompts.get('summary')
                self.ask(f"{prompt} {self.context}")
            case _:
                raise KeyError("Prompt codename doesn't exist")

    def ask(self, prompt):
        response = ""
        for data in self.ChatGPT.ask(prompt):
            response = data["message"]
        return(response)

    def conversation(self):
        conversation = ""
        while True:
            question = input("")
            for data in self.ChatGPT.ask(question):
                message = data["message"][len(conversation):]
                print(message, end="", flush=True)
                conversation = data["message"]

ChatGPT = OpenAIWrapper(token=token, context="")
ChatGPT.promptGenerator(input(''))