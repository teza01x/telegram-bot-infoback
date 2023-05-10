import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from config import *


bot = AsyncTeleBot(token)


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, "Hello! I can help give full information about your account\n"
                                            "Write command /menu")


@bot.message_handler(commands=['menu'])
async def send_welcome(message):
    button_list = [
        types.InlineKeyboardButton(id_button, callback_data='button1'),
    ]
    reply_markup = types.InlineKeyboardMarkup([button_list])
    await bot.send_message(message.chat.id, menu_text, reply_markup=reply_markup)


@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    if call.data == "button1":
        await bot.answer_callback_query(call.id,)
        await bot.send_message(call.from_user.id, ("♦️YOUR INFO♦️\n"
                                        "🔘ID▪️ {}\n"
                                        "🔘First name▪️ {}\n"
                                        "🔘Last name▪️ {}\n"
                                        "🔘Username▪️ {}\n"
                                        "🔘Language▪️ {}").format(call.from_user.id, call.from_user.first_name, call.from_user.last_name,
                                                               call.from_user.username, call.from_user.language_code))


async def main():
    while True:
        try:
            await bot.send_message(chat_id=admin_chat_id, text="🤖 Bot started working")
            await bot.infinity_polling()
        except Exception as e:
            await bot.send_message(chat_id=admin_chat_id, text=f"⚠️ Bot has been crashed. Error: {str(e)}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()