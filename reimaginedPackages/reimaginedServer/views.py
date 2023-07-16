from flask import Flask, request
from reimaginedPackages.reimaginedServer.main import ChatGPTProcesser 

app = Flask(__name__)

# JSON object recieving test is needed
# See: https://flask.palletsprojects.com/en/2.3.x/testing/
@app.route('/send', methods=['POST'])
def catch():
    sourceData = request.get_json()
    if not sourceData:
        return "No data to process."
    
    response = ChatGPT.processData(sourceData)
    return f"{response}"

# TODO: handle the Access Token AKA login session from chat.openai.com
@app.route('/api', methods=['POST'])
def set_api():
    return "all settled!"


if __name__ == '__main__':
    ChatGPT = ChatGPTProcesser()
    app.run(debug=True, port=5000)

