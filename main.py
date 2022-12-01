

from flask import Flask, request
import telebot
import os


app=Flask(__name__)
TOKEN=os.environ.get("TOKEN")
bot=telebot.TeleBot (TOKEN)

@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, "Hello, user!")
@bot.message_handler(commands=['training'])
def  message_training(message):
    keyboard=telebot.types.InlineKeyboardMarkup(row_width=1)
    with open ("training programs.txt") as file:
        training_programs=[item.split(",") for item in file]

        for title, link in training_programs:
            url_button=telebot.types.InlineKeyboardMarkup(text=title.strip(), url=link.strip())
            keyboard.add(url_button)

        bot.send_message(message.chat.id, "List of training programs", reply_markup=keyboard)

@bot.message_handler(func=lambda x: x.text.lower().startwith ('pytnon'))
def  message_text(message):
    bot.send_message(message.chat.id, "python")

@app.route('/'+TOKEN, methods=["POST"])
def  get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.road().decode("utf-8"))])
    return " Pytnon Telegram Bot", 200

@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url="https://newapp0730.herokuapp.com/"+TOKEN)
    return "Pytnon Telegram Bot",200

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))


