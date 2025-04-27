from common import add_todo, get_todos

def run(driver, state):
    add_todo(driver, "QA 연습하기")
    todos = get_todos(driver)
    assert any("QA 연습하기" in t.text for t in todos), "TC001 실패: 할 일이 추가되지 않음"
    state['todos'] = todos