from telebot import types
from markup import *
from bot_seting import bot
# Замените на ваш токен бота

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Здравствуйте. Спасибо что обратились к нам, для того что бы начать регестрицию и выбор услуг, нажмите \"Начать\"",
        reply_markup=start_message()
    )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Начать":

        bot.send_message(
            chat_id=message.chat.id,
            text="Введите ФИО через пробел:",
            reply_markup=types.ReplyKeyboardRemove()
        )

        bot.register_next_step_handler(message, get_fio)
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Извините, я вас не понял. Нажмите кнопку \"Начать\", чтобы оставить заявку.")

def get_fio(message):
    fio = message.text.split()
    if len(fio) != 3:
        bot.send_message(
            chat_id=message.chat.id,
            text="Пожалуйста, введите ФИО через пробел, без точек и прочих символов."
        )
        bot.register_next_step_handler(message, get_fio)
    else:
        full_name = message.text # -----------
        bot.send_message(
            chat_id=message.chat.id,
            text="Гражданином какой страны вы являетесь?",
            reply_markup=country()
        )
        bot.register_next_step_handler(message, get_country)

def get_country(message):
    if message.text in ["Румыния", "Украина", "Россия"]:
        country = message.text # ---------
    elif message.text == "Другое":
        bot.send_message(
            chat_id=message.chat.id,
            text="Введите название своей страны:"
        )
        bot.register_next_step_handler(message, get_other_country)
        return 0
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Пожалуйста, выберите страну из списка. Если вашей страны нету в списке то нажмите \"Другое\" и напишите название своей страны"
        )
        bot.register_next_step_handler(message, get_country)
        return 0

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Вы работаете официально или же нет?",
        reply_markup=workplace()
    )
    bot.register_next_step_handler(message, criminal_record)

def get_other_country(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Вы работаете официально или же нет?",
        reply_markup=workplace()
    )
    bot.register_next_step_handler(message, criminal_record)
    return 0

def criminal_record(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"У вас когда либо была судимость?",
        reply_markup=criminal()
    )
    bot.register_next_step_handler(message, check_criminal)
    return 0

def check_criminal(message):
    if(message.text.lower() == "да"):
        bot.send_message(
            chat_id=message.chat.id,
            text="Опишите свою ситуацию, чуть подробнее, открыты ли на данный момент какие то дела, приходилось ли вам отбывать тюремный срок, если да то по какой статье (или статьям)? Чем подробнее вы опишите вашу ситуацию, тем легче нам будет сделать все необходимые документы, максимально безопасно для вас.",
            reply_markup=types.ReplyKeyboardRemove()
        )
        bot.register_next_step_handler(message, get_doc_status)
        return 0
    elif (message.text.lower() == "нет"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Какую услугу вы хотите?",
            reply_markup=typedoc()
        )
        bot.register_next_step_handler(message, info_doc)
        return 0
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Я вас не понял. Так у вас когда либо была судимость?",
            reply_markup=criminal()
        )
        bot.register_next_step_handler(message, check_criminal)
        return 0
def get_doc_status(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Какую услугу вы хотите?",
        reply_markup=typedoc()
    )
    bot.register_next_step_handler(message, info_doc)
    return 0
def info_doc(message):
    ansver = message.text
    if (ansver == "ВМЖ"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ВМЖ",
            reply_markup=country_doc()
        )
        bot.register_next_step_handler(message, chek_doc_country_vmj)
        return 0

    elif (ansver == "ПМЖ"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ПМЖ",
            reply_markup=country_doc()
        )
        bot.register_next_step_handler(message, chek_doc_country_pmj)
        return 0

    elif (ansver == "Выезд из Украины"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация Украины",
            reply_markup=docmanager()
        )
        bot.register_next_step_handler(message, end_step)
        return 0

    elif (ansver == "Вьезд в Украину"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация Вьезд в Украину",
            reply_markup=docmanager()
        )
        bot.register_next_step_handler(message, end_step)
        return 0

    elif (ansver == "Водительские права"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация Водительские права",
            reply_markup=drive_country_doc()
        )
        return 0

    else:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Я вас не понял, какую услугу вы хотите? Выберете услугу из списка:",
            reply_markup=typedoc()
        )
        bot.register_next_step_handler(message, info_doc)
        return 0


def chek_doc_country_vmj(message):

    ansver = message.text

    if (ansver == "Болгария"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ВМЖ",
            reply_markup=country_doc()
        )
        return 0
    elif (ansver == "Италия"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ПМЖ",
            reply_markup=country_doc()
        )
        return 0

    elif (ansver == "Турция"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ПМЖ",
            reply_markup=country_doc()
        )
        return 0

    elif (ansver == "Украина"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Молдова",
            reply_markup=country_doc()
        )
        return 0

    elif (ansver == "Казакстан"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ПМЖ",
            reply_markup=country_doc()
        )
        return 0

    elif (ansver == "Румыния"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ПМЖ",
            reply_markup=country_doc()
        )
        return 0

    elif (ansver == "Назад"):

        bot.send_message(
            chat_id=message.chat.id,
            text=f"Какую услугу вы хотите?",
            reply_markup=typedoc()
        )
        bot.register_next_step_handler(message, info_doc)
        return 0

    else:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Выбирете страну из списка:",
            reply_markup=country_doc()
        )
        bot.register_next_step_handler(message, chek_doc_country_vmj)
        return 0

    bot.register_next_step_handler(message, end_step)

def chek_doc_country_pmj(message):

    ansver = message.text

    if (ansver == "Болгария"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ВМЖ",
            reply_markup=country_doc()
        )
        return 0
    elif (ansver == "Италия"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ПМЖ",
            reply_markup=country_doc()
        )
        return 0

    elif (ansver == "Турция"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ПМЖ",
            reply_markup=country_doc()
        )
        return 0

    elif (ansver == "Украина"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Молдова",
            reply_markup=country_doc()
        )
        return 0

    elif (ansver == "Казакстан"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ПМЖ",
            reply_markup=country_doc()
        )
        return 0

    elif (ansver == "Румыния"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Информация ПМЖ",
            reply_markup=country_doc()
        )
        return 0


    elif (ansver == "Назад"):

        bot.send_message(
            chat_id=message.chat.id,
            text=f"Какую услугу вы хотите?",
            reply_markup=typedoc()
        )
        bot.register_next_step_handler(message, info_doc)
        return 0

    else:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Выберите страну из списка",
            reply_markup=country_doc()
        )
        bot.register_next_step_handler(message, chek_doc_country_pmj)
        return 0

    bot.register_next_step_handler(message, end_step)


def end_step(message):

    ansver = message.text

    if (ansver == "Назад"):
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Какую услугу вы хотите?",
            reply_markup=typedoc()
        )
        bot.register_next_step_handler(message, info_doc)
        return 0
    elif (ansver == "Выбрать услугу"):
        a = types.ReplyKeyboardRemove()
        bot.send_message(
            chat_id=message.chat.id,
            text="Спасибо, с вами скоро свяжутся!",
            reply_markup=a
        )
        return 0

bot.infinity_polling()
