import pickle
from norm import *
from telebot import TelegramBot

nlp_pipeline = pickle.load(open("tfidf_pipe.pkl", 'rb'))

bot = TelegramBot(nlp_pipeline)

update_id = None

while True:
    updates = bot.get_updates(offset=update_id)['result']

    if updates:
        for item in updates:
            update_id = item['update_id']
            try:
                message = item['message']['text']
            except:
                message = None
            if message:
                chat_id = item['message']['chat']['id']

                prediction = bot.generate_response(message)
                bot.sent_msg(prediction, chat_id)