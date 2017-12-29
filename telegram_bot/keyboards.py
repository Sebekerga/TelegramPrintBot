from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram_bot import emojies

control = [
            # [InlineKeyboardButton("x", callback_data='1'),
            # InlineKeyboardButton("and", callback_data='1'),
            # InlineKeyboardButton("Y", callback_data='1'),
            # InlineKeyboardButton("Z", callback_data='1'),
            # InlineKeyboardButton("E", callback_data='1')],

           [InlineKeyboardButton(" ", callback_data='1'),
            InlineKeyboardButton(emojies.arrow_up, callback_data='Y+'),
            InlineKeyboardButton(" ", callback_data='1'),
            InlineKeyboardButton(emojies.arrow_up, callback_data='Z+'),
            InlineKeyboardButton(emojies.arrow_up, callback_data='E-')],

           [InlineKeyboardButton(emojies.arrow_left, callback_data='X-'),
            InlineKeyboardButton(emojies.home, callback_data='XY'),
            InlineKeyboardButton(emojies.arrow_right, callback_data='X+'),
            InlineKeyboardButton(emojies.home, callback_data='Z'),
            InlineKeyboardButton(emojies.arrow_down, callback_data='E+')],

           [InlineKeyboardButton(" ", callback_data='1'),
            InlineKeyboardButton(emojies.arrow_down, callback_data='Y-'),
            InlineKeyboardButton(emojies.back + " Cancel", callback_data='0'),
            InlineKeyboardButton(emojies.arrow_down, callback_data='Z+'),
            InlineKeyboardButton(emojies.arrow_down_doubled, callback_data='E++')]]

control_reply_markup = InlineKeyboardMarkup(control)

#minimalized_control =