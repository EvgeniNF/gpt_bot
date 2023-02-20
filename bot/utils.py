import logging


def create_logger(name_logger: str):
    log_format = f"%(asctime)s -> [%(levelname)s] [%(name)s] - %(message)s"
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(log_format))

    logger = logging.getLogger(name_logger)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
