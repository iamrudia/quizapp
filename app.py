import os
from flask import Flask, render_template, request
import json

app = Flask(__name__, template_folder='templates')

# 퀴즈 데이터 불러오기
try:
    with open("quiz_data.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
except FileNotFoundError:
    print("❌ quiz_data.json 파일을 찾을 수 없습니다!")
    questions = []

scores = []

@app.route("/")
def index():
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    answers = request.form.getlist("answer")
    score = 0
    for i, q in enumerate(questions):
        if answers[i] == q["answer"]:
            score += 1
    scores.append({"name": name, "score": score})
    return f"{name}님의 점수: {score}/{len(questions)}"

@app.route("/teacher")
def teacher():
    return render_template("teacher.html", scores=scores)

if __name__ == "__main__":
    app.run(debug=True)
