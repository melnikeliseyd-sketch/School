# 5.1 дз
tasks = []


def show_tasks():
    if not tasks:
        print("Список пуст.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(task):
    tasks.append(task)
    print(f"Добавлено: {task}")


while True:
    command = input("\nВведите команду (add/show/exit): ").strip()

    if command == "add":
        task = input("Введите задачу: ")
        add_task(task)
    elif command == "show":
        show_tasks()
    elif command == "exit":
        break
