from src import pencil_factory

def test_should_return_number_2hb_pencil():
    pencil = pencil_factory.get_no2_hb()

    assert pencil.point_durability == pencil_factory.NO2_HB_POINT_DURABILITY
    assert pencil.length == pencil_factory.NO2_HB_LENGTH
    assert pencil.eraser.durability == pencil_factory.NO2_HB_ERASER_DURABILITY
