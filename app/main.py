from config import main_logger, Paths, Mode

from pathlib import Path
from utils import running_pypeec

# const
VIEWER = 0
PLOTTER = 1


main_logger.info("=== Creating paths ===")

current_path = Path(__file__).resolve().parent

geometry = current_path.parent / "figures" / "geometry.yaml"
viewer = current_path.parent / "other" / "config" / "viewer.yaml"
problem = current_path.parent / "figures" / "problem.yaml"
tolerance = current_path.parent / "other" / "config" / "tolerance.yaml"
plotter = current_path.parent / "other" / "config" / "plotter.yaml"

solution = current_path.parent / "other" / "solution.json.gz"
voxel = current_path.parent / "other" / "voxel.json.gz"


main_logger.info("=== Creating data for main ===")

paths_for_pypeec = Paths(geometry, voxel, viewer, solution, problem, tolerance, plotter)
mode = Mode(VIEWER, PLOTTER)


if __name__ == "__main__":
    running_pypeec(paths_for_pypeec, mode)
    main_logger.info("=== End ===")
