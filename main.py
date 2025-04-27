import time
import datetime
import os  # 추가
from common import get_driver

# 테스트 케이스 import
from tests import (
    tc001_add_todo,
    tc002_blank_todo,
    tc003_complete_todo,
    tc004_delete_todo,
    tc005_filter_completed,
)

URL = "https://todomvc.com/examples/react/dist/"

def timestamp():
    # 현재 시각을 문자열로 반환 (스크린샷 파일명 등에 사용)
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def save_screenshot(driver, name):
    # screenshot 디렉토리 없으면 생성
    os.makedirs("screenshot", exist_ok=True)
    path = f"screenshot/{name}.png"
    driver.save_screenshot(path)

# 테스트 케이스 목록 (이름, 함수)
test_cases = [
    ("[TC001] 할 일 추가", tc001_add_todo.run),
    ("[TC002] 공백 입력", tc002_blank_todo.run),
    ("[TC003] 완료 처리", tc003_complete_todo.run),
    ("[TC004] 삭제 기능", tc004_delete_todo.run),
    ("[TC005] 필터 기능", tc005_filter_completed.run),
]

def main():
    results = []  # 각 TC의 결과를 저장할 리스트
    state = {}    # TC 간 공유 상태(할 일 목록, 첫 항목 등)
    driver = get_driver()
    try:
        try:
            driver.get(URL)
            time.sleep(1)
        except Exception as e:
            # URL 접근 실패 시 스크린샷 저장 및 에러 메시지 출력 후 종료
            save_screenshot(driver, f"fail_URL_access_{timestamp()}")
            print(f"[URL 접근 실패] {URL}\n에러: {e}")
            results.append(f"[URL 접근 실패] {e}")
            return  # 테스트 중단

        for name, func in test_cases:
            print(f"{name} 테스트 실행 중...")
            try:
                func(driver, state)  # TC 함수 실행
                results.append(f"{name} 성공")
            except Exception as e:
                # 실패 시 스크린샷 저장 및 결과 기록
                save_screenshot(driver, f"fail_{name.replace(' ', '_')}_{timestamp()}")
                print(f"{name} 실패: {e}")
                results.append(f"{name} 실패: {e}")
                driver.refresh()  # 페이지 새로고침으로 상태 초기화
                time.sleep(1)
                state.clear()     # 상태 딕셔너리도 초기화
    finally:
        driver.quit()
        print("\n--- 테스트 결과 요약 ---")
        for r in results:
            print(r)

if __name__ == "__main__":
    main() 