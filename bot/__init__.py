import bot.config as cfg


def _setup_bot_configuration():
    yml_config = cfg.load_yml_config()
    cfg.setup_tele_token(yml_config)
    cfg.setup_gpt_token(yml_config)


try:
    _setup_bot_configuration()
except Exception as error:
    cfg.LOGGER.critical(f"Error load configs: {error}")
