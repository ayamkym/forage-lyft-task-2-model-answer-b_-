import unittest
from tire.octoprime_tires import OctoprimeTire
from tire.carrigan_tires import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.9, 0.4, 0.7]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.8, 0.8, 0.4, 0.7]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.9, 0.8, 0.7]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.5, 0.7, 0.6, 0.4]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
