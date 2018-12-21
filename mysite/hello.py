import os
import random
import requests
from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ping")
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args['name']
    #random
    result = random.choice(["ocean.jpg","2.jpg","image.png"])
    
    return render_template('pong.html',name_in_html=name, result=result)

@app.route('/lotto/<int:num>')    # num = 사용자로부터 받은 회차정보

def lotto(num):
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    response = requests.get(url)
    lotto = response.json()
    
    winner=[]
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])   #> 30
    
    bonus = lotto['bnusNo']   #> 6

    return render_template('lotto.html', w=winner, b=bonus, n=num)



@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    chat_id = os.getenv('CHAT_ID')
    token = os.getenv('TELEGRAM_BOT_TOKEN')

    text = request.args['message']
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return render_template('send.html')