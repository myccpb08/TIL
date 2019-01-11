from flask import Flask
app = Flask(__name__)

@app.route("/")     # @ 는 데코레이터 의미
def hello():        # 위 주소로 들어갔을 때, 실행될 함수
    return "Hello World!"   # 라우트라는 메소드를 실행할 때, hello 함수를 같이 넘김?

@app.route("/python")    # 다른 페이지 만들기
def phtyon():
    return 'Python is fun!'

@app.route("/dictionary/<string:word>") # <> 는 variable routing 의미
								# word 는 string 만 가능함을 의미
    						# word 에 무엇을 넣든 같은 페이지 보여줌
def dictionary(word):
    dictionary = {
        'apple':'사과',
        'banana':'바나나',
        'pear':'배',
        'watermelon':'수박'
    }
    result = dictionary.get(word,'나만의 단어장에 없는 단어입니다')  # dictionary[] 하지 않는 이유는, [] 안에 key 가 없으면 오류나니까
                        # get 은 없으면 None 주니까 안전
    return f'{word}은(는) {result}!'