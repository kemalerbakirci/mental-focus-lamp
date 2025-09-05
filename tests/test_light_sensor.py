import unittest
import sys
import os

# Add the parent directory to sys.path to import project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sensors.light_sensor import LightSensor


class TestLightSensor(unittest.TestCase):
    """Test cases for LightSensor class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.light_sensor = LightSensor()
    
    def test_sensor_initialization(self):
        """Test that sensor initializes correctly."""
        self.assertIsInstance(self.light_sensor, LightSensor)
    
    def test_read_value_type(self):
        """Test that read_value returns an integer."""
        value = self.light_sensor.read_value()
        self.assertIsInstance(value, int)
    
    def test_read_value_range(self):
        """Test that read_value returns values within expected range (50-500 lux)."""
        for _ in range(100):  # Test multiple readings
            value = self.light_sensor.read_value()
            self.assertGreaterEqual(value, 50, "Light value should be >= 50 lux")
            self.assertLessEqual(value, 500, "Light value should be <= 500 lux")
    
    def test_read_value_variability(self):
        """Test that read_value produces different values (not always the same)."""
        values = [self.light_sensor.read_value() for _ in range(10)]
        # Check that we don't get the same value every time
        unique_values = set(values)
        self.assertGreater(len(unique_values), 1, "Sensor should produce varying values")


if __name__ == '__main__':
    unittest.main()
