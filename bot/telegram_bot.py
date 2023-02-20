import telebot
import bot.config as cfg
from bot.utils import create_logger
from .chat_gpt.client import GPTClient

LOGGER = create_logger(__name__)

BOT = telebot.TeleBot(cfg.TELE_TOKEN)


@BOT.message_handler(commands=['start'])
def handle_start(message):
    LOGGER.info(f"Handle start message from user: {message.from_user.username} {message.from_user.id}")
    BOT.send_message(message.from_user.id, "Привет я прокси chat_gpt. Задай свой вопрос")


@BOT.message_handler(content_types=['text'])
def handle_text_message(message):
    LOGGER.info(f"Handle text message from user: {message.from_user.username} {message.from_user.id} -> {message.text}")
    try:
        client = GPTClient(cfg.DEFAULT_MODEL, cfg.DEFAULT_MAX_TOKENS, cfg.DEFAULT_TEMPERATURE)
        answer = client.send(message.text)
        LOGGER.info(f"Answer to user {message.from_user.id} is success")
        BOT.send_message(message.from_user.id, f"Ответ бота: {answer}")
    except Exception as error:
        LOGGER.error(f"User id: {message.from_user.id}, GPT service error: {error}")
        BOT.send_message(message.from_user.id, "Задайте вопрос чуть позже сервис сейчас не достпен")


def bot_start():
    BOT.infinity_polling()
