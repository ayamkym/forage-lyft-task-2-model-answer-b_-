import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_needs_service_true(self):
        current_date = datetime(2024, 6, 1)
        last_service_date = datetime(2019, 5, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_needs_service_false(self):
        current_date = datetime(2024, 6, 1)
        last_service_date = datetime(2021, 5, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_needs_service_true(self):
        current_date = datetime(2024, 6, 1)
        last_service_date = datetime(2021, 5, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_needs_service_false(self):
        current_date = datetime(2024, 6, 1)
        last_service_date = datetime(2023, 5, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
