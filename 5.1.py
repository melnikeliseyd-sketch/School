# 5.1 дз
import json
import os
FILENAME = "tasks.json"
tasks = []

#сохранение/загрузка
def save_tasks():
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    print("Задачи сохранены.")

def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            tasks = json.load(f)
        print("Задачи загружены.")
    else:
        tasks = []

#показать задачи
def show_tasks():
    if not tasks:
        print("Список пуст.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# добавить задачу
def add_task(task):
    tasks.append(task)
    save_tasks()
    print(f"Добавлено: {task}")
#удалить задачу
def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        save_tasks()
        print(f"Удалено: {removed}")
    except IndexError:
        print("Нет задачи с таким номером.")
#отметка выполнения задачи
def mark_done(index):
    try:
        tasks[index - 1] = tasks[index - 1] + " (выполнено)"
        save_tasks()
        print("Задача отмечена как выполненная.")
    except IndexError:
        print("Нет задачи с таким номером.")
load_tasks()

while True:
    command = input("\nВведите команду (add/delete/done/show/exit/): ").strip()

    if command == "add":
        task = input("Введите задачу: ")
        add_task(task)
    elif command == "show":
        show_tasks()
    elif command == "delete":
        num = int(input("Введите номер задачи для удаления: "))
        delete_task(num)
    elif command == "done":
        num = int(input("Введите номер задачи для отметки: "))
        mark_done(num)
    elif command == "exit":
        break
