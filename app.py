from chatterbot import ChatBot
from flask import Flask, render_template, request
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
app.static_folder = 'static'

# Creating ChatBot Instance
# englishBot = ChatBot(
    # 'CoronaBot',
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # logic_adapters=[
        # 'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter',
        # 'chatterbot.logic.BestMatch',
        # {
            # 'import_path': 'chatterbot.logic.BestMatch',
            # 'default_response': 'I am sorry, but I do not understand. I am still learning.',
            # 'maximum_similarity_threshold': 0.90
        # }
    # ],
    # database_uri='sqlite:///database.sqlite3'
# )
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(str(englishBot.get_response(userText)))
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run()