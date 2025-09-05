import unittest
import sys
import os

# Add the parent directory to sys.path to import project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sensors.noise_sensor import NoiseSensor


class TestNoiseSensor(unittest.TestCase):
    """Test cases for NoiseSensor class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.noise_sensor = NoiseSensor()
    
    def test_sensor_initialization(self):
        """Test that sensor initializes correctly."""
        self.assertIsInstance(self.noise_sensor, NoiseSensor)
    
    def test_read_value_type(self):
        """Test that read_value returns an integer."""
        value = self.noise_sensor.read_value()
        self.assertIsInstance(value, int)
    
    def test_read_value_range(self):
        """Test that read_value returns values within expected range (30-90 dB)."""
        for _ in range(100):  # Test multiple readings
            value = self.noise_sensor.read_value()
            self.assertGreaterEqual(value, 30, "Noise value should be >= 30 dB")
            self.assertLessEqual(value, 90, "Noise value should be <= 90 dB")
    
    def test_read_value_variability(self):
        """Test that read_value produces different values (not always the same)."""
        values = [self.noise_sensor.read_value() for _ in range(10)]
        # Check that we don't get the same value every time
        unique_values = set(values)
        self.assertGreater(len(unique_values), 1, "Sensor should produce varying values")


if __name__ == '__main__':
    unittest.main()
