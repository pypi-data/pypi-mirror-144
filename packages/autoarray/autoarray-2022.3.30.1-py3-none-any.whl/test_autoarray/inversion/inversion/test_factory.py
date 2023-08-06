import numpy as np
import pytest

import autoarray as aa

# TODO : NEed to figure out how we blur linear light profile with blurring gird.


def test__inversion_imaging__via_linear_obj_func(masked_imaging_7x7_no_blur):

    mask = masked_imaging_7x7_no_blur.mask

    grid = aa.Grid2D.from_mask(mask=mask)

    linear_obj = aa.m.MockLinearObjFunc(
        grid=grid, mapping_matrix=np.full(fill_value=0.5, shape=(9, 1))
    )

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[linear_obj],
        settings=aa.SettingsInversion(use_w_tilde=False, check_solution=False),
    )

    assert isinstance(inversion.linear_obj_list[0], aa.m.MockLinearObjFunc)
    assert isinstance(inversion.leq, aa.LEqImagingMapping)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[linear_obj],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.linear_obj_list[0], aa.m.MockLinearObjFunc)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)


def test__inversion_imaging__via_mapper(
    masked_imaging_7x7_no_blur,
    rectangular_mapper_7x7_3x3,
    delaunay_mapper_9_3x3,
    voronoi_mapper_9_3x3,
    regularization_constant,
):

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[rectangular_mapper_7x7_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=False, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperRectangularNoInterp)
    assert isinstance(inversion.leq, aa.LEqImagingMapping)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(6.9546, 1.0e-4)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[rectangular_mapper_7x7_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperRectangularNoInterp)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(6.9546, 1.0e-4)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[delaunay_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=False, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperDelaunay)
    assert isinstance(inversion.leq, aa.LEqImagingMapping)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(10.6674, 1.0e-4)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[delaunay_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperDelaunay)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(10.6674, 1.0e-4)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=False, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoiNoInterp)
    assert isinstance(inversion.leq, aa.LEqImagingMapping)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(10.6763, 1.0e-4)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoiNoInterp)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(10.6763, 1.0e-4)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)


def test__inversion_imaging__via_regularizations(
    masked_imaging_7x7_no_blur,
    delaunay_mapper_9_3x3,
    voronoi_mapper_9_3x3,
    voronoi_mapper_nn_9_3x3,
    regularization_constant,
    regularization_constant_split,
    regularization_adaptive_brightness,
    regularization_adaptive_brightness_split,
):

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[delaunay_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperDelaunay)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        10.66747, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[delaunay_mapper_9_3x3],
        regularization_list=[regularization_constant_split],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperDelaunay)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        10.52745, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[delaunay_mapper_9_3x3],
        regularization_list=[regularization_adaptive_brightness],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperDelaunay)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        47.410169, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[delaunay_mapper_9_3x3],
        regularization_list=[regularization_adaptive_brightness_split],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperDelaunay)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        38.956734, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoiNoInterp)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(10.6763, 1.0e-4)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_9_3x3],
        regularization_list=[regularization_constant_split],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoiNoInterp)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        10.38417, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_9_3x3],
        regularization_list=[regularization_adaptive_brightness],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoiNoInterp)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        -25.71476, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_9_3x3],
        regularization_list=[regularization_adaptive_brightness_split],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoiNoInterp)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        -26.31747, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_nn_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoi)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        10.66505, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_nn_9_3x3],
        regularization_list=[regularization_constant_split],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoi)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        10.37955, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_nn_9_3x3],
        regularization_list=[regularization_adaptive_brightness],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoi)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        49.63744, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[voronoi_mapper_nn_9_3x3],
        regularization_list=[regularization_adaptive_brightness_split],
        settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoi)
    assert isinstance(inversion.leq, aa.LEqImagingWTilde)
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        34.90782, 1.0e-4
    )
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)


def test__inversion_imaging__compare_mapping_and_w_tilde_values(
    masked_imaging_7x7, voronoi_mapper_9_3x3, regularization_constant
):

    inversion_w_tilde = aa.Inversion(
        dataset=masked_imaging_7x7,
        linear_obj_list=[voronoi_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=True),
    )

    inversion_mapping = aa.Inversion(
        dataset=masked_imaging_7x7,
        linear_obj_list=[voronoi_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=False),
    )

    assert inversion_w_tilde.reconstruction == pytest.approx(
        inversion_mapping.reconstruction, 1.0e-4
    )
    assert inversion_w_tilde.mapped_reconstructed_image == pytest.approx(
        inversion_mapping.mapped_reconstructed_image, 1.0e-4
    )
    assert (
        inversion_w_tilde.log_det_curvature_reg_matrix_term
        == inversion_mapping.log_det_curvature_reg_matrix_term
    )


def test__inversion_interferometer__via_mapper(
    interferometer_7_no_fft,
    rectangular_mapper_7x7_3x3,
    delaunay_mapper_9_3x3,
    voronoi_mapper_9_3x3,
    regularization_constant,
):

    inversion = aa.Inversion(
        dataset=interferometer_7_no_fft,
        linear_obj_list=[rectangular_mapper_7x7_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=False, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperRectangularNoInterp)
    assert isinstance(inversion.leq, aa.LEqInterferometerMapping)
    assert inversion.mapped_reconstructed_data == pytest.approx(
        1.0 + 0.0j * np.ones(shape=(7,)), 1.0e-4
    )
    assert (np.imag(inversion.mapped_reconstructed_data) < 0.0001).all()
    assert (np.imag(inversion.mapped_reconstructed_data) > 0.0).all()
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(10.2116, 1.0e-4)

    inversion = aa.Inversion(
        dataset=interferometer_7_no_fft,
        linear_obj_list=[delaunay_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=False, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperDelaunay)
    assert isinstance(inversion.leq, aa.LEqInterferometerMapping)
    assert inversion.mapped_reconstructed_data == pytest.approx(
        1.0 + 0.0j * np.ones(shape=(7,)), 1.0e-4
    )
    assert (np.imag(inversion.mapped_reconstructed_data) < 0.0001).all()
    assert (np.imag(inversion.mapped_reconstructed_data) > 0.0).all()
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
        14.49772, 1.0e-4
    )

    inversion = aa.Inversion(
        dataset=interferometer_7_no_fft,
        linear_obj_list=[voronoi_mapper_9_3x3],
        regularization_list=[regularization_constant],
        settings=aa.SettingsInversion(use_w_tilde=False, check_solution=False),
    )

    assert isinstance(inversion.mapper_list[0], aa.MapperVoronoiNoInterp)
    assert isinstance(inversion.leq, aa.LEqInterferometerMapping)
    assert inversion.mapped_reconstructed_data == pytest.approx(
        1.0 + 0.0j * np.ones(shape=(7,)), 1.0e-4
    )
    assert (np.imag(inversion.mapped_reconstructed_data) < 0.0001).all()
    assert (np.imag(inversion.mapped_reconstructed_data) > 0.0).all()
    assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(14.4977, 1.0e-4)


def test__inversion_matrices__x2_mappers(
    masked_imaging_7x7_no_blur,
    rectangular_mapper_7x7_3x3,
    voronoi_mapper_9_3x3,
    regularization_constant,
):

    inversion = aa.Inversion(
        dataset=masked_imaging_7x7_no_blur,
        linear_obj_list=[rectangular_mapper_7x7_3x3, voronoi_mapper_9_3x3],
        regularization_list=[regularization_constant, regularization_constant],
        settings=aa.SettingsInversion(check_solution=False),
    )

    assert (
        inversion.operated_mapping_matrix[0:9, 0:9]
        == rectangular_mapper_7x7_3x3.mapping_matrix
    ).all()
    assert (
        inversion.operated_mapping_matrix[0:9, 9:18]
        == voronoi_mapper_9_3x3.mapping_matrix
    ).all()

    blurred_mapping_matrix = np.hstack(
        [rectangular_mapper_7x7_3x3.mapping_matrix, voronoi_mapper_9_3x3.mapping_matrix]
    )

    assert inversion.operated_mapping_matrix == pytest.approx(
        blurred_mapping_matrix, 1.0e-4
    )

    curvature_matrix = aa.util.leq.curvature_matrix_via_mapping_matrix_from(
        mapping_matrix=blurred_mapping_matrix, noise_map=inversion.noise_map
    )

    assert inversion.curvature_matrix == pytest.approx(curvature_matrix, 1.0e-4)

    regularization_matrix_of_reg_0 = regularization_constant.regularization_matrix_from(
        mapper=rectangular_mapper_7x7_3x3
    )
    regularization_matrix_of_reg_1 = regularization_constant.regularization_matrix_from(
        mapper=voronoi_mapper_9_3x3
    )

    assert (
        inversion.regularization_matrix[0:9, 0:9] == regularization_matrix_of_reg_0
    ).all()
    assert (
        inversion.regularization_matrix[9:18, 9:18] == regularization_matrix_of_reg_1
    ).all()
    assert (inversion.regularization_matrix[0:9, 9:18] == np.zeros((9, 9))).all()
    assert (inversion.regularization_matrix[9:18, 0:9] == np.zeros((9, 9))).all()

    reconstruction_0 = 0.5 * np.ones(9)
    reconstruction_1 = 0.5 * np.ones(9)

    assert inversion.reconstruction_dict[rectangular_mapper_7x7_3x3] == pytest.approx(
        reconstruction_0, 1.0e-4
    )
    assert inversion.reconstruction_dict[voronoi_mapper_9_3x3] == pytest.approx(
        reconstruction_1, 1.0e-4
    )
    assert inversion.reconstruction == pytest.approx(
        np.concatenate([reconstruction_0, reconstruction_1]), 1.0e-4
    )

    assert inversion.mapped_reconstructed_data_dict[
        rectangular_mapper_7x7_3x3
    ] == pytest.approx(0.5 * np.ones(9), 1.0e-4)
    assert inversion.mapped_reconstructed_data_dict[
        voronoi_mapper_9_3x3
    ] == pytest.approx(0.5 * np.ones(9), 1.0e-4)
    assert inversion.mapped_reconstructed_image == pytest.approx(np.ones(9), 1.0e-4)
