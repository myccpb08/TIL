from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ssafy")                 # 새로운 페이지 만들기
def ssafy():
    return "This is SSAFY"           # 수정했으면 terminal 에서 ctrl+c 해서 종료 시킨 후 재실행

@app.route("/greeting/<string:name>")    # <자료형: 변수의 이름>  
def greeting(name):
    return f'반갑습니다! {name}님'       # 주소창에 greeting/김 이라 치면 반갑습니다 김님 출력

@app.route("/cube/<int:num>")
def cube(num) :
    cube = num**3
    return str(cube)        # flask 는 return 으로 정수형을 못 받아서 문자열로 바꿔줘야 함

@app.route("/lunch/<int:person>")
def lunch(person):
    menu = ["짬뽕","불닭볶음면","까르보불닭","죠리퐁","새우깡"]
    #person = int(person)
    order = random.sample(menu,person)
    return str(order)

@app.route("/html")
def html():
    multiline_string = '''
            <h1>이것은 h1입니다!</h1>
            <p>여기는 p입니다 </p>
            
    '''
    return multiline_string

@app.route("/html_file")        #html 파일 읽어서 페이지 만듦
def html_file():
    return render_template('html_file.html')

@app.route("/hi/<string:name>")
def hi(name):
    return render_template('hi.html', name=name)

@app.route("/fake_naver")
def fake_naver():
    return render_template('fake_naver.html')