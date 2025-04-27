from selenium.webdriver.common.by import By

def run(driver, state):
    todos = state.get('todos', [])
    first = todos[0]
    first.find_element(By.CSS_SELECTOR, "input.toggle").click()
    assert "completed" in first.get_attribute("class"), "TC003 실패: 완료 표시 안됨"
    state['first'] = first