import unittest

from .test_battery.test_nubbin_battery import TestNubbinBattery
from .test_battery.test_spindler_battery import TestSpindlerBattery
from .test_engine.test_capulet_engine import TestCapuletEngine
from .test_engine.test_sternman_engine import TestSternmanEngine
from .test_engine.test_willoughby_engine import TestWilloughbyEngine

if __name__ == '__main__':
    unittest.main()
