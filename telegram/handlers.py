from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
import multiprocessing
from bybit_module.bybit_main import make_orderbook_bybit
from mexs_module.mexx_main import get_tickers_mexs
from okx_module.okx_main import make_tickers_okx
import asyncio

router = Router()  # [1]


@router.message(Command("start"))
async def send_message(message: Message):
    await message.reply("Hi i'm CryptoScaner, use /run to look at pairs")


@router.message(Command("help"))
async def send_welcome(message: Message):
    await message.reply("Hi! Use /run to execute functions.")


@router.message(Command("run"))
async def run_functions(message: Message, bot: Bot):
    process = multiprocessing.Process(target=execute_and_send, args=(message.chat.id, Bot, ))
    process.start()


def worker_function(func):
    try:
        result = func()
        return result
    except Exception as e:
        return str(e)


def execute_and_send(chat_id: int, bot: Bot):
    functions = [make_orderbook_bybit, get_tickers_mexs, make_tickers_okx]
    with multiprocessing.Pool(processes=len(functions)) as pool:
        results = pool.map(worker_function, functions)
        print(results[0])
        result_message = "\n".join([f"Function {i + 1} result:" for i in range(len(functions))])
    bot.send_message(chat_id=chat_id, text=result_message)
