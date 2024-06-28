from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer
from chatterbot.storage import SQLStorageAdapter
from chatterbot.trainers import ChatterBotCorpusTrainer
from custom_storage import ReadOnlySQLStorageAdapter
from text_processing import handle_special_cases, expand_abbreviations

app = Flask(__name__)
chatBot = ChatBot(
    'MediBot',
    storage_adapter='custom_storage.ReadOnlySQLStorageAdapter',
    database_uri='sqlite:///database.db',
    read_only=True
)
trainer = ChatterBotCorpusTrainer(chatBot)
list_trainer = ListTrainer(chatBot)
custom_corpus_file = 'D:\minor 1\Medi Bot - Personal Medical Assistant\Medical.yml'
trainer.train(custom_corpus_file)
def process_input(text):
    text = handle_special_cases(text)
    expanded_text = expand_abbreviations(text)
    keywords = [word.lower() for word in expanded_text.split()]
    return keywords
def process_output(response):
    return response
print("Hi, I am MediBot")
while True:
    query = input(">")
    response = chatBot.get_response(query)
    if response.confidence < 0.5:
        default_response = "I'm sorry, I didn't understand that."
        print(default_response)
    print(str(response))