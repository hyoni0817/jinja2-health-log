from flask import Flask, render_template, request

import os
from dotenv import load_dotenv
from supabase import create_client, Client

from utils.blood_pressure.status import (
    get_blood_pressure_status,
    get_blood_pressure_status_label,
)
from utils.blood_sugar.status import (
    get_blood_sugar_status,
    get_blood_sugar_status_label,
)

# 환경 변수 로드
load_dotenv()

# Flask 웹 애플리케이션 생성
app = Flask(__name__)

# Supabase 클라이언트 초기화
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)


@app.context_processor
def inject_current_path():
    return {"currentPath": request.path}


# 루트 경로로 접근했을 때
@app.route("/")
def home():

    try:
        # 혈당 추이
        response = supabase.rpc("get_blood_sugar_trend", {"days": 30}).execute()
        blood_sugar_trend = response.data if response.data else []

        # 최근 혈당 기록
        latest_response = (
            supabase.table("glucose")
            .select("*")
            .order("date", desc=True)
            .limit(1)
            .execute()
        )
        latest_blood_sugar = latest_response.data[0] if latest_response.data else None

        # 최근 혈압 기록
        latest_bp_response = (
            supabase.table("blood_pressure")
            .select("*")
            .order("date", desc=True)
            .limit(1)
            .execute()
        )
        latest_blood_pressure = (
            latest_bp_response.data[0] if latest_bp_response.data else None
        )

    except Exception as e:
        print(f"Supabase RPC 오류: {e}")
        blood_sugar_trend = []

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
        blood_sugar_trend=blood_sugar_trend,
        latest_blood_sugar=latest_blood_sugar,
        latest_blood_pressure=latest_blood_pressure,
    )


if __name__ == "__main__":
    app.run(
        "0.0.0.0", port=4000, debug=True
    )  # Flask 애플리케이션 실행 및 디버그 모드 활성화
