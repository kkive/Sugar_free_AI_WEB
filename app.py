#app.py
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/test',methods=['get','post'])




def hello_world():
    import os
    import openai
    account = request.args.get("ask")
#     openai.api_key="你的OpenAI-API"
    openai.api_key=""
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=account,
        temperature=0,
        max_tokens=1024,  #  官方为7，建议1024，大小影响答案次数
        )
    return (response.choices[0].text).strip()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
