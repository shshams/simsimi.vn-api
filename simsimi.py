from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SIMSIMI_API_URL = 'https://api.simsimi.vn/v1/simtalk'
API_KEY = ''  # Replace with your actual API key

@app.route('/api/v2/', methods=['GET'])
def simtalk():
    text = request.args.get('message')
    lc = request.args.get('lang', 'en')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'text': text,
        'lc': lc,
    }

    response = requests.post(SIMSIMI_API_URL, headers=headers, data=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2100)
