from random import *
import json
plans = {}

def save():
    with open('plans.json','w', encoding ="utf-8" )as file:
            json.dump(plans, file)
            print("Ваши планы сохранены")

def load():
    global plans
    with open('plans.json','r',encoding ="utf-8")as file:
            plans = json.load(file)
            save()
            print("Ваши планы и праздники загружены")
            print(plans)

def delete():
    try:
        key_to_del = input("Введите дату, которую хотите удалить: ")
        del plans[key_to_del]
        print("Событие удалено")
    except:
        print("Такой даты нет в календаре.")
while True:
    command =input("Введите команду: ")
    if command == "/start":
        print("Привет, это планер-бот. Здесь ты можешь записывать свои планы, дела, праздники в календарь и просматривать их в удобном формате!")
    elif command == "/load":
        load()
    elif command == "/show_all":
        print("Текущий словарь:")
        print(plans)
    elif command == "/stop":
        save()
        print("Bye-bye")
        break
    elif command == "/add_day":
        key = input("Введите день: ")
        value = input("Введите планы на этот день: ")
        plans[key] = value
        save()
    elif command == "/delete":
        delete()
    elif command == "/help":
        print("/start - начало работы бота \n/load - загрузка данных из файла(внешнее хранилище)\n/show_all - показать текущие планы\n/stop - прекращение работы бота\n/add_day - добавление нового плана в календарь\n/delete - удаление события")
    else:
        print("Неопознанная команда. Посмотрите список команд бота через /help")
        