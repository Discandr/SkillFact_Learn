clients = [
    {"name": "Иван Петров", "balance": 50.0},

    {"name": "Василий Кунц", "balance": 136.0}
]

from task_c1_10_3 import Clients
c1 = input("Введите Имя и Фамилию клиента:")
flag = False
for d in clients:
    if c1 == d.get("name"):
        flag = True
        name = d.get("name")
        balance = d.get("balance")
        info = Clients(name, balance)
        break

    else:
        continue

if  flag:
    print(info.get_balance())
else:
    print("Клиент не найден. Попробуйте ещё раз.")

