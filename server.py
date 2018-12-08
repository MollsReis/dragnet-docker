from flask import Flask, request
from dragnet import extract_content

app = Flask(__name__)

@app.route('/content', methods=['POST'])
def content():
    return extract_content(request.data)

@app.route('/content-comments', methods=['POST'])
def comments():
    return extract_content_and_comments(request.data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
