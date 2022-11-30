import logging


def create_logger():
    """Create logger that only outputs statements to console"""
    logger = logging.getLogger('app')
    # set verbosity to show msgs whose severity >= INFO
    logger.setLevel(logging.INFO)  # or 'INFO' 

    console = logging.StreamHandler()
    logger.addHandler(console)

    return logger

log = create_logger()