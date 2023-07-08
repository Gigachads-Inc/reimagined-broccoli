from reimaginedPackages.reimaginedOpenAI.openAIRequester import OpenAIWrapper
from models import Article

from dotenv import load_dotenv as env
import os
env()

token = os.environ.get('ACCESS_TOKEN')

class ChatGPTProcesser:

    def __init__(self):
        self.ChatGPT = OpenAIWrapper(token=token)

    def processData(self, jsonObject):
        article = Article(jsonObject['title'], jsonObject['content'], jsonObject['flag'])
        prompt = self.ChatGPT.promptGenerator(article.flag)
        response = self.ChatGPT.ask(f"{prompt} {article.content}")
        return response
