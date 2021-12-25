import logging


class MyFormat(logging.Formatter):
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    green = "\x1b[32m"
    asctime = "%(asctime)s"
    name = "[%(name)s]"
    levelname = "[%(levelname)-4s]"
    msg = "%(message)s"

    FORMATS = {
        logging.DEBUG: f"{asctime} {grey} {name} {levelname} {reset} {msg}",
        logging.INFO: f"{asctime} {green} {name} {levelname} {reset} {msg}",
        logging.WARNING: f"{asctime} {yellow} {name} {levelname} {msg}",
        logging.ERROR: f"{asctime} {red} {name} {levelname} {msg} {reset}",
        logging.CRITICAL: f"{asctime} {bold_red} {name} {levelname} {msg}",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logging(mod_name: str) -> logging.Logger:
    log = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    handler.setFormatter(MyFormat())
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    return log
