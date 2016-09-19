import logging


def info(msg, *args, **kwargs):
    return logger.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    return logger.warning(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    ch.setFormatter(logging.Formatter('%(name)s-%(levelname)s-%(message)s'))
    logger.addHandler(ch)
    return logger.debug(msg, *args, **kwargs)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s'))
logger.addHandler(ch)
