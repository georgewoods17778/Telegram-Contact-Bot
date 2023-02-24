#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple Bot to contact George
"""

import logging, time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello my friend this is the new doxx free telegram contact bot for George!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('In order to send a message to George just enter /message <your message for george> and I\'ll shipp it to him :)')

def legal(update, context):
    """Send a message when the command /legal is issued."""
    update.message.reply_text('This bot was developed by [George Woods](https://github.com/georgewoods17778) © All rights reserved',parse_mode='MarkdownV2', disable_web_page_preview=True)

def message(update, context):
    """Send a message when the command /message is issued."""
    time.sleep(1)
    logi = open("messages_for_george.txt","a")
    logi.write(update.message.text)
    logi.write("\n")
    logi.close()
    update.message.reply_text('Thank you for your message!')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("<secret_bot_token>", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("message", message))
    dp.add_handler(CommandHandler("legal", legal))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()