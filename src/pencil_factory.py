from src.eraser import Eraser
from src.pencil import Pencil

NO2_HB_POINT_DURABILITY = 4860
NO2_HB_LENGTH = 44
NO2_HB_ERASER_DURABILITY = NO2_HB_LENGTH * NO2_HB_POINT_DURABILITY


def get_no2_hb():
    return Pencil(point_durability=NO2_HB_POINT_DURABILITY, length=NO2_HB_LENGTH,
                  eraser=Eraser(NO2_HB_ERASER_DURABILITY))
