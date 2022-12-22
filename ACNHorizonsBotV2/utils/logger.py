from logging.config import dictConfig
from logging import Logger, getLogger, INFO
import logging
from typing import Any, Dict

class TweetLogger:
    """
    Class used to log information collected by the twitter Bot.

    Fields:
        logger
    
    Methods:
        debug()

        info()

        warning()

        error()

        critical()
    """
    logger: Logger

    def __init__(self) -> None:
        dictConfig(self.__get_logging_config())
        self.logger = getLogger()
    
    def debug(self, msg: Any, *args, **kwargs) -> None:
        self.logger.debug(msg, *args, **kwargs)
    
    def info(self, msg: Any, *args, **kwargs) -> None:
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg: Any, *args, **kwargs) -> None:
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg: Any, *args, **kwargs) -> None:
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg: Any, *args, **kwargs) -> None:
        self.logger.critical(msg, *args, **kwargs)

    def __get_logging_config(self) -> Dict[str, Any]:
        return dict(
            version = 1,
            formatters = {
                'f': {'format': '%(asctime)s %(name)s [%(levelname)s]: %(message)s'}
                },
            handlers = {
                'h': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'f',
                    'level': INFO}
                },
            root = {
                'handlers': ['h'],
                'level': INFO,
                },
        )

tweet_logger = TweetLogger()