import numpy as np
import autoarray as aa


def test__pix_indexes_for_sub_slim_index__matches_util(grid_2d_7x7):
    pixelization_grid = aa.Grid2D.manual_slim(
        [[0.1, 0.1], [1.1, 0.6], [2.1, 0.1], [0.4, 1.1], [1.1, 7.1], [2.1, 1.1]],
        shape_native=(3, 2),
        pixel_scales=1.0,
    )

    pixelization_grid = aa.Grid2DDelaunay(grid=pixelization_grid)

    mapper = aa.Mapper(
        source_grid_slim=grid_2d_7x7, source_pixelization_grid=pixelization_grid
    )

    simplex_index_for_sub_slim_index = mapper.delaunay.find_simplex(
        mapper.source_grid_slim
    )
    pix_indexes_for_simplex_index = mapper.delaunay.simplices

    pix_indexes_for_sub_slim_index_util, sizes = aa.util.mapper.pix_indexes_for_sub_slim_index_delaunay_from(
        source_grid_slim=mapper.source_grid_slim,
        simplex_index_for_sub_slim_index=simplex_index_for_sub_slim_index,
        pix_indexes_for_simplex_index=pix_indexes_for_simplex_index,
        delaunay_points=mapper.delaunay.points,
    )
    pix_indexes_for_sub_slim_index_util = pix_indexes_for_sub_slim_index_util.astype(
        "int"
    )
    sizes = sizes.astype("int")

    assert (
        mapper.pix_indexes_for_sub_slim_index == pix_indexes_for_sub_slim_index_util
    ).all()
    assert (mapper.pix_sizes_for_sub_slim_index == sizes).all()

    assert (
        mapper.pix_indexes_for_sub_slim_index
        == np.array(
            [
                [0, -1, -1],
                [1, -1, -1],
                [1, 5, 3],
                [0, -1, -1],
                [0, -1, -1],
                [3, -1, -1],
                [0, -1, -1],
                [0, -1, -1],
                [3, -1, -1],
            ]
        )
    ).all()

    assert (
        mapper.pix_sizes_for_sub_slim_index == np.array([1, 1, 3, 1, 1, 1, 1, 1, 1])
    ).all()
