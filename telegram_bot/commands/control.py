from telegram_bot import emojies, keyboards

coors = [100.0, 100.0, 100.0]
prev_message_id = 0
prev_message_canceled = False


def control(bot, update):
    global prev_message_id, prev_message_canceled
    if not prev_message_id == 0 and not prev_message_canceled:
        bot.editMessageText(text="You called another control panel, so I hid this to make chat looks clear ^.^",
                            chat_id=update.message.chat_id,
                            message_id=prev_message_id)
    prev_message_id = update.message.message_id + 1
    prev_message_canceled = False
    update.message.reply_text('Control panel \n X: {}\n Y: {}\n Z: {}'.format(coors[0], coors[1], coors[2]),
                              reply_markup=keyboards.control_reply_markup)


def button(bot, update):
    global prev_message_canceled
    query = update.callback_query

    print("Selected option: {}".format(query.data))

    if query.data == '0':
        bot.editMessageText(text="Nice to work with you :3",
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id)
        prev_message_canceled = True
    else:
        update_coors(query.data)
        bot.editMessageText(text='Control panel \n X: {}\n Y: {}\n Z: {}'.format(coors[0], coors[1], coors[2]),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            reply_markup=keyboards.control_reply_markup)


def update_coors(command):
    if command == "X-":
        coors[0] -= 10.0
    elif command == "X+":
        coors[0] += 10.0
    elif command == "Y-":
        coors[1] -= 10.0
    elif command == "Y+":
        coors[1] += 10.0
    elif command == "XY":
        coors[0] = 100.0
        coors[1] = 100.0
    elif command == "Z-":
        coors[2] -= 10.0
    elif command == "Z+":
        coors[2] += 10.0
