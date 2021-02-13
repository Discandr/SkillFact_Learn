class Clients:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return f"Клиент: {self.name}. Баланс: {self.balance} р."

class Guest(Clients):
    def __init__(self, name, city, status):
        super().__init__(self, name)
        self.city = city
        self.status = status

    def getdata_guests(self):
        return f"{name}, г. {self.city}, статус {self.status}"

def personal_data(name, city, status):
    guest_data = []
    guest_data.append(name)
    guest_data.append(city)
    guest_data.append(status)
    return guest_data

list_person = []
v = bool
print("*"*20)
print("Введите данные гостя")
print("*"*20)

while v:
    f = input("Есть данные? (да/нет)\n ")
    if f == "да":
        name = input("Введите имя гостя: \n")
        city = input("Введите город проживания: \n")
        status = input("Введите статус гостя: \n")
        pers = personal_data(name, city, status)
        list_person.append(pers)
        print(list_person)
    elif f == "нет":
        v = False
    else:
       print("Введите еще раз ваш ответ")

print(list_person)

for i in  list_person:
    name = i[0]
    city = i[1]
    status = i[2]
#    print(i[0], i[1], i[2])
    gs_gold = Guest(name, city, status)
    print(gs_gold.getdata_guests())