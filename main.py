#Импортирование нужных библиотек
import telebot
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Токен бота
bot = telebot.TeleBot('5138000973:AAHl5INx1bFA06VLTvnLtIAEHwlpRnB7Uhw')

# Генерация приветсвия
greetings = ['Привет, ', 'Салют, ', 'Хай, ', 'Приветики-пистолетики, ', 'Приветсвую, ', 'Как жизнь, ']
names = ['сударь', 'чебуречек', 'чел', 'чувак']

# Создание кастомной клавиатуры
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('HELP ME PLS', 'Донатик')
keyboard.row('Предложения по улучшению')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('if/elif/else', 'for', 'while')
keyboard2.row('class', 'def', 'import')
keyboard2.row('2D arrays', 'multiplicity')
keyboard2.row('arrays', 'dictionary', 'strings')
keyboardback = telebot.types.ReplyKeyboardMarkup(True)
keyboardback.row('Назад')
keyexam = telebot.types.ReplyKeyboardMarkup(True)

#Генерация секретного кода
secret_code = random.randint(1000000, 9999999)

@bot.message_handler(commands=['start'])
# Приветствие
def start_message(message):
    bot.send_message(message.chat.id,
                     'P/s это очень ранняя версия бота, поэтому тут много не смешных шуток, граматических ошибок и т.д')
    bot.send_message(message.chat.id,
                     f'{random.choice(greetings) + random.choice(names)}, я крутой бот Глент, помогу тебе вспомнить синтаксис Python',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    
    #Глобальность секретного кода
    global secret_code
    
    #Переобразование сообщения в переменную
    a = message.text
    
    #Переобразование секретного кода из типа int в тип str
    str_secret = str(secret_code)
    
    # Хелп
    if message.text.lower() == 'help me pls':
        bot.send_message(message.chat.id, 'Выберите одну из предложенных конструкций', reply_markup=keyboard2)

    #Предложения по улучшению
    elif message.text.lower() == 'предложения по улучшению':
        bot.send_message(message.chat.id, 'Введите свой адрес электронной почты(мы отошлём вам код для проверки что вы не бот)')
        
    #Отправка кода на почту    
    elif a.find('@') != -1:
        secret_code = random.randint(1000000, 9999999)
        print(a)
        bot.send_message(message.chat.id, 'Если вы правильно указали почту, то вам в течении 1 минуты должен прийти код. Введите его ниже, сделайте пробел и напишите то что вы хотите(обязательно используйте где-нибудь фразу "я хочу.')
        
        # создание экземпляра сообщения
        msg = MIMEMultipart()

        # сообщение
        message = f"{secret_code}"

        # настройка параметров сообщения
        password = "Support1540"
        msg['From'] = "ughackers.team@gmail.com"
        msg['To'] = f"{a}"
        msg['Subject'] = "Code"

        # добавление тела сообщения
        msg.attach(MIMEText(message, 'plain'))

        # создание сервера
        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()

        # логин в системе
        server.login(msg['From'], password)

        # отправление сообщения через сервер
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        print("successfully sent email to %s:" % (msg['To']))
        
    #Подтверждение отправки запроса
    elif str(a).lower().find(str_secret) != -1 and str(a).lower().find("я хочу") != -1:
        bot.send_message(message.chat.id,'Принято и отправлено в общий канал модераторов')
        bot.send_message(-749663206, f'{a.replace(str_secret,"")}')



    # if/elif/else
    elif message.text.lower() == 'if/elif/else':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id, """Конструкция if/elif/else позволяет делать ответвления в ходе программы. Программа уходит в ветку при выполнении определенного условия.
В этой конструкции только if является обязательным, elif и else опциональны:
Проверка if всегда идет первой.
После оператора if должно быть какое-то условие: если это условие выполняется (возвращает True), то действия в блоке if выполняются.
С помощью elif можно сделать несколько разветвлений, то есть, проверять входящие данные на разные условия.
Блок elif это тот же if, но только следующая проверка. Грубо говоря, это «а если …»
Блоков elif может быть много.
Блок else выполняется в том случае, если ни одно из условий if или elif не было истинным.""", reply_markup=keyexam)

    # Примеры if/elif/else
    elif message.text.lower() == 'примеры if/elif/else':
        bot.send_message(message.chat.id, """if age == 15:
    print('Если 15 лет')
elif age == 32:
    print('Иначе если 32 года')
else:
    print('Иначе')""", reply_markup=keyboardback)

    # Назад
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Возварщаю вас назад', reply_markup=keyboard2)

    # for
    elif message.text.lower() == 'for':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id, """Цикл for в языке программирования Python предназначен для перебора элементов структур данных и некоторых других объектов. Это не цикл со счетчиком, каковым является for во многих других языках.
Что значит перебор элементов? Например, у нас есть список, состоящий из ряда элементов. Сначала берем из него первый элемент, затем второй, потом третий и так далее. С каждым элементом мы выполняем одни и те же действия в теле for. Нам не надо извлекать элементы по их индексам и заботиться, на каком из них список заканчивается, и следующая итерация бессмысленна. Цикл for сам переберет и определит конец.""",
                         reply_markup=keyexam)

    # Примеры for
    elif message.text.lower() == 'примеры for':
        bot.send_message(message.chat.id, """spisok = [10, 40, 20, 30]
for element in spisok:
    print(element + 2)""", reply_markup=keyboardback)

    # while
    elif message.text.lower() == 'while':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id,
                         """Цикл while (“пока”) позволяет выполнить одну и ту же последовательность действий, пока проверяемое условие истинно. Условие записывается до тела цикла и проверяется до выполнения тела цикла. Как правило, цикл while используется, когда невозможно определить точное значение количества проходов исполнения цикла.""",
                         reply_markup=keyexam)

    # Примеры while
    elif message.text.lower() == 'примеры while':
        bot.send_message(message.chat.id, """i = 1
while i <= 10:
    print(i ** 2)
    i += 1
""", reply_markup=keyboardback)

    # class
    elif message.text.lower() == 'class':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id, """Класс — тип, описывающий устройство объектов. Объект — это экземпляр класса. Класс можно сравнить с чертежом, по которому создаются объекты.
Python соответствует принципам объектно-ориентированного программирования. В python всё является объектами - и строки, и списки, и словари, и всё остальное.
Но возможности ООП в python этим не ограничены. Программист может написать свой тип данных (класс), определить в нём свои методы.
Это не является обязательным - мы можем пользоваться только встроенными объектами. Однако ООП полезно при долгосрочной разработке программы несколькими людьми, так как упрощает понимание кода.""",
                         reply_markup=keyexam)

    # Примеры class
    elif message.text.lower() == 'примеры class':
        bot.send_message(message.chat.id, """
class Employee:   
    emp_count = 0  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Employee.empCount += 1  
    def display_count(self):  
        print('Всего сотрудников: %d' % Employee.empCount)  
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))  
print("Employee.__doc__:", Employee.__doc__)  
print("Employee.__name__:", Employee.__name__)  
print("Employee.__module__:", Employee.__module__)  
print("Employee.__bases__:", Employee.__bases__)  
print("Employee.__dict__:", Employee.__dict__) """, reply_markup=keyboardback)

    # def
    elif message.text.lower() == 'def':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id,
                         """Функция в python - объект, принимающий аргументы и возвращающий значение. Обычно функция определяется с помощью инструкции def.""",
                         reply_markup=keyexam)

    # Примеры def
    elif message.text.lower() == 'примеры def':
        bot.send_message(message.chat.id, """def newfunc(n):
   def myfunc(x):
    return x + n
    return myfunc""", reply_markup=keyboardback)

    # import
    elif message.text.lower() == 'import':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id, """Модулем в Python называется любой файл с программой (да-да, все те программы, которые вы писали, можно назвать модулями). В этой статье мы поговорим о том, как создать модуль, и как подключить модуль, из стандартной библиотеки или написанный вами.
Каждая программа может импортировать модуль и получить доступ к его классам, функциям и объектам. Нужно заметить, что модуль может быть написан не только на Python, а например, на C или C++.""",
                         reply_markup=keyexam)

    # Примеры import
    elif message.text.lower() == 'примеры import':
        bot.send_message(message.chat.id, """import random
        ВНИМАНИЕ: БОЛЬШИНСТВО МОДУЛЕЙ ПЕРЕД ИМПОРТОМ ТРЕБУЮТ ИНСТАЛЯЦИИ В КОНСОЛИ! ПРИМЕР: pip install модуль""",
                         reply_markup=keyboardback)

    # 2D arrays
    elif message.text.lower() == '2d arrays':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id, '2D arrays', reply_markup=keyexam)

    # Примеры 2d arrays
    elif message.text.lower() == 'примеры 2d arrays':
        bot.send_message(message.chat.id, """keys = [[1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]
        ["*", 0, "#"]]

        print(keys[0][1], end ="")""", reply_markup=keyboardback)

    # multiplicity
    elif message.text.lower() == 'multiplicity':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id, 'multiplicity', reply_markup=keyexam)

    # Примеры multiplicity
    elif message.text.lower() == 'примеры multiplicity':
        bot.send_message(message.chat.id, """colors = {"yellow", "green", "red", "blue", "purple"}
    print(color)""", reply_markup=keyboardback)

    # arrays
    elif message.text.lower() == 'arrays':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id, 'arrays', reply_markup=keyexam)

    # Примеры arrays
    elif message.text.lower() == 'примеры arrays':
        bot.send_message(message.chat.id, """from array import *

         my_array = array(i, [1, 2, 3, 4])

         for i in my_array:
            print(i)""", reply_markup=keyboardback)

    # dictionary
    elif message.text.lower() == 'dictionary':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id, 'dictionary', reply_markup=keyexam)

    # Примеры dictionary
    elif message.text.lower() == 'примеры dictionary':
        bot.send_message(message.chat.id, """solar_system = {"Jupiter": 1321,
        "Mars": 0.15,
        "Saturn": 764}

        print(solar_system["Saturn"])""", reply_markup=keyboardback)

    # strings
    elif message.text.lower() == 'strings':
        keyexam = telebot.types.ReplyKeyboardMarkup(True)
        keyexam.row(f'Примеры {message.text.lower()}')
        bot.send_message(message.chat.id, 'strings', reply_markup=keyexam)

    # Примеры strings
    elif message.text.lower() == 'примеры strings':
        bot.send_message(message.chat.id, "пример", reply_markup=keyboardback)

    # Донатик
    elif message.text.lower() == 'донатик':
        try:
            bot.send_photo(message.chat.id, 'https://i.ibb.co/pQbnQb6/photo-2022-02-01-20-44-26.jpg')
        except Exception as error:
            bot.send_message(message.chat.id, 'ошибка')
            bot.send_message(message.chat.id, error)
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')


bot.polling()
