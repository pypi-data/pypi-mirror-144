from os import path
import pytest
import autoarray as aa
import autoarray.plot as aplt

import numpy as np

directory = path.dirname(path.realpath(__file__))


@pytest.fixture(name="plot_path")
def make_plot_path_setup():
    return path.join(
        "{}".format(path.dirname(path.realpath(__file__))), "files", "plots", "imaging"
    )


class TestMultiPlotter:
    def test__subplot_of_plotter_list_figure(self, imaging_7x7, plot_path, plot_patch):

        mat_plot_2d = aplt.MatPlot2D(output=aplt.Output(plot_path, format="png"))

        plotter_0 = aplt.ImagingPlotter(imaging=imaging_7x7, mat_plot_2d=mat_plot_2d)
        plotter_1 = aplt.ImagingPlotter(imaging=imaging_7x7)

        plotter_list = [plotter_0, plotter_1]

        multi_plotter = aplt.MultiFigurePlotter(plotter_list=plotter_list)
        multi_plotter.subplot_of_figure(func_name="figures_2d", figure_name="image")

        assert path.join(plot_path, "subplot_image_list.png") in plot_patch.paths

        plot_patch.paths = []

        multi_plotter = aplt.MultiFigurePlotter(plotter_list=plotter_list)
        multi_plotter.subplot_of_figure(
            func_name="figures_2d", figure_name="image", noise_map=True
        )

        assert path.join(plot_path, "subplot_image_list.png") in plot_patch.paths


class MockYX1DPlotter(aplt.YX1DPlotter):
    def __init__(
        self,
        y,
        x,
        mat_plot_1d: aplt.MatPlot1D = aplt.MatPlot1D(),
        visuals_1d: aplt.Visuals1D = aplt.Visuals1D(),
        include_1d: aplt.Include1D = aplt.Include1D(),
    ):

        super().__init__(
            y=y,
            x=x,
            mat_plot_1d=mat_plot_1d,
            visuals_1d=visuals_1d,
            include_1d=include_1d,
        )

    def figures_1d(self, figure_name=False):

        if figure_name:

            self.figure_1d()


class TestMultiYX1DPlotter:
    def test__subplot_of_plotter_list_figure(self, imaging_7x7, plot_path, plot_patch):

        mat_plot_1d = aplt.MatPlot1D(output=aplt.Output(plot_path, format="png"))

        plotter_0 = MockYX1DPlotter(
            y=aa.Array1D.manual_native([1.0, 2.0, 3.0], pixel_scales=1.0),
            x=aa.Array1D.manual_native([0.5, 1.0, 1.5], pixel_scales=0.5),
            mat_plot_1d=mat_plot_1d,
        )

        plotter_1 = MockYX1DPlotter(
            y=aa.Array1D.manual_native([1.0, 2.0, 4.0], pixel_scales=1.0),
            x=aa.Array1D.manual_native([0.5, 1.0, 1.5], pixel_scales=0.5),
            mat_plot_1d=mat_plot_1d,
        )

        plotter_list = [plotter_0, plotter_1]

        multi_plotter = aplt.MultiYX1DPlotter(plotter_list=plotter_list)
        multi_plotter.figure_1d(func_name="figures_1d", figure_name="figure_name")

        assert path.join(plot_path, "multi_figure_name.png") in plot_patch.paths
