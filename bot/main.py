import telebot
from telebot import types
import random
import string

# Токен твоего бота
bot = telebot.TeleBot("7399086585:AAHT3PppLMvL5GgVvjKSacXGkOYrwbbZlyQ")

# Словарь для хранения состояния пользователей
user_states = {}

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin.")

# Команда /hello
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

# Команда /bye
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

# Команда /test — начало теста
@bot.message_handler(commands=['test'])
def start_test(message):
    user_states[message.chat.id] = {'question': 0, 'score': 0}
    bot.reply_to(message, "Вы хотите начать тест? (да/нет)")

# Обработка ответов в тесте
@bot.message_handler(func=lambda message: message.chat.id in user_states)
def handle_test_response(message):
    user_id = message.chat.id
    state = user_states[user_id]
    question = state['question']
    score = state['score']

    if question == 0:
        if message.text.lower() == 'да':
            bot.reply_to(message, "Вопрос 1: Часто вы используете личный автомобиль? (да/нет)")
            state['question'] += 1  # Переход к следующему вопросу
        else:
            bot.reply_to(message, "А зачем вы здесь? :)")
            del user_states[user_id]

    elif question == 1:
        if message.text.lower() == 'нет':
            score += 1
        state['score'] = score  # Обновляем счет

        bot.reply_to(message, "Вопрос 2: Часто вы разделяете мусор? (да/нет)")
        state['question'] += 1

    elif question == 2:
        if message.text.lower() == 'да':
            score += 1
        state['score'] = score

        bot.reply_to(message, "Вопрос 3: Часто вы покупаете товары с избыточной упаковкой? (да/нет)")
        state['question'] += 1

    elif question == 3:
        if message.text.lower() == 'нет':
            score += 1
        state['score'] = score

        bot.reply_to(message, "Вопрос 4: Используете ли вы многоразовые сумки для покупок? (да/нет)")
        state['question'] += 1

    elif question == 4:
        if message.text.lower() == 'да':
            score += 1
        state['score'] = score

        bot.reply_to(message, "Вопрос 5: часто вы используете одноразовые пластиковые изделия? (да/нет)")
        state['question'] += 1

    elif question == 5:
        if message.text.lower() == 'нет':
            score += 1
        state['score'] = score

        bot.reply_to(message, "Вопрос 6: Вы выбрасываете мусор на улице или в неположенных местах? (да/нет)")
        state['question'] += 1

    elif question == 6:
        if message.text.lower() == 'нет':
            score += 1
        state['score'] = score

        bot.reply_to(message, "Вопрос 7: Вы часто оставляете электроприборы включенными, когда они не используются? (да/нет)")
        state['question'] += 1

    elif question == 7:
        if message.text.lower() == 'нет':
            score += 1
        state['score'] = score

        bot.reply_to(message, "Вопрос 8: Вы часто покупаете одежду и другие товары, которые быстро выходят из моды и выбрасываете их? (да/нет)")
        state['question'] += 1

    elif question == 8:
        if message.text.lower() == 'нет':
            score += 1
        state['score'] = score

        bot.reply_to(message, "Вопрос 9: Вы не задумываетесь о последствиях своих покупок для окружающей среды? (да/нет)")
        state['question'] += 1

    elif question == 9:
        if message.text.lower() == 'да':
            score += 1
        state['score'] = score

        bot.reply_to(message, "Вопрос 10: Вы часто оставляете мусор на пляже или в парке после отдыха? (да/нет)")
        state['question'] += 1

    elif question == 10:
        if message.text.lower() == 'нет':
            score += 1
        state['score'] = score



        # Завершение теста и вывод результата
        bot.reply_to(message, f"Тест завершен! Ваш результат: {score} из 10.")
        
        # Удаляем пользователя из состояния после завершения теста.
        del user_states[user_id]



# === Запуск бота ===
print("Бот запущен...")
bot.polling()