from config import utils_logger, Paths, Mode

import pypeec


def run_mesher(geometry_file, voxel_file):
    try:
        utils_logger.info("=== 🚀 Run mesh          ===")
        pypeec.run_mesher_file(file_geometry=geometry_file, file_voxel=voxel_file)
        utils_logger.info("=== ✅ End mesh          ===")
    except Exception as e:
        utils_logger.error(f"⛔ Error in mesh figure: {e}")


def run_viewer(voxel_file, viewer_file):
    try:
        utils_logger.info("=== 🚀 Running viewer   ===")
        pypeec.run_viewer_file(
            file_voxel=voxel_file,
            file_viewer=viewer_file,
            tag_plot=["domain", "voxelization", "adjacent"],
            plot_mode="qt",
        )
        utils_logger.info("=== ✅ End viewer        ===")
    except Exception as e:
        utils_logger.error(f"⛔ Error in viewer figure: {e}")


def run_solver(voxel_file, file_problem, file_tolerance, file_solution):
    try:
        utils_logger.info("=== 🚀 Run solver       ===")

        pypeec.run_solver_file(
            file_voxel=voxel_file,
            file_problem=file_problem,
            file_tolerance=file_tolerance,
            file_solution=file_solution,
        )
        utils_logger.info("=== ✅ End solver        ===")
    except Exception as e:
        utils_logger.error(f"⛔ Error in solver figure: {e}")


def run_plotter(file_solution, file_plotter):
    try:
        utils_logger.info("=== 🚀 Start plotter     ===")
        pypeec.run_plotter_file(
            file_solution=file_solution,
            file_plotter=file_plotter,
            tag_plot=["V_c_norm", "J_c_norm", "H_p_norm", "residuum"],
            plot_mode="qt",
        )
        utils_logger.info("=== ✅ End plotter run   ===")
    except Exception as e:
        utils_logger.error(f"⛔ Error in plotter figure: {e}")


def running_pypeec(paths: Paths, operatingMode: Mode):
    run_mesher(paths.geometry_file, paths.voxel_file)
    if operatingMode.viewer:
        run_viewer(paths.voxel_file, paths.viewer_file)
    else:
        utils_logger.info("===     Skip logger      ===")
    run_solver(
        paths.voxel_file, paths.file_problem, paths.file_tolerance, paths.file_solution
    )
    if operatingMode.plotter:
        run_plotter(paths.file_solution, paths.file_plotter)
    else:
        utils_logger.info("===     Skip plotter     ===")
