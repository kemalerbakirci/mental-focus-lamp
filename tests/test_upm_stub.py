import unittest
import sys
import os

# Add the parent directory to sys.path to import project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stubs.upm_stub import Sensor


class TestUpmStub(unittest.TestCase):
    """Test cases for UPM stub implementation."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.sensor = Sensor()
    
    def test_sensor_initialization(self):
        """Test that sensor initializes correctly."""
        self.assertIsInstance(self.sensor, Sensor)
    
    def test_read_value_not_implemented(self):
        """Test that base sensor raises NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            self.sensor.read_value()
    
    def test_sensor_inheritance(self):
        """Test that sensor can be inherited properly."""
        class TestSensor(Sensor):
            def read_value(self):
                return 42
        
        test_sensor = TestSensor()
        self.assertEqual(test_sensor.read_value(), 42)


if __name__ == '__main__':
    unittest.main()
