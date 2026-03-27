import json
import os

def write():
    phone_notebook(notebook)
    json.dump(notebook, open("notebook.json", "w"))

def phone_notebook(notebook):
    print("\nДобро пожаловать! Выберите команду ниже:")
    while True:
            print("1 - Добавить контакт")
            print("2 - Найти номер по имени")
            print("3 - Удалить контакт")
            print("4 - Показать все контакты")
            print("5 - Выход\n")

            while True:
                try:
                    choice = int(input())
                except ValueError:
                    print("Введите цифру\n")
                    continue
                if choice not in [1,2,3,4,5]:
                    print("Введите цифру от 1 до 5\n")
                    continue
                else:
                    break

            if choice == 1:
                print("Введите контакт: Имя и Номер")
                name = input()
                number = input()
                notebook[name] = number

            elif choice == 2:

                print("Введите имя:")
                name = input()

                if name in notebook:
                    print(f"Номер для {name} - {notebook[name]}")
                else:
                    print("Имя не найдено")

            elif choice == 3:

                print("Введите имя контакта для удаления")
                name = input()
                if name in notebook:
                    del notebook[name]
                    continue
                else:
                    print("Имя не найдено")

            elif choice == 4:

                if notebook:
                    for name, number in notebook.items():
                        print(name, number)
                else:
                    print("Книжка пуста")
            else:
                return

filename = "notebook.json"
notebook = {}
if os.path.exists(filename):
    try:
        with open(filename) as f:
            notebook = json.load(f)

    except json.decoder.JSONDecodeError:
        pass
write()
