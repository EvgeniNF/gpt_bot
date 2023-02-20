import sys
import yaml
from .utils import create_logger

CONFIG_PATH = sys.path[1] + "/config/bot.config.yaml"
LOGGER = create_logger(__name__)

TELE_TOKEN = None

GPT_TOKEN = None
LIST_MODELS = [
    "text-davinci-003",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001"
]
DEFAULT_MODEL = "text-davinci-003"
DEFAULT_TEMPERATURE = 0.5
DEFAULT_MAX_TOKENS = 1000


def load_yml_config():
    LOGGER.info(f"Load configuration from: {CONFIG_PATH}")
    with open(CONFIG_PATH, 'r') as file:
        file = yaml.safe_load(file)
        return file


def setup_tele_token(yml_config):
    global TELE_TOKEN
    TELE_TOKEN = yml_config["TelegramBotConfig"]["token"]
    LOGGER.info(f"Setup telegram token as: {TELE_TOKEN}")


def setup_gpt_token(yml_config):
    global GPT_TOKEN
    GPT_TOKEN = yml_config["GPTConfig"]["token"]
    LOGGER.info(f"Setup gpt token as: {GPT_TOKEN}")

