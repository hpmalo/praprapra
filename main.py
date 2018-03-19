# -*- coding: utf-8 -*-
import coms
import telebot
import os
from telebot import types

bot = telebot.TeleBot(coms.token)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ['Заявка на рекламу✳️', 'О нас✅', 'Предложить новость🔝', 'Заказать бота💻']])
    bot.send_message(m.chat.id, '''Привет я бот помощник👨🏼‍🏭
*Telegram mass media Kazan*🏪
/start начать диалог с ботом
/help помощь
Предложить новость
У меня ты можешь оставить заявку на рекламу🏵
Заказать разработку Телеграм Бота💻
Связаться с нами📞''', parse_mode="Markdown", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, '''Для общения с ботом нажимай на кнопки снизу🔽''')

@bot.message_handler(regexp='Заявка на рекламу✳️')
def media(m):
    keyboard = types.InlineKeyboardMarkup()
    abutton = types.InlineKeyboardButton(text="🎩Бизнес Казань🎩", callback_data="🎩Бизнес Казань🎩")
    bbutton = types.InlineKeyboardButton(text="📺Новости Казань📺", callback_data="📺Новости Казань📺")
    cbutton = types.InlineKeyboardButton(text="🌸Miss Kazan🌸", callback_data="🌸Miss Kazan🌸")
    keyboard.add(abutton)
    keyboard.add(bbutton)
    keyboard.add(cbutton)
    bot.send_message(m.chat.id, """*Выбери Канал на котором ты хочешь купить рекламу*""", parse_mode="Markdown", reply_markup=keyboard)

def bsnkzn(m):
    try:
        if m.text =="в меню▶":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Заявка на рекламу✳️', 'О нас✅', 'Предложить новость🔝', 'Заказать бота💻']])
            bot.send_message(m.chat.id, '''Привет я бот помощник👨🏼‍🏭
*Telegram mass media Kazan*🏪
/start начать диалог с ботом
/help помощь
Предложить новость
У меня ты можешь оставить заявку на рекламу🏵
Заказать разработку Телеграм Бота💻
Связаться с нами📞''', parse_mode="Markdown", reply_markup=keyboard)

        elif m.text:
            bsnn=bot.send_message(m.chat.id, "Введи номер телефона")
            bot.register_next_step_handler(bsnn, bsnkzn2)
            f = open('{}.txt'.format(m.chat.id), 'w+')
            f.write(m.text + '\n')
        else:
            bskz = bot.send_message(m.chat.id, "Я не совсем тебя понимаю, опиши рекламируемый товар текстом")
            bot.register_next_step_handler(bskz, bsnkzn)
    except ValueError:
        bkz=bot.send_message(m.chat.id, "Я не совсем тебя понимаю, опиши рекламируемый товар текстом")
        bot.register_next_step_handler(bkz, bsnkzn)

def bsnkzn3(m):
    try:
        if m.text == "в меню▶":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Заявка на рекламу✳️', 'О нас✅', 'Предложить новость🔝', 'Заказать бота💻']])
            bot.send_message(m.chat.id, '''Привет я бот помощник👨🏼‍🏭
*Telegram mass media Kazan*🏪
/start начать диалог с ботом
/help помощь
Предложить новость
У меня ты можешь оставить заявку на рекламу🏵
Заказать разработку Телеграм Бота💻
Связаться с нами📞''', parse_mode="Markdown", reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        elif m.text.isalnum():
            bot.send_message(m.chat.id, '''*Заявка оформлена*
Жди звонка😉''', parse_mode="Markdown")
            f = open('{}.txt'.format(m.chat.id), 'a')
            f.write(m.text + '\n')
            f.close()
            f = open('{}.txt'.format(m.chat.id), 'r')
            line = f.readlines()
            sym = line[0]
            num = line[1]
            bot.send_message(chat_id='280331686', text="""Заявка 
*Бизнес Казань*
*Рекламный пост*
Описание:
*{}*Номер:
*{}*""".format(sym, num), parse_mode='Markdown')
            f.close()
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            bbb=bot.send_message(m.chat.id, """Блин я тебя не совсем понимаю 
Напиши номер цифрами без *+*""", parse_mode="Markdown")
            bot.register_next_step_handler(bbb, bsnkzn3)
    except ValueError:
        babb = bot.send_message(m.chat.id, """Блин я тебя не совсем понимаю 
Напиши номер цифрами без *+*""", parse_mode="Markdown")
        bot.register_next_step_handler(babb, bsnkzn3)
    except AttributeError:
        babab = bot.send_message(m.chat.id, """Блин я тебя не совсем понимаю 
0Напиши номер цифрами без *+*""", parse_mode="Markdown")
        bot.register_next_step_handler(babab, bsnkzn3)

def bsnkzn2(m):
    try:
        if m.text == "в меню▶":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Заявка на рекламу✳️', 'О нас✅', 'Предложить новость🔝', 'Заказать бота💻']])
            bot.send_message(m.chat.id, '''Привет я бот помощник👨🏼‍🏭
*Telegram mass media Kazan*🏪
/start начать диалог с ботом
/help помощь
Предложить новость
У меня ты можешь оставить заявку на рекламу🏵
Заказать разработку Телеграм Бота💻
Связаться с нами📞''', parse_mode="Markdown", reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        elif m.text.isalnum():
            bot.send_message(m.chat.id, '''*Заявка оформлена*
Жди звонка😉''', parse_mode="Markdown")
            f = open('{}.txt'.format(m.chat.id), 'a')
            f.write(m.text + '\n')
            f.close()
            f = open('{}.txt'.format(m.chat.id), 'r')
            line = f.readlines()
            sym = line[0]
            num = line[1]
            bot.send_message(chat_id='280331686', text="""Заявка 
*Бизнес Казань*
*Реклама в закрепленном сообщении*
Описание:
*{}*Номер:
*{}*""".format(sym, num), parse_mode='Markdown')
            f.close()
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            bbb=bot.send_message(m.chat.id, """Блин я тебя не совсем понимаю 
Напиши номер цифрами без *+*""", parse_mode="Markdown")
            bot.register_next_step_handler(bbb, bsnkzn2)
    except ValueError:
        babb = bot.send_message(m.chat.id, """Блин я тебя не совсем понимаю 
Напиши номер цифрами без *+*""", parse_mode="Markdown")
        bot.register_next_step_handler(babb, bsnkzn2)
    except AttributeError:
        babab = bot.send_message(m.chat.id, """Блин я тебя не совсем понимаю 
0Напиши номер цифрами без *+*""", parse_mode="Markdown")
        bot.register_next_step_handler(babab, bsnkzn2)

def bsnkzn4(m):
    try:
        if m.text == "в меню▶":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Заявка на рекламу✳️', 'О нас✅', 'Предложить новость🔝', 'Заказать бота💻']])
            bot.send_message(m.chat.id, '''Привет я бот помощник👨🏼‍🏭
*Telegram mass media Kazan*🏪
/start начать диалог с ботом
/help помощь
Предложить новость
У меня ты можешь оставить заявку на рекламу🏵
Заказать разработку Телеграм Бота💻
Связаться с нами📞''', parse_mode="Markdown", reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        elif m.text.isalnum():
            bot.send_message(m.chat.id, '''*Заявка оформлена*
Жди звонка😉''', parse_mode="Markdown")
            f = open('{}.txt'.format(m.chat.id), 'a')
            f.write(m.text + '\n')
            f.close()
            f = open('{}.txt'.format(m.chat.id), 'r')
            line = f.readlines()
            sym = line[0]
            num = line[1]
            bot.send_message(chat_id='280331686', text="""Заявка 
*Бизнес Казань*
*Обзор вашего предприятия/ Завдения/ Фирмы*
Описание:
*{}*Номер:
*{}*""".format(sym, num), parse_mode='Markdown')
            f.close()
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            bbb=bot.send_message(m.chat.id, """Блин я тебя не совсем понимаю 
Напиши номер цифрами без *+*""", parse_mode="Markdown")
            bot.register_next_step_handler(bbb, bsnkzn4)
    except ValueError:
        babb = bot.send_message(m.chat.id, """Блин я тебя не совсем понимаю 
Напиши номер цифрами без *+*""", parse_mode="Markdown")
        bot.register_next_step_handler(babb, bsnkzn4)
    except AttributeError:
        babab = bot.send_message(m.chat.id, """Блин я тебя не совсем понимаю 
0Напиши номер цифрами без *+*""", parse_mode="Markdown")
        bot.register_next_step_handler(babab, bsnkzn4)

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == '🎩Бизнес Казань🎩':
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="1️⃣ ", callback_data="1️⃣ ")
        bbutto = types.InlineKeyboardButton(text="2️⃣ ", callback_data="2️⃣ ")
        cbutto = types.InlineKeyboardButton(text="3️⃣ ", callback_data="3️⃣ ")
        keyboard.add(abutto)
        keyboard.add(bbutto)
        keyboard.add(cbutto)
        bot.send_message(chat_id=c.message.chat.id, text='''🎩Бизнес Казань🎩
Прайс рекламы:

1️⃣ Реклама в закрепленном сообщении
    (_обновляется раз в месяц_) 
    *15000* рублей.

2️⃣ Рекламный пост
   (_удаляется через сутки_)
    *3000* рублей.

3️⃣ Обзор вашего предприятия/ Завдения/ Фирмы
    (_статья в  выпуске_)
    *по договоренности*''',parse_mode='Markdown', reply_markup=keyboard)
    elif c.data == "1️⃣ ":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['в меню▶']])
        bsn=bot.send_message(chat_id=c.message.chat.id, text="""Напиши кратко что ты хочешь рекламировать
*Например*
_Меня зовут Саша я из компании Money Credit, хочу рекламировать кредитный продукт_""",parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(bsn, bsnkzn)

    elif c.data == "2️⃣ ":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['в меню▶']])
        bsn=bot.send_message(chat_id=c.message.chat.id, text="""Напиши кратко что ты хочешь рекламировать""", reply_markup=keyboard)
        bot.register_next_step_handler(bsn, bsnkzn)

    elif c.data == "3️⃣ ":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['в меню▶']])
        bsn=bot.send_message(chat_id=c.message.chat.id, text="""Напиши кратко что ты хочешь рекламировать""", reply_markup=keyboard)
        bot.register_next_step_handler(bsn, bsnkzn4)

    elif c.data == '📺Новости Казань📺':
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="1️⃣ ", callback_data="1️⃣ ")
        bbutto = types.InlineKeyboardButton(text="2️⃣ ", callback_data="2️⃣ ")
        cbutto = types.InlineKeyboardButton(text="3️⃣ ", callback_data="3️⃣ ")
        keyboard.add(abutto)
        keyboard.add(bbutto)
        keyboard.add(cbutto)
        bot.send_message(chat_id=c.message.chat.id, text='''📺Новости Казань📺
Прайс рекламы:

1️⃣ Реклама в закрепленном сообщении
(_обновляется раз в месяц_) 
*15000* рублей.

2️⃣ Рекламный пост
(_удаляется через сутки_)
*3000* рублей.

3️⃣ Обзор
(_статья в  выпуске_)
*по договоренности*''', parse_mode='Markdown', reply_markup=keyboard)
    elif c.data == '🌸Miss Kazan🌸':
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="1️⃣ ", callback_data="1️⃣ ")
        bbutto = types.InlineKeyboardButton(text="2️⃣ ", callback_data="2️⃣ ")
        cbutto = types.InlineKeyboardButton(text="3️⃣ ", callback_data="3️⃣ ")
        keyboard.add(abutto)
        keyboard.add(bbutto)
        keyboard.add(cbutto)
        bot.send_message(chat_id=c.message.chat.id, text='''🌸Miss Kazan🌸
Прайс рекламы:

1️⃣ Реклама в закрепленном сообщении
(_обновляется раз в месяц_) 
*15000* рублей.

2️⃣ Рекламный пост
(_удаляется через сутки_)
*3000* рублей.

3️⃣ Обзор
(_статья в  выпуске_)
*по договоренности*''', parse_mode='Markdown', reply_markup=keyboard)

@bot.message_handler(regexp='О нас✅')
def onas(m):
    bot.send_message(m.chat.id, """*Telegram mass media Kazan*🏪
Мы компания👨‍👩‍👧‍👦 которая занимается:
-развитием телеграм Каналов🏢
-разработкой ботов🖥""", parse_mode='Markdown')

@bot.message_handler(regexp='Предложить новость🔝')
def news(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ['в меню▶']])
    nsw=bot.send_message(m.chat.id, """Отправьте новость которую хотите опубликовать""", reply_markup=keyboard)
    bot.register_next_step_handler(nsw, news1)

def news1(m):
    try:
        if m.text == "в меню▶":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Заявка на рекламу✳️', 'О нас✅', 'Предложить новость🔝', 'Заказать бота💻']])
            bot.send_message(m.chat.id, '''Привет я бот помощник👨🏼‍🏭
        *Telegram mass media Kazan*🏪
        /start начать диалог с ботом
        /help помощь
        Предложить новость
        У меня ты можешь оставить заявку на рекламу🏵
        Заказать разработку Телеграм Бота💻
        Связаться с нами📞''', parse_mode="Markdown", reply_markup=keyboard)
        elif m.text:
            bot.send_message(m.chat.id, 'Спасибо за вашу новость, мы обязательно ее опубликуем по возможности')
            f = open('{}.txt'.format(m.chat.id), 'w+')
            f.write(m.text)
            f.close()
            f = open('{}.txt'.format(m.chat.id), 'r')
            line = f.read()
            bot.send_message("280331686", """НОВОСТЬ
{}""".format(line))
            f.close()
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            vav = bot.send_message(m.chat.id, "Какая то ошибка, попробуй снова")
            bot.register_next_step_handler(vav, news1)
    except ValueError:
        vav=bot.send_message(m.chat.id, "Какая то ошибка, попробуй снова")
        bot.register_next_step_handler(vav, news1)

@bot.message_handler(regexp='Заказать бота💻')
def zakaz(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ['в меню▶']])
    zak=bot.send_message(m.chat.id, "Опиши в двух словах что должен уметь бот", reply_markup=keyboard)
    bot.register_next_step_handler(zak, zak1)

def zak1(m):
    try:
        if m.text == "в меню▶":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Заявка на рекламу✳️', 'О нас✅', 'Предложить новость🔝', 'Заказать бота💻']])
            bot.send_message(m.chat.id, '''Привет я бот помощник👨🏼‍🏭
    *Telegram mass media Kazan*🏪
    /start начать диалог с ботом
    /help помощь
    Предложить новость
    У меня ты можешь оставить заявку на рекламу🏵
    Заказать разработку Телеграм Бота💻
    Связаться с нами📞''', parse_mode="Markdown", reply_markup=keyboard)

        elif m.text:
            bsnn = bot.send_message(m.chat.id, "Введи номер телефона")
            bot.register_next_step_handler(bsnn, bsnkzn2)
            f = open('{}.txt'.format(m.chat.id), 'w+')
            f.write(m.text + '\n')
        else:
            bskz = bot.send_message(m.chat.id, "Я не совсем тебя понимаю, опиши рекламируемый товар текстом")
            bot.register_next_step_handler(bskz, zak1)
    except ValueError:
        bkz = bot.send_message(m.chat.id, "Я не совсем тебя понимаю, опиши рекламируемый товар текстом")
        bot.register_next_step_handler(bkz, zak1)









bot.polling(none_stop=True, interval=4)