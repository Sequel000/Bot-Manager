from telebot import types

def start_message():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_start = types.KeyboardButton("Начать")
    markup.add(btn_start)
    return markup

def country():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_romania = types.KeyboardButton("Румыния")
    btn_ukraine = types.KeyboardButton("Украина")
    btn_russia = types.KeyboardButton("Россия")
    btn_other = types.KeyboardButton("Другое")
    markup.add(btn_romania, btn_ukraine, btn_russia, btn_other)
    return markup

def workplace():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_legal = types.KeyboardButton("Официально")
    btn_illegal = types.KeyboardButton("Неофициально")
    markup.add(btn_legal, btn_illegal)
    return markup

def typedoc():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("ПМЖ")
    btn_2 = types.KeyboardButton("ВМЖ")
    btn_3 = types.KeyboardButton("Выезд из Украины")
    btn_4 = types.KeyboardButton("Вьезд в Украину")
    btn_5 = types.KeyboardButton("Водительские права")
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
    return markup

def docmanager():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("Выбрать услугу")
    btn_2 = types.KeyboardButton("Назад")
    markup.add(btn_1, btn_2)
    return markup

def criminal():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("Да")
    btn_2 = types.KeyboardButton("Нет")
    markup.add(btn_1, btn_2)
    return markup

def country_doc():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("Болгария")
    btn_2 = types.KeyboardButton("Италия")
    btn_3 = types.KeyboardButton("Турция")
    btn_4 = types.KeyboardButton("Украина")
    btn_5 = types.KeyboardButton("Молдова")
    btn_6 = types.KeyboardButton("Казакстан")
    btn_7 = types.KeyboardButton("Румыния")
    btn_7 = types.KeyboardButton("Назад")
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7)
    return markup

def deive_country_doc():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("США")
    btn_2 = types.KeyboardButton("Украина")
    btn_3 = types.KeyboardButton("Канада")
    markup.add(btn_1, btn_2, btn_3)
    return markup






