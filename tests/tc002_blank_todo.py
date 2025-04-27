from common import add_todo, get_todos

def run(driver, state):
    todos = state.get('todos', [])
    add_todo(driver, "   ")
    todos_after = get_todos(driver)
    assert len(todos_after) == len(todos), "DEF-001: 공백 입력 시 빈 항목이 추가됨"