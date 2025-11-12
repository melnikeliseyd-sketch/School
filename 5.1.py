# 5.1 дз
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
    print(f"Добавлено: {task}")
#удалить задачу
def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Удалено: {removed}")
    except IndexError:
        print("Нет задачи с таким номером.")

while True:
    command = input("\nВведите команду (add/delete/show/exit/): ").strip()

    if command == "add":
        task = input("Введите задачу: ")
        add_task(task)
    elif command == "show":
        show_tasks()
    elif command == "delete":
        num = int(input("Введите номер задачи для удаления: "))
        delete_task(num)
    elif command == "exit":
        break
