#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, octoprint.plugin
import telegram_bot.commands.control as control_com
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

coors = [100.0, 100.0, 100.0]
prev_message_id = 0
prev_message_canceled = False


class TelegramPrintBot(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")


def control(bot, update):
    control_com.control(bot, update)


def button(bot, update):
    control_com.button(bot, update)


def help(bot, update):
    update.message.reply_text("Use /control to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("348441909:AAE1zt0j_BR_0krs4ewULqkewJzrZTX_YvQ")

    updater.dispatcher.add_handler(CommandHandler('control', control))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('start', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()