from selenium.webdriver.common.by import By
from common import get_todos
import time

def run(driver, state):
    first = state.get('first')
    driver.execute_script("arguments[0].scrollIntoView()", first)
    driver.execute_script("arguments[0].style.visibility='visible';", first.find_element(By.CSS_SELECTOR, "button.destroy"))
    first.find_element(By.CSS_SELECTOR, "button.destroy").click()
    time.sleep(1)
    assert not any("QA 연습하기" == t.text for t in get_todos(driver)), "TC004 실패: 항목이 삭제되지 않음"