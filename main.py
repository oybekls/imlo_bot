import logging

from aiogram import Dispatcher, Bot, executor, types
from checkWord import checkWord

API_TOKEN = "6200529681:AAH-4DcJ-FV1tPYmf2lnGzgWozUffgZkF7Y"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    await message.reply("Imlo botga xush kelibsiz")
@dp.message_handler(commands="help")
async def help_user(message: types.Message):
    await message.reply("Bot sizga yuborgan so'zingizdagi xatolarni chiqarib beradi. Biron so'z yuboring!")
@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    print(result)
    if result["available"]:
        responce = f"✅️ {word.capitalize()}"
    else:
        responce = f"❌️ {word.capitalize()}\n"
        for text in result["matches"]:
            responce += f"✅️ {text.capitalize()}\n"
    await message.answer(responce)

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)


