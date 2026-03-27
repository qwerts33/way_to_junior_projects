def to_do_list():
    while True:
        print("1 - Добавить задачу \n2 - Показать все задачи \n3 - Удалить задачу\n4 - Выход")
        while True:
            try:
                choice = int(input())
            except ValueError:
                print("Введите число")
                continue
            if choice in [1,2,3,4]:
                break
        if choice == 1:
            print("Введите задачу")
            task = input()
            tasks.append(task)
        elif choice == 2:
            if not tasks:
                print("Список пуст")
                continue
            for i, task in enumerate(tasks,1):
                print(i, task)
        elif choice == 3:
            if not tasks:
                print("Список пуст")
                continue
            for i, task in enumerate(tasks,1):
                print(i, task)
            print("Выберите задачу для удаления")
            while True:
                try:
                    w = int(input())
                except ValueError:
                  print("Введите число")
                  continue
                if w in [x for x in range(1,i+1)]:
                    tasks.pop(w)
                    break
        else:
            return
tasks =[]
to_do_list(tasks)