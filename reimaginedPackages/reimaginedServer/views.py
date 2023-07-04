from flask import Flask, request
from main import ChatGPTProcesser 

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def catch():
    sourceData = request.get_json()
    if not sourceData:
        return "No data to process."
    
    ChatGPT.processData(sourceData)
    return "Processed successfully." 

if __name__ == '__main__':
    ChatGPT = ChatGPTProcesser()
    app.run(debug=True, port=5000)

