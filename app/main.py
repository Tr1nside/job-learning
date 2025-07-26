from config import main_logger, Paths, Mode, objects_path, creating_paths, config_path
from utils import running_processing, running_gui

from concurrent.futures import ThreadPoolExecutor


# const
main_logger.debug("=== Creating consts ===")

VIEWER = 0
PLOTTER = 1


# paths and mode
main_logger.debug("=== Creating const path and mode ===")

models_dirs = set()
for model_dir in objects_path.iterdir():
    if model_dir.is_dir() and model_dir !=  config_path:
        paths = creating_paths(model_dir)
        models_dirs.add(paths)


def process_dir(object_paths: Paths):
    main_logger.debug(f"=== Processing {object_paths.geometry_file.parent.name} ===")
    running_processing(object_paths)


def run_all_models_proccesing(objects_dirs: set):
    main_logger.debug("=== Run multiprocessing ===")
    with ThreadPoolExecutor() as executor:
        executor.map(process_dir, objects_dirs)
    
def run_all_models_gui(objects_dirs: set, mode: Mode = Mode(1, 0)):
    for dirs in objects_dirs:
        running_gui(dirs, mode)

if __name__ == "__main__":
    
    mode = Mode(VIEWER, PLOTTER)
    main_logger.info(f"=== Selected: \n=== Viewer = {mode.viewer} \n=== Plotter = {mode.plotter}")

    main_logger.info("=== Run proccesing models ===")
    run_all_models_proccesing(models_dirs)
    
    main_logger.info("=== Run GUI for models ===")
    run_all_models_gui(models_dirs, mode)

    main_logger.info("=== End ===")
