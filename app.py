from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/checkNumber")
def check_number():

    # 사용자가 보낸 데이터 input_num의 데이터타입을 정수형으로 바꾼다.
    # 정수형으로 바뀐 input_num을 result_num 변수에 저장한다.
    # result_num이 1보다 작다면 "비교할 수 없는 값 입니다" 라는 데이터를
    # "result"에 저장하고 화면으로 함께 전송한다.
    # result_num을 2로 나눴을때, 나머지가 0이라면 짝수고,
    # 그게 아니라면
    # 홀수이다.
    # "짝수" 또는 "홀수" 라는 스트링 데이터를 result라는 변수를 만들어
    # 저장하고, render_template 함수를 통해 화면으로 이동할 때
    # 함께 전송해진다.
    input_num = request.args.get("num")
    result = ""

    result_num = int(input_num)

    if result_num < 1:
        result = "비교 할 수 없는 값"
        return render_template("index.html", msg=result)

    else:
        if result_num % 2 == 0:
            result = "짝수"
            return render_template("index.html", msg=result)
        else:
            result = "홀수"
            return render_template("index.html", msg=result)


app.run(debug=True)
