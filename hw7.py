'''   Настав час об'єднати наші попередні домашні завдання в одне.
Зараз ми нарешті ми об'єднаємо попередні домашні завдання в один функціональний проєкт. Сьогодні ти навчишся:
• Створенню класу Birthday з можливістю додавання поля для дня народження до контакту 
• Підтримці нового списку команд, включаючи обробку додавання та показу дня народження для контактів. 
• Коректному закриттю програми після виконання команди close або exit
Формат здачі: Розмістіть файли з розв'язанням у репозиторії goit-core-hw-07, та прикріпіть лінки до них у відповідь на домашнє завдання.
Поїхали!🚀
Ми продовжимо робити консольного бота помічника. Настав час об'єднати наші попередні домашні завдання в одне.
По перше додамо додатковий функціонал до класів з попередньої домашньої роботи:
Додайте поле birthday для дня народження в клас Record . Це поле має бути класу Birthday. Це поле не обов'язкове, але може бути тільки одне.
class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
Додайте функціонал роботи з Birthday у клас Record, а саме функцію add_birthday, яка додає день народження до контакту.
Додайте функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
Додайте та адаптуйте до класу AddressBook нашу функцію з четвертого домашнього завдання, тиждень 3, get_upcoming_birthdays, яка для контактів адресної книги повертає список користувачів,
яких потрібно привітати по днях на наступному тижні.
Тепер ваш бот (4 домашнє завдання тиждень 5) повинен працювати саме з функціоналом класу AddressBook. Це значить, що замість словника contacts ми використовуємо book = AddressBook()
Для реалізації нового функціоналу також додайте функції обробники з наступними командами:
add-birthday - додаємо до контакту день народження в форматі DD.MM.YYYY
show-birthday - показуємо день народження контакту
birthdays - повертає список користувачів, яких потрібно привітати по днях на наступному тижні
@input_error
def add_birthday(args, book):
    # реалізація
@input_error
def show_birthday(args, book):
    # реалізація
@input_error
def birthdays(args, book):
    # реалізація
Тож в фіналі наш бот повинен підтримувати наступний список команд:
add [ім'я] [телефон]: Додати новий контакт з іменем та телефонним номером.
change [ім'я] [новий телефон]: Змінити телефонний номер для вказаного контакту.
phone [ім'я]: Показати телефонний номер для вказаного контакту.
all: Показати всі контакти в адресній книзі.
add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
show-birthday [ім'я]: Показати дату народження для вказаного контакту.
birthdays: Показати дні народження, які відбудуться протягом наступного тижня.
hello: Отримати вітання від бота.
close або exit: Закрити програму.

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # реалізація

        elif command == "change":
            # реалізація

        elif command == "phone":
            # реалізація

        elif command == "all":
            # реалізація

        elif command == "add-birthday":
            # реалізація

        elif command == "show-birthday":
            # реалізація

        elif command == "birthdays":
            # реалізація

        else:
            print("Invalid command.")
Критерії оцінювання:
Реалізувати всі вказані команди до бота
Всі дані повинні виводитися у зрозумілому та зручному для користувача форматі
Всі помилки, такі як неправильний ввід чи відсутність контакту, повинні оброблятися інформативно з відповідним повідомленням для користувача
Валідація даних:
Дата народження має бути у форматі DD.MM.YYYY.
Телефонний номер має складатися з 10 цифр.
Програма повинна закриватися коректно після виконання команд close або exit  
'''  
'''
Chat GPT
'''
'''   
Давайте реалізуємо необхідні зміни та функції обробники для бота:
1. Додайте поле birthday для дня народження в клас Record та клас Birthday:
'''
'''
from datetime import datetime

class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних та перетворіть рядок на об'єкт datetime
            date_obj = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(date_obj)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

'''        
'''
2. Додайте функції обробники для бота:
'''
'''
@input_error
def add_birthday(args, book):
    if len(args) == 2:
        name, birthday = args
        record = book.find(name)
        if record:
            record.birthday = Birthday(birthday)
            return f"Birthday added for {name}."
        else:
            raise KeyError("Contact not found.")
    else:
        raise ValueError("Give me name and birthday please.")

@input_error
def show_birthday(args, book):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record and record.birthday:
            return f"{name}'s birthday: {record.birthday}"
        elif record:
            return f"{name} has no birthday set."
        else:
            raise KeyError("Contact not found.")
    else:
        raise ValueError("Enter the argument for the command.")

@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join([f"Upcoming birthday: {entry['name']} on {entry['congratulation_date']}" for entry in upcoming_birthdays])
    else:
        return "No upcoming birthdays."

# Додайте функцію get_upcoming_birthdays до класу AddressBook
def get_upcoming_birthdays(self):
    today = datetime.today().date()
    upcoming_birthdays = []

    for record in self.data.values():
        if record.birthday:
            birthday = record.birthday.value.replace(year=today.year)

            if birthday < today:
                birthday = birthday.replace(year=today.year + 1)

            days_until_birthday = (birthday - today).days

            if 0 <= days_until_birthday <= 7:
                if birthday.weekday() in [5, 6]:  # 5: Saturday, 6: Sunday
                    monday = today + timedelta(days=(7 - today.weekday()) + 1)
                    congratulation_date = monday.strftime("%d.%m.%Y")
                else:
                    congratulation_date = birthday.strftime("%d.%m.%Y")

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date
                })

    return upcoming_birthdays
'''
'''
3. Оновіть головну функцію main для бота:
'''
'''
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            # Реалізація
        elif command == "change":
            # Реалізація
        elif command == "phone":
            # Реалізація
        elif command == "all":
            # Реалізація
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
'''
'''
Ці зміни додають функціонал для роботи з днями народженнями в боті та враховують вимоги/
'''

