import unittest
from src import pencil_factory


class Number2HBPencilFactoryTests(unittest.TestCase):
    def test_should_return_number_2hb_pencil(self):
        pencil = pencil_factory.get_no2_hb()

        self.assertEqual(pencil.point_durability,
                         pencil_factory.NO2_HB_POINT_DURABILITY)
        self.assertEqual(pencil.length, pencil_factory.NO2_HB_LENGTH)
        self.assertEqual(pencil.eraser.durability,
                         pencil_factory.NO2_HB_ERASER_DURABILITY)
