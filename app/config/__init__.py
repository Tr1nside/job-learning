from .logger import setup_logger
from .types import Mode, Paths

main_logger = setup_logger("[main]")
utils_logger = setup_logger("[utils]")


__all__ = ["main_logger", "utils_logger", "Mode", "Paths"]
