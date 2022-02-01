import telebot
import random

bot = telebot.TeleBot('5138000973:AAHl5INx1bFA06VLTvnLtIAEHwlpRnB7Uhw')

greetings = ['Привет, ', 'Салют, ', 'Хай, ', 'Приветики-пистолетики, ']
names = ['сударь', 'чебуречек']
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('HELP ME PLS', 'Донатик')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('if/elif/else', 'for', 'while')
keyboard2.row('class', 'def', 'import')
keyboardback = telebot.types.ReplyKeyboardMarkup(True)
keyboardback.row('Назад')
keyboardelif = telebot.types.ReplyKeyboardMarkup(True)
keyboardelif.row('Примеры if/elif/else')
keyboardfor = telebot.types.ReplyKeyboardMarkup(True)
keyboardfor.row('Примеры for')
keyboardwhile = telebot.types.ReplyKeyboardMarkup(True)
keyboardwhile.row('Примеры while')
keyboardclass = telebot.types.ReplyKeyboardMarkup(True)
keyboardclass.row('Примеры class')
keyboarddef = telebot.types.ReplyKeyboardMarkup(True)
keyboarddef.row('Примеры def')
keyboardimport = telebot.types.ReplyKeyboardMarkup(True)
keyboardimport.row('Примеры import')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'P/s это очень ранняя версия бота, поэтому тут много не смешных шуток, граматических ошибок и т.д')
    bot.send_message(message.chat.id,
                     f'{random.choice(greetings) + random.choice(names)}, я крутой бот Глент, помогу тебе вспомнить синтаксис Python, для тупых: help',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'help me pls':
        bot.send_message(message.chat.id, 'Выберите одну из предложенных конструкций', reply_markup=keyboard2)

    elif message.text.lower() == 'if/elif/else':
        bot.send_message(message.chat.id, """Конструкция if/elif/else позволяет делать ответвления в ходе программы. Программа уходит в ветку при выполнении определенного условия.

В этой конструкции только if является обязательным, elif и else опциональны:

Проверка if всегда идет первой.
После оператора if должно быть какое-то условие: если это условие выполняется (возвращает True), то действия в блоке if выполняются.
С помощью elif можно сделать несколько разветвлений, то есть, проверять входящие данные на разные условия.
Блок elif это тот же if, но только следующая проверка. Грубо говоря, это «а если …»
Блоков elif может быть много.
Блок else выполняется в том случае, если ни одно из условий if или elif не было истинным.""", reply_markup=keyboardelif)
    elif message.text.lower() == 'примеры if/elif/else':
        bot.send_message(message.chat.id, """if age == 15:
    print('Если 15 лет')
elif age == 32:
    print('Иначе если 32 года')
else:
    print('Иначе')""", reply_markup=keyboardback)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Возварщаю вас назад', reply_markup=keyboard2)
    elif message.text.lower() == 'for':
        bot.send_message(message.chat.id, """Цикл for в языке программирования Python предназначен для перебора элементов структур данных и некоторых других объектов. Это не цикл со счетчиком, каковым является for во многих других языках.

Что значит перебор элементов? Например, у нас есть список, состоящий из ряда элементов. Сначала берем из него первый элемент, затем второй, потом третий и так далее. С каждым элементом мы выполняем одни и те же действия в теле for. Нам не надо извлекать элементы по их индексам и заботиться, на каком из них список заканчивается, и следующая итерация бессмысленна. Цикл for сам переберет и определит конец.""",
                         reply_markup=keyboardfor)
    elif message.text.lower() == 'примеры for':
        bot.send_message(message.chat.id, """spisok = [10, 40, 20, 30]
for element in spisok:
    print(element + 2)""", reply_markup=keyboardback)

    elif message.text.lower() == 'while':
        bot.send_message(message.chat.id,
                         """Цикл while (“пока”) позволяет выполнить одну и ту же последовательность действий, пока проверяемое условие истинно. Условие записывается до тела цикла и проверяется до выполнения тела цикла. Как правило, цикл while используется, когда невозможно определить точное значение количества проходов исполнения цикла.""",
                         reply_markup=keyboardwhile)

    elif message.text.lower() == 'примеры while':
        bot.send_message(message.chat.id, """i = 1
while i <= 10:
    print(i ** 2)
    i += 1
""", reply_markup=keyboardback)

    elif message.text.lower() == 'class':
        bot.send_message(message.chat.id, """Класс — тип, описывающий устройство объектов. Объект — это экземпляр класса. Класс можно сравнить с чертежом, по которому создаются объекты.

Python соответствует принципам объектно-ориентированного программирования. В python всё является объектами - и строки, и списки, и словари, и всё остальное.

Но возможности ООП в python этим не ограничены. Программист может написать свой тип данных (класс), определить в нём свои методы.

Это не является обязательным - мы можем пользоваться только встроенными объектами. Однако ООП полезно при долгосрочной разработке программы несколькими людьми, так как упрощает понимание кода.""",
                         reply_markup=keyboardclass)
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
    elif message.text.lower() == 'def':
        bot.send_message(message.chat.id,
                         """Функция в python - объект, принимающий аргументы и возвращающий значение. Обычно функция определяется с помощью инструкции def.""",
                         reply_markup=keyboarddef)
    elif message.text.lower() == 'примеры def':
        bot.send_message(message.chat.id, """def newfunc(n):
   def myfunc(x):
    return x + n
    return myfunc""", reply_markup=keyboardback)
    elif message.text.lower() == 'import':
        bot.send_message(message.chat.id, """Модулем в Python называется любой файл с программой (да-да, все те программы, которые вы писали, можно назвать модулями). В этой статье мы поговорим о том, как создать модуль, и как подключить модуль, из стандартной библиотеки или написанный вами.

Каждая программа может импортировать модуль и получить доступ к его классам, функциям и объектам. Нужно заметить, что модуль может быть написан не только на Python, а например, на C или C++.""",
                         reply_markup=keyboardimport)

    elif message.text.lower() == 'примеры import':
        bot.send_message(message.chat.id, """import random
        ВНИМАНИЕ: БОЛЬШИНСТВО МОДУЛЕЙ ПЕРЕД ИМПОРТОМ ТРЕБУЮТ ИНСТАЛЯЦИИ В КОНСОЛИ! ПРИМЕР: pip install модуль""",
                         reply_markup=keyboardback)

    elif message.text.lower() == 'донатик':
        try:
            bot.send_photo(message.chat.id, photo=open('465549.png', 'rb'))
        except:
            bot.send_message(message.chat.id, 'ошибка')
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')


bot.polling()