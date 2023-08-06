import autoarray as aa


class TestRegression:
    def test__grid_is_relocated_via_border(self, sub_grid_2d_7x7):
        pixelization = aa.pix.VoronoiMagnification(shape=(3, 3))

        mask = aa.Mask2D.circular(
            shape_native=(60, 60),
            radius=1.0,
            pixel_scales=(0.1, 0.1),
            centre=(1.0, 1.0),
            sub_size=1,
        )

        grid = aa.Grid2D.from_mask(mask=mask)

        sparse_grid = pixelization.data_pixelization_grid_from(data_grid_slim=grid)

        grid[8, 0] = 100.0

        mapper = pixelization.mapper_from(
            source_grid_slim=grid,
            source_pixelization_grid=sparse_grid,
            settings=aa.SettingsPixelization(use_border=True),
        )

        assert grid[8, 0] != mapper.source_grid_slim[8, 0]
        assert mapper.source_grid_slim[8, 0] < 5.0

        grid[0, 0] = 0.0
        sparse_grid[0, 0] = 100.0

        mapper = pixelization.mapper_from(
            source_grid_slim=grid,
            source_pixelization_grid=sparse_grid,
            settings=aa.SettingsPixelization(use_border=True),
        )

        assert isinstance(mapper, aa.MapperVoronoiNoInterp)
        assert sparse_grid[0, 0] != mapper.source_pixelization_grid[0, 0]
        assert mapper.source_pixelization_grid[0, 0] < 5.0

        pixelization = aa.pix.VoronoiNNMagnification(shape=(3, 3))

        mapper = pixelization.mapper_from(
            source_grid_slim=grid,
            source_pixelization_grid=sparse_grid,
            settings=aa.SettingsPixelization(use_border=True),
        )

        assert isinstance(mapper, aa.MapperVoronoi)
        assert sparse_grid[0, 0] != mapper.source_pixelization_grid[0, 0]
        assert mapper.source_pixelization_grid[0, 0] < 5.0
