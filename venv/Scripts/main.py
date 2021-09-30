import aiogram
from Ping import Ping_IP
from Read_config import TOKEN, time_connect, chat_id, data_turnstile, turnstile_list
import asyncio

# 329051835

bot = aiogram.Bot(TOKEN)
dp = aiogram.Dispatcher(bot)
ping = Ping_IP()
last_ping_DOWN = []

@dp.message_handler(commands=['start'])
async def send_welcome(message: aiogram.types.Message):
    print(message.chat.id)
    await   message.answer("Привэт!")
    message.chat.id

@dp.message_handler(commands=['all'])
async def send_welcome(message: aiogram.types.Message):
    await   message.answer(ping.status_ping(data_turnstile, turnstile_list))


@dp.message_handler(commands=['up'])
async def send_welcome(message: aiogram.types.Message):
    await   message.answer(ping.statusUP_ping(data_turnstile, turnstile_list))

@dp.message_handler(commands=['down'])
async def send_welcome(message: aiogram.types.Message):
    await   message.answer(ping.statusDOWN_ping(data_turnstile, turnstile_list))



async def sendMessage(chat_id, time_connect, last_ping_DOWN, numberErrorConnect, errorConnect):
    while True:
        await asyncio.sleep(time_connect)

        new_ping_DOWN = ping.statusDOWN_ping(data_turnstile, turnstile_list)
        if new_ping_DOWN:
            for i in new_ping_DOWN:
                if i in last_ping_DOWN:
                    continue
                else:
                    for j in chat_id:
                        await bot.send_message(j, i)
        last_ping_DOWN = new_ping_DOWN



if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.create_task(sendMessage(chat_id, time_connect, last_ping_DOWN, data_turnstile, turnstile_list))
    aiogram.executor.start_polling(dp, skip_updates=True)