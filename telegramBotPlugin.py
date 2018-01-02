# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
from telegram_bot import main


class HelloWorldPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("Bot started!")
        main.main()


__plugin_name__ = "Telegram Print Bot"
__plugin_version__ = "0.0.1"
__plugin_description__ = "Telegram bot to control printe"
