from unittest import TestCase
from datetime import datetime

from batteries.nubbin_battery import NubbinBattery


class TestNubbinBattery(TestCase):
    def test_should_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_should_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 3)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
