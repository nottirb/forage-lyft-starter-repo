from unittest import TestCase

from engines.sternman_engine import SternmanEngine


class TestSternmanEngine(TestCase):
    def test_should_need_service(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())
        
    def test_should_not_need_service(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())
