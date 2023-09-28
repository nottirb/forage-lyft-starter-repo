from unittest import TestCase

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(TestCase):
    def test_should_need_service(self):
        tire_wear = [0.5, 0.9, 0.8, 0.2]
        tire = CarriganTires(tire_wear)
        self.assertTrue(tire.needs_service())
        
    def test_should_not_need_service(self):
        tire_wear = [0.5, 0.899, 0.8, 0.1]
        tire = CarriganTires(tire_wear)
        self.assertFalse(tire.needs_service())
