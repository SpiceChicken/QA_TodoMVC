from common import add_todo, get_todos, filter_selector
from selenium.webdriver.common.by import By
import time

def run(driver, state):
    # "Filter Test"라는 할 일을 추가
    add_todo(driver, "Filter Test")
    # 방금 추가한 항목을 완료 처리
    new = get_todos(driver)[-1]
    new.find_element(By.CSS_SELECTOR, "input.toggle").click()
    # "Completed" 필터 클릭
    filter_selector(driver, "Completed").click()
    time.sleep(1)
    # 필터링된 목록이 모두 "Filter Test"인지 확인
    filtered = get_todos(driver)
    assert all("Filter Test" in t.text for t in filtered), "TC005 실패: 필터링 동작 이상" 