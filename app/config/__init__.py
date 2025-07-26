from .logger import setup_logger
from .types import Mode, Paths
from .paths import config_path, objects_path, creating_paths

main_logger = setup_logger("[main]")
utils_logger = setup_logger("[utils]")


__all__ = ["main_logger", "utils_logger", "Mode", "Paths", "config_path", "creating_paths", "objects_path"]
