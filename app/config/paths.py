from config import Paths

from pathlib import Path

current_path = Path(__file__).resolve().parent.parent
config_path = current_path.parent / 'figures' / 'config'
objects_path = current_path.parent / 'figures'


def creating_paths(dir):
    output_dir = dir / "out"
    output_dir.mkdir(parents=True, exist_ok=True)

    geometry = dir / "geometry.yaml"
    problem = dir / "problem.yaml"
    viewer = config_path / "viewer.yaml"
    tolerance = config_path / "tolerance.yaml"
    plotter = config_path / "plotter.yaml"
    solution = output_dir / "solution.json.gz"
    voxel = output_dir / "voxel.json.gz"

    object_paths = Paths(geometry, voxel, viewer, solution, problem, tolerance, plotter)
    
    return object_paths
