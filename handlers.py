import asyncio

from aiogram import Dispatcher, F, types, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.enums.dice_emoji import DiceEmoji

from keyboards import keyboard_start

import config

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: types.Message):
    await message.reply(f'Привет, {message.from_user.first_name}!'
                        '\n\nЭтот бот открывает вам доступ к <b>ChatGPT, Google Sheets</b>'
                        '\n\n<b>Чатбот умеет:</b>'
                        '\n1.Ничего', reply_markup=keyboard_start)
    
@dp.message(F.text == '🎲 Сыграть')
async def command_play_dice(message: Message):
    x = await message.reply_dice(DiceEmoji.DICE)

    # TO DO::
    await config.bot.send_message(6623705141, f'Пользователь : @{message.from_user.username}'
                                  F'\nБросил кости : {x.dice.value}', )

# TO DO::
@dp.message(F.text == '👤 Профиль')
async def command_profile_info(message: Message):
    await message.reply(
        f'<b>Имя : </b> {message.from_user.first_name}\n'
        f'<b>ID : </b> {message.from_user.id}\n'
        f'<b>Username : </b> @{message.from_user.username}\n'
        f'<b>Статус : </b> Пользователь'
    )

async def main():
    # delete_webhook - пропускает сообщения, которые отправил пользователь, пока бот был выключен
    await config.bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(config.bot)
