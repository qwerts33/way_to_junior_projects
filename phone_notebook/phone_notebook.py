import json
import os

class Notebook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, number):
        self.contacts[name] = number

    def find(self,name):
        if name in self.contacts:
            print(f"Номер для {name} - {self.contacts[name]}")
        else:
            print("Имя не найдено")

    def show(self):
        if self.contacts:
            for name, number in self.contacts.items():
                print(name, number)
        else:
            print("Книжка пуста")

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Имя не найдено")

    def save(self):
        json.dump(self.contacts, open("notebook.json", "w"))

    def load(self):
        if os.path.exists(filename):
            try:
                with open(filename) as f:
                    self.contacts = json.load(f)

            except json.decoder.JSONDecodeError:
                pass


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
                nb.add(name, number)

            elif choice == 2:
                print("Введите имя:")
                name = input()
                nb.find(name)

            elif choice == 3:
                print("Введите имя контакта для удаления")
                name = input()
                nb.delete(name)

            elif choice == 4:
                nb.show()
            else:
                return

filename = "notebook.json"
notebook = {}
nb = Notebook()
nb.load()
phone_notebook(notebook)
nb.save()

