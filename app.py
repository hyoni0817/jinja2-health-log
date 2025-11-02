from flask import Flask, render_template, request

# Flask 웹 애플리케이션 생성
app = Flask(__name__)


@app.context_processor
def inject_current_path():
    return {"currentPath": request.path}


# 루트 경로로 접근했을 때
@app.route("/")
def home():
    position = "프론트엔드"

    return render_template("index.html", position=position)


if __name__ == "__main__":
    app.run(
        "0.0.0.0", port=4000, debug=True
    )  # Flask 애플리케이션 실행 및 디버그 모드 활성화
