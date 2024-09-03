import telebot
import telebot as tb

bot = tb.TeleBot('7302759225:AAERjoW4BHboVQ0zeF5ML7fJSKzRWRYlW-c')

# @bot.message_handler()
# def main1():
#     bot.send_message('6754232719:AAEJwI5zmSlMiNXYmE9qon99Q_bn2teEeWw', text='awdadsdafqawawsfeasdfafaadas')

tb.types.KeyboardButton(text='wadsdwasdasd')


@bot.message_handler(commands=['start'])
def main(message):
    mark = tb.types.InlineKeyboardMarkup()
    mark.add(tb.types.InlineKeyboardButton('💿профиль💿', callback_data='pro'))
    mark.add(tb.types.InlineKeyboardButton('🖤категории🖤', callback_data='cat'))
    but1 = tb.types.InlineKeyboardButton('💞о боте💞', callback_data='obo')
    but2 = tb.types.InlineKeyboardButton('✅техподдержка✅', callback_data='teh')
    mark.add(but1, but2)
    mark.add(tb.types.InlineKeyboardButton('📸пруфы📸', callback_data='pru'))

    bot.send_message(message.chat.id, text="😈Bac привeтствует самый бaлдежный бoт😈\n"
                                           "🤤У нас ты можешь увидеть тонны apхивов, от которых текут cлюнки🤤\n"
                                           "❣️Mы гарантируем, что oт нашего эксклюзивного контента никто не oстанется рaвнодушным❣️\n",
                     reply_markup=mark)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'cat':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('🍓школьницы🍓', callback_data='cat1'))
        mark.add(tb.types.InlineKeyboardButton('😋цn😋', callback_data='cat2'))
        mark.add(tb.types.InlineKeyboardButton('🥵Home Videos🥵', callback_data='cat3'))
        mark.add(tb.types.InlineKeyboardButton('📸пруфы📸', callback_data='pru'))
        mark.add(tb.types.InlineKeyboardButton('💻главное меню💻', callback_data='gla'))
        bot.send_message(callback.message.chat.id, text='💘😋самые свежие сливы из секретных архивов😋💘',
                         reply_markup=mark)


    elif callback.data == 'pru':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('💻главное меню💻', callback_data='gla'))
        bot.send_video(callback.message.chat.id, open('pru.mp4', 'rb'), reply_markup=mark)
        bot.send_message(callback.message.chat.id, text='💪Больше пруфов в категориях💪', reply_markup=mark)



    elif callback.data == 'gla':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('💿профиль💿', callback_data='pro'))
        mark.add(tb.types.InlineKeyboardButton('🖤категории🖤', callback_data='cat'))
        but1 = tb.types.InlineKeyboardButton('💞о боте💞', callback_data='obo')
        but2 = tb.types.InlineKeyboardButton('✅техподдержка✅', callback_data='teh')
        mark.add(but1, but2)
        mark.add(tb.types.InlineKeyboardButton('📸пруфы📸', callback_data='pru'))
        bot.send_message(callback.message.chat.id,
                         text='💕Здесь ты можешь увидеть тонны apхивов, от которых текут cлюнки💕', reply_markup=mark)

    elif callback.data == 'pro':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('да', callback_data='gla'))
        bot.send_message(callback.message.chat.id,
                         text=f"💋Привет, {callback.from_user.first_name} , ты действительно хочешь получить райское наслаждение?💋",
                         reply_markup=mark)

    elif callback.data == 'obo':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('Главное меню', callback_data='gla'))
        bot.send_message(callback.message.chat.id, text=f'🗓Бот создан 13.08.2022\n'
                                                        f'🧍Количество пользователей: 12832', reply_markup=mark)

    elif callback.data == 'teh':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('Главное меню', callback_data='gla'))
        bot.send_message(callback.message.chat.id, text=f'Можете написать @linarrhot', reply_markup=mark)

    elif callback.data == 'cat1':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('🗂8 гб🗂', callback_data='opl1'))
        mark.add(tb.types.InlineKeyboardButton('🗂28 гб🗂(🖤🧡PREMIUM🧡🖤)', callback_data='opl2'))
        mark.add(tb.types.InlineKeyboardButton('📸пруфы📸', callback_data='pru1'))
        mark.add(tb.types.InlineKeyboardButton('🖥главное меню🖥', callback_data='gla'))
        bot.send_message(callback.message.chat.id, text="⚡️Выбранный тариф⚡️:\n"
                                                        "🖤Сочные видео школьниц🖤\n"
                                                        "😍Доступ😍: Навсегда\n"
                                                        "\n"
                                                        "В архиве присутствуют:\n"
                                                        "🏫Видео в школе🏫\n"
                                                        "🤫Инцест🤫\n"
                                                        "💦Изн@силования💦\n", reply_markup=mark)

    elif callback.data == 'cat2':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('🗂9 гб🗂', callback_data='opl1'))
        mark.add(tb.types.InlineKeyboardButton('🗂21 гб🗂(🖤🧡PREMIUM🧡🖤)', callback_data='opl2'))
        mark.add(tb.types.InlineKeyboardButton('📸пруфы📸', callback_data='pru2'))
        mark.add(tb.types.InlineKeyboardButton('🖥главное меню🖥', callback_data='gla'))
        bot.send_message(callback.message.chat.id, text="⚡️Выбранный тариф⚡️:\n"
                                                        "🔞Сочные видео м@лолеток🔞\n"
                                                        "😍Доступ😍: Навсегда\n"
                                                        "\n"
                                                        "В архиве присутствуют:\n"
                                                        "🥰Группoвое🥰\n"
                                                        "🤫<10🤫\n"
                                                        "💦Изн@силования💦\n", reply_markup=mark)
    elif callback.data == 'cat3':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('🗂15 гб🗂', callback_data='opl1'))
        mark.add(tb.types.InlineKeyboardButton('🗂39 гб🗂(🖤🧡PREMIUM🧡🖤)', callback_data='opl2'))
        mark.add(tb.types.InlineKeyboardButton('📸пруфы📸', callback_data='pru3'))
        mark.add(tb.types.InlineKeyboardButton('🖥главное меню🖥', callback_data='gla'))
        bot.send_message(callback.message.chat.id, text="⚡️Выбранный тариф⚡️:\n"
                                                        "❤️Видео с дoмашкой❤️\n"
                                                        "😍Доступ😍: Нaвсегда\n"
                                                        ""
                                                        "В архиве присутствуют:"
                                                        "🎆Лучшие видeо более чем от 150 пар🎆\n"
                                                        "🛁В вaнной🛁\n"
                                                        "🍓Жёсткoе🍓\n"
                                                        "🍇Coло🍇\n", reply_markup=mark)

    elif callback.data == 'pru1':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('🏫тариф школьниц🏫', callback_data='cat1'))
        media_group = []
        text = ''
        media_group.append(telebot.types.InputMediaPhoto(open('Ш1.jpg', 'rb'), caption=text))
        media_group.append(telebot.types.InputMediaPhoto(open('Ш2.jpg', 'rb'), caption=''))
        media_group.append(telebot.types.InputMediaPhoto(open('Ш3.jpg', 'rb'), caption=''))
        bot.send_media_group(callback.message.chat.id, media=media_group)
        bot.send_message(callback.message.chat.id, text=f'😍вернуться к тарифу😍', reply_markup=mark)

    elif callback.data == 'pru2':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('❤️тариф цn❤️', callback_data='cat2'))
        media_group = []
        text = ''
        media_group.append(telebot.types.InputMediaPhoto(open('cp1.jpg', 'rb'), caption=text))
        media_group.append(telebot.types.InputMediaPhoto(open('Ц1.jpg', 'rb'), caption=''))
        media_group.append(telebot.types.InputMediaPhoto(open('Ц2.jpg', 'rb'), caption=''))
        bot.send_media_group(callback.message.chat.id, media=media_group)
        bot.send_message(callback.message.chat.id, text=f'😍вернуться к тарифу😍', reply_markup=mark)



    elif callback.data == 'pru3':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('❤️тариф хоум❤️', callback_data='cat3'))
        media_group = []
        text = ''
        media_group.append(telebot.types.InputMediaPhoto(open('X1.jpg', 'rb'), caption=text))
        media_group.append(telebot.types.InputMediaPhoto(open('X2.jpg', 'rb'), caption=''))
        media_group.append(telebot.types.InputMediaPhoto(open('X3.jpg', 'rb'), caption=''))
        bot.send_media_group(callback.message.chat.id, media=media_group)
        bot.send_message(callback.message.chat.id, text=f'😍вернуться к тарифу😍', reply_markup=mark)

    elif callback.data == 'opl1':
        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('🖤🧡PREMIUM доступ🧡🖤', callback_data='opl3'))
        mark.add(tb.types.InlineKeyboardButton('обычный доступ', callback_data='opl3'))
        mark.add(tb.types.InlineKeyboardButton('🖥главное меню🖥', callback_data='gla'))
        mark.add(tb.types.InlineKeyboardButton('📸пруфы📸', callback_data='pru2'))
        bot.send_message(callback.message.chat.id, text="обычный доступ: 119 RUB\n"
                                                        "🖤🧡\n"
                                                        "PREMIUM доступ(❤️‍🔥HOT❤️‍🔥): 179 RUB\n"
                                                        "\n"
                                                        "💜С PREMIUM ДОСТУПОМ ДОСТУПНЫ ВСЕ ТОВАРЫ ДЛЯ ПРОСМОТРА💜\n",
                         reply_markup=mark)
    elif callback.data == 'opl2':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('🖤🧡PREMIUM доступ🧡🖤', callback_data='opl3'))
        mark.add(tb.types.InlineKeyboardButton('обычный доступ', callback_data='opl3'))
        mark.add(tb.types.InlineKeyboardButton('🖥главное меню🖥', callback_data='gla'))
        mark.add(tb.types.InlineKeyboardButton('📸пруфы📸', callback_data='pru2'))
        bot.send_message(callback.message.chat.id, text="обычный доступ: 119 RUB\n"
                                                        "🖤🧡\n"
                                                        "PREMIUM доступ(❤️‍🔥HOT❤️‍🔥): 179 RUB\n"
                                                        "\n"
                                                        "💜С PREMIUM ДОСТУПОМ ДОСТУПНЫ ВСЕ ТОВАРЫ ДЛЯ ПРОСМОТРА💜\n",
                         reply_markup=mark)

    elif callback.data == 'opl3':

        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('✅оплатил✅', callback_data='opl4'))
        mark.add(tb.types.InlineKeyboardButton('🖥главное меню🖥', callback_data='gla'))
        mark.add(tb.types.InlineKeyboardButton('📸пруфы📸', callback_data='pru3'))
        bot.send_message(callback.message.chat.id, text="✅оплата по номеру карты(Альфа):\n"
                                                        "\n"
                                                        "2200152961001180\n"
                                                        "\n"
                                                        "✅мгновенно дадим доступ к подписке\n", reply_markup=mark)
    elif callback.data == 'opl4':
        mark = tb.types.InlineKeyboardMarkup()
        mark.add(tb.types.InlineKeyboardButton('✅оплатить✅', callback_data='opl3'))
        bot.send_message(callback.message.chat.id, text="❌вы ещё не оплатили доступ к видео❌", reply_markup=mark)


bot.polling(none_stop=True)                                 
