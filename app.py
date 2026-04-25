    from flask import Flask, render_template, request, redirect
... import json
... 
... app = Flask(__name__)
... 
... # 퀴즈 데이터 불러오기 (샘플 JSON)
... with open("quiz_data.json", "r", encoding="utf-8") as f:
...     questions = json.load(f)
... 
... # 학생 점수 저장용 (간단히 메모리 DB, 실제는 PostgreSQL 사용 권장)
... scores = []
... 
... @app.route("/")
... def index():
...     return render_template("index.html", questions=questions)
... 
... @app.route("/submit", methods=["POST"])
... def submit():
...     name = request.form.get("name")
...     answers = request.form.getlist("answer")
...     score = 0
...     for i, q in enumerate(questions):
...         if answers[i] == q["answer"]:
...             score += 1
...     scores.append({"name": name, "score": score})
...     return f"{name}님의 점수: {score}/{len(questions)}"
... 
... @app.route("/teacher")
... def teacher():
...     return render_template("teacher.html", scores=scores)
... 
... if __name__ == "__main__":
...     app.run(debug=True)
