<h1 align="center">🫀Health Log With Flask</h1>
<div align="center" >
  Next.js로 기획 및 개발된 프로젝트를 Flask와 Jinja2로 다시 개발한 혈당 및 혈압 관리를 도와주는 웹앱입니다.<br />
  <a href="https://github.com/hyoni0817/health-log">Next.js로 개발한 코드 보러가기</a>
</div>


## 기능

📊 대시보드에서 DB에 저장된 혈당 및 혈압 수치를 기반으로 현재 건강 상태와 추이를 한눈에 파악할 수 있습니다(현재는 혈당 추이만 확인할 수 있습니다).   

**<p align="center">🚀 이 외에도 다양한 기능이 계속 추가될 예정입니다 🚀</p>**

## 기술

- 코어: Flask, Jinja2, Python, Javascript, HTML
- 스타일링: SCSS
- 패키지 매니저: NPM

## 스크린샷

<img width="3024" height="2344" alt="image" src="https://github.com/user-attachments/assets/7db64a0e-9655-4c42-a253-9792d6373967" />


## 데모 사이트

🏠 [Health Log With Flask로 이동하기](http://13.125.229.209:4000/)

## 실행

1. 프로젝트의 루트 경로에 아래 내용이 포함된 .env 파일을 생성합니다.

```
SUPABASE_URL="SUPABASE에서_제공하는_URL"
SUPABASE_ANON_KEY="SUPABASE에서_발급받은_ANON_KEY"
```

2. 터미널에 아래 명령어를 순서대로 실행하면 Health Log를 실행하실 수 있습니다.

```
pip install flask (설치되어있으면 생략 가능)
pip install supabase python-dotenv
npm run flask:start
```

## 블로그 기록

✨ [블로그 기록 보러가기](https://dev-sisun.tistory.com/category/%EA%B0%9C%EB%B0%9C%20%EC%A7%80%EC%8B%9D/Flask%EC%99%80%20Jinja2)  
Flask와 Jinja2를 사용하여 프로젝트를 진행하면서 설치 과정을 가볍게 블로그로 기록하며 지식을 습득했습니다.

