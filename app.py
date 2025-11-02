from flask import Flask, render_template, request

from utils.blood_pressure.status import (
    get_blood_pressure_status,
    get_blood_pressure_status_label,
)
from utils.blood_sugar.status import (
    get_blood_sugar_status,
    get_blood_sugar_status_label,
)

# Flask 웹 애플리케이션 생성
app = Flask(__name__)


@app.context_processor
def inject_current_path():
    return {"currentPath": request.path}


# 루트 경로로 접근했을 때
@app.route("/")
def home():
    blood_sugar_status = get_blood_sugar_status(100, "BEFORE", "30")
    blood_sugar_status_label = get_blood_sugar_status_label(blood_sugar_status)

    blood_pressure_status = get_blood_pressure_status(100, 60)
    blood_pressure_status_label = get_blood_pressure_status_label(blood_pressure_status)

    return render_template(
        "index.html",
        blood_sugar_status=blood_sugar_status,
        blood_sugar_status_label=blood_sugar_status_label,
        blood_pressure_status=blood_pressure_status,
        blood_pressure_status_label=blood_pressure_status_label,
    )


if __name__ == "__main__":
    app.run(
        "0.0.0.0", port=4000, debug=True
    )  # Flask 애플리케이션 실행 및 디버그 모드 활성화
