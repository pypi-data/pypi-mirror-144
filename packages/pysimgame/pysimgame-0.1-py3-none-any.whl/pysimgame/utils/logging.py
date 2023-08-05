import functools
import logging
from typing import Callable

import pygame
import pysimgame
from pygame_gui.ui_manager import UIManager
from pygame_gui.windows import UIMessageWindow

# Logging parameters
formatter = logging.Formatter(
    "%(asctime)s %(threadName)-10s %(name)s %(levelname)-8s %(message)s"
)
location_formatter = logging.Formatter(
    '"%(pathname)s", line %(lineno)d, in %(module)s %(funcName)s'
)
console = logging.StreamHandler()
console.setFormatter(formatter)
console2 = logging.StreamHandler()
console2.setFormatter(location_formatter)

logger = logging.getLogger(pysimgame.__name__)
logger.setLevel(pysimgame.LOGGING_LEVEL)


def register_logger(logger: logging.Logger):

    if logger.getEffectiveLevel() <= logging.DEBUG:
        # Puts the file and line number before the message if DEBUG
        logger.addHandler(console2)
    logger.addHandler(console)


register_logger(logger)


def logger_enter_exit(
    level: int = logging.DEBUG,
    with_args: bool = False,
    with_return: bool = False,
    ignore_enter: bool = False,
    ignore_exit: bool = False,
) -> Callable:
    """Decorate a function for logging when the function start and ends.

    Can also handle loggin the args and the return values.

    :param level: The level of logging to use, defaults to logging.DEBUG
    :param with_args: Whether to log args as well, defaults to False
    :param with_return: Whether to log return as well, defaults to False
    :param ignore_enter: Whether to ignore the enter statement, defaults to False
    :param ignore_exit: Whether to ignore the exit statement, defaults to False
    :return: the decorated function
    """

    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not ignore_enter:
                logger.log(
                    level,
                    f"[ENTER] {func.__module__}.{func.__name__} "
                    + (f"Args: {args}, Kwargs: {kwargs}" if with_args else ""),
                )
            ret = func(*args, **kwargs)
            if not ignore_exit:
                logger.log(
                    level,
                    f"[EXIT] {func.__module__}.{func.__name__} "
                    + (f"Return: {ret}" if with_return else ""),
                )
            return ret

        return wrapper

    return decorator


class PopUpHandler(logging.Handler):
    def __init__(
        self, ui_manager: UIManager, rect: pygame.Rect = None
    ) -> None:
        super().__init__()
        self.ui_manager = ui_manager
        if rect is None:
            x, y = self.ui_manager.window_resolution
            self.rect = pygame.Rect(x / 3, y / 3, x / 3, y / 3)
        elif isinstance(rect, pygame.Rect):
            self.rect = rect
        else:
            raise TypeError(
                f"rect kwarg must be pygame.Rect, not {type(rect)}."
            )

    def emit(self, record: logging.LogRecord) -> None:
        window = UIMessageWindow(
            self.rect,
            html_message=record.msg,
            manager=self.ui_manager,
            window_title="",
        )
