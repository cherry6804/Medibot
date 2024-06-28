from flask import Flask, render_template, request
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer
from chatterbot.storage import SQLStorageAdapter
from chatterbot.trainers import ChatterBotCorpusTrainer
from custom_storage import ReadOnlySQLStorageAdapter
from text_processing import handle_special_cases, expand_abbreviations
app = Flask(__name__)
chatBot = ChatBot(
    'Medibot',
    storage_adapter='custom_storage.ReadOnlySQLStorageAdapter',
    database_uri='sqlite:///database.db',
    read_only=True
)
trainer = ChatterBotCorpusTrainer(chatBot)
list_trainer = ListTrainer(chatBot)
custom_corpus_file = 'F:\minor 1\Medibot\Medical.yml'
trainer.train(custom_corpus_file)
def process_input(text):
    text = handle_special_cases(text)
    expanded_text = expand_abbreviations(text)
    keywords = [word.lower() for word in expanded_text.split()]
    return keywords
def process_output(response):
    return response
@app.route("/")
def index():
    return render_template("app medibot.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/contactUs")
def contactUs():
    return render_template("contactUs.html")
@app.route("/help")
def help():
    return render_template("help.html")
@app.route("/fp")
def fp():
    return render_template("fp.html")
@app.route("/dash")
def dash():
    return render_template("dash.html")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    user_keywords = process_input(userText)
    user_statement = Statement(userText, metadata={"keywords": user_keywords})
    response = chatBot.get_response(user_statement)
    processed_response = process_output(response)
    if response.confidence < 0.9:
        default_response = "I'm sorry, I didn't understand that."
        return default_response
    return str(processed_response)
if __name__ == "__main__":
    app.run()