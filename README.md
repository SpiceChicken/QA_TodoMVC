# QA 포트폴리오 - TodoMVC 테스트 프로젝트

## 📌 프로젝트 소개
- 테스트 대상: [TodoMVC - React Example](https://todomvc.com/examples/react/dist/)
  - TodoMVC GitHub: https://github.com/tastejs/todomvc
- 목표: 수동 테스트 케이스 설계 및 Selenium을 활용한 테스트 자동화 수행

## 프로젝트 구조
```
qa_todomvc_project/
├── screenshot/ (테스트 실패 스크린샷)
├── tests/ (Selenium 테스트 케이스)
├── requirements.txt
├── common.py (Selenium Action)
└── main.py
```

## 📋 수행 항목
1. 수동 테스트 케이스 작성
2. 테스트 자동화 스크립트 개발 (Python + Selenium)
3. 테스트 실패 시 스크린샷 저장 및 로깅 처리

## 실행 방법
1. 패키지 설치
    ```
    pip install -r requirements.txt
    ```
2. 테스트 실행
    ```
    python .\main.py
    ```

## 기술 스택
- Python 3.12.2
- Selenium
- ChromeDriver 최신 버전