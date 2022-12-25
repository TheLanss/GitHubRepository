import telebot
import psycopg2
from datetime import date
from telebot import types

token = "5607985345:AAGwbdSi5u1VrVzN1xNBz_iI9BaOBQZ9hcQ"

bot = telebot.TeleBot(token)


conn = psycopg2.connect(database="time_rasp", user="postgres", password="password123",
                        host="localhost", port="5432")
cursor = conn.cursor()

vn_week = date.today() - date(2022,8,22)
vn_week = vn_week.days // 7 % 2

pair1 = '9:30'
pair2 = '11:20'
pair3 = '13:10'
pair4 = '15:25'
pair5 = '17:15'

keyboard = types.ReplyKeyboardMarkup()
keyboard.row("a. Понедельник", "b. Вторник", "c. Среда", "d. Четверг", "e. Пятница")
keyboard.row("f. Расписание на текущую неделю", "g. Расписание на следующую неделю")

def dayrasp(day, plus_week=False):
    global vn_week
    if not vn_week:
        day += 7
    if plus_week:
        day += 7
        day %= 14
    cursor.execute(f"select * from timetable where day = {day};")
    records = list(map(lambda x: x[1:], list(cursor.fetchall())))
    records.sort(key=lambda x: x[3])
    return records



@bot.message_handler(commands=['rasp_on_day'])
def rod(message):
    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, 'Уважаемый пользователь, введите день недели:', reply_markup=keyboard)
    tmp = message.text.split()[1]

    if tmp.lower() == 'понедельник':
        rasp = dayrasp(1)
        forsend = f"{tmp.upper()}\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id,forsend, reply_markup=keyboard)

    if tmp.lower() == 'вторник':
        rasp = dayrasp(2)
        forsend = f"{tmp.upper()}\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)

    if tmp.lower() == 'среда':
        rasp = dayrasp(3)
        forsend = f"{tmp.upper()}\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)

    if tmp.lower() == 'четверг':
        rasp = dayrasp(4)
        forsend = f"{tmp.upper()}\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)

    if tmp.lower() == 'пятница':
        rasp = dayrasp(5)
        forsend = f"{tmp.upper()}\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, """Здравствуйте! Я бот-расписание БФИ2202! \n
Чтобы узнать расписание на текущую неделю, введите: \n f. Расписание на текущую неделю \n
Чтобы узнать расписание на следующую неделю, введите: \n g. Расписание на следующую неделю \n
Для получения ссылки на сайт Московского Технического Университета Связи и Информатики - используйте команду /mtuci \n
Чтобы узнать, какая сейчас неделя (верхняя/нижняя) - используйте команду /week \n
Форма вывода расписания - Предмет | Кабинет | Время | Преподаватель
""", reply_markup=keyboard)

@bot.message_handler(commands=['week'])
def week(message):
    vn_week = date.today() - date(2022, 8, 22)
    vn_week = vn_week.days // 7 % 2
    if vn_week == 1:
        bot.send_message(message.chat.id, 'Сейчас верхняя неделя', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Сейчас нижняя неделя', reply_markup=keyboard)

@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'Официальный сайт МТУСИ - https://mtuci.ru/', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
    elif message.text.lower() == 'a. понедельник':
        rasp = dayrasp(1)
        forsend = f"понедельник\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id,forsend, reply_markup=keyboard)

    elif message.text.lower() == 'b. вторник':
        rasp = dayrasp(2)
        forsend = f"вторник\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)

    elif message.text.lower() == 'c. среда':
        rasp = dayrasp(3)
        forsend = f"среда\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)

    elif message.text.lower() == 'd. четверг':
        rasp = dayrasp(4)
        forsend = f"четверг\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)

    elif message.text.lower() == 'e. пятница':
        rasp = dayrasp(5)
        forsend = f"пятница\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '__________________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)

    elif message.text.lower() == 'f. расписание на текущую неделю':
        rasp = dayrasp(1)
        forsend = f"понедельник\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n \n'
        rasp = dayrasp(2)
        forsend += f"вторник\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n \n'
        rasp = dayrasp(3)
        forsend += f"среда\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n \n'
        rasp = dayrasp(4)
        forsend += f"четверг\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n \n'
        rasp = dayrasp(5)
        forsend += f"пятница\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)

    elif message.text.lower() == 'g. расписание на следующую неделю':
        rasp = dayrasp(1, plus_week=True)
        forsend = f"понедельник\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n \n'
        rasp = dayrasp(2, plus_week=True)
        forsend += f"вторник\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n \n'
        rasp = dayrasp(3, plus_week=True)
        forsend += f"среда\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n \n'
        rasp = dayrasp(4, plus_week=True)
        forsend += f"четверг\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n \n'
        rasp = dayrasp(5, plus_week=True)
        forsend += f"пятница\n _______________________ \n"
        for sub in rasp:
            forsend += sub[1] + ' ' + str(sub[2]) + ' '
            if sub[3] == 1:
                forsend += pair1
            elif sub[3] == 2:
                forsend += pair2
            elif sub[3] == 3:
                forsend += pair3
            elif sub[3] == 4:
                forsend += pair4
            elif sub[3] == 5:
                forsend += pair5
            cursor.execute(f"select full_name from teacher WHERE subject = '{sub[1]}';")
            prepod = cursor.fetchall()[0][0]
            forsend += ' ' + prepod + '\n'
        forsend += '_______________________ \n'
        bot.send_message(message.chat.id, forsend, reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понял.', reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)
