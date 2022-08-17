import json
import requests

class TelegramBot:
    def __init__(self, pipeline):
        self.token = "5482535473:AAHC7UJ5wQoePl3h0C90iuc7Jcv6Vh0_m6I"
        self.url = f"https://api.telegram.org/bot{self.token}"
        self.pipeline = pipeline

    def get_updates(self, offset=None):
        url = self.url + "/getUpdates?timeout=100"
        if offset:
            url = url + f"&offset={offset + 1}"
        url_info = requests.get(url)
        return json.loads(url_info.content)

    def sent_msg(self, msg, chat_id):
        url = self.url + f'/sendMessage?chat_id={chat_id}&text={msg}'
        if msg is not None:
            requests.get(url)

    def generate_response(self, user_text):
        pred = self.pipeline.predict([user_text])[0]
        if pred == "sarcasm":
            pred = "Ha, ha, not funny"
        elif pred == "irony":
            pred = "What a terse line. Is the head blithe? Or is the money gone?"
        elif pred == "figurative":
            pred = "Subtle, and most importantly by whom - an intelligent person!!! "
        else:
            pred = "Thanks"
        return pred

