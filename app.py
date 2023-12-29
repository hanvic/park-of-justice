import requests
import json
import os
from flask import Flask, render_template, request

API_HOST = os.environ.get('API_HOST','https://j5juzhoitxi4kmbssppblaq63u0jgcau.lambda-url.ap-northeast-2.on.aws')
API_KEY = os.environ.get('API_KEY','test')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('search.html')


@app.route('/search', methods=['POST'])
def search_number():

    req = request.form
    car_number = req['number']
    response = requests.get(API_HOST, {'car': car_number, 'key': API_KEY})

    info = {"status":False, 'cnt':0}
    if response.status_code == 200:  # 요청 성공
        info = json.loads(response.text)

    else:  # 요청 실패

        print('실패 상태 코드:', response.status_code)

    return render_template('search_result.html', infos={'req': req, 'info': info})


if __name__ == '__main__':
    app.run()
