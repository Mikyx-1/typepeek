import logging


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    cyan = "\x1b[36;20m"
    green = "\x1b[32;20m"
    bright_white = "\x1b[97;20m"
    blue = "\x1b[34;20m"
    bold_blue = "\x1b[1;34;20m"
    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: bold_blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logger(name="My_app", level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setLevel(level)

    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)
    return logger
