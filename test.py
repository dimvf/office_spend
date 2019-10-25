from dialog_bot_sdk.bot import DialogBot
import grpc

def on_msg(*params):
        bot.messaging.send_message(peer, "Введите 'help' для помощи")

if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        "hackathon-mob.transmit.im",  # bot endpoint from environment
        grpc.ssl_channel_credentials(), # SSL credentials (empty by default!)
        '7f38e457bebadf578dbba6d5ccbacd4b3e926938'  # bot token from environment
    )
    bot.messaging.on_message(on_msg)