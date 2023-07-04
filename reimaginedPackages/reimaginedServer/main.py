from reimaginedPackages.reimaginedOpenAI.openAIRequester import OpenAIWrapper

from dotenv import load_dotenv as env
import os
env()

token = os.environ.get('ACCESS_TOKEN')

class ChatGPTProcesser:

    def __init__(self):
        self.ChatGPT = OpenAIWrapper(token=token)

    def processData(self, jsonObject):
        prompt = self.ChatGPT.promptGenerator('summary')
        self.ChatGPT.ask(f"{prompt} {jsonObject['content']}")
