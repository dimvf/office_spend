from dialog_bot_sdk.bot import DialogBot
import grpc
from flask import Flask

app = Flask(__name__)

#def on_msg(*params):
#        bot.messaging.send_message(peer, "Введите 'help' для помощи")


@app.route('/')
def main():
    return "Hello world"
    #bot = DialogBot.get_secure_bot(
    #    "hackathon-mob.transmit.im",  # bot endpoint from environment
    #    grpc.ssl_channel_credentials(), # SSL credentials (empty by default!)
    #    '7f38e457bebadf578dbba6d5ccbacd4b3e926938'  # bot token from environment
    #)
    #bot.messaging.on_message(on_msg)