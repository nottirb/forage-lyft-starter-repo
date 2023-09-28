from unittest import TestCase
from datetime import datetime

from batteries.spindler_battery import SpindlerBattery


class TestSpindlerBattery(TestCase):
    def test_should_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 4)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_should_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 3)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
