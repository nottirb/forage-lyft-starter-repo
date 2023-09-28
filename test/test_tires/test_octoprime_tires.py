from unittest import TestCase

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(TestCase):
    def test_should_need_service(self):
        tire_wear = [0.75, 0.75, 0.75, 0.75]
        tire = OctoprimeTires(tire_wear)
        self.assertTrue(tire.needs_service())
        
    def test_should_not_need_service(self):
        tire_wear = [0.749, 0.75, 0.75, 0.75]
        tire = OctoprimeTires(tire_wear)
        self.assertFalse(tire.needs_service())
