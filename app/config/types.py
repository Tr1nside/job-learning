from pathlib import Path
from dataclasses import dataclass


@dataclass
class Paths:
    geometry_file: Path
    voxel_file: Path
    viewer_file: Path
    file_solution: Path
    file_problem: Path
    file_tolerance: Path
    file_plotter: Path


@dataclass
class Mode:
    viewer: bool
    plotter: bool
