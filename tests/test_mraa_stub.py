import unittest
import sys
import os
from io import StringIO

# Add the parent directory to sys.path to import project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stubs.mraa_stub import Gpio, DIR_OUT, DIR_IN


class TestMraaStub(unittest.TestCase):
    """Test cases for MRAA stub implementation."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Capture stdout to test printed messages
        self.held, sys.stdout = sys.stdout, StringIO()
        self.gpio = Gpio(13)
    
    def tearDown(self):
        """Clean up after each test method."""
        sys.stdout = self.held
    
    def test_gpio_initialization(self):
        """Test that GPIO initializes correctly."""
        self.assertIsInstance(self.gpio, Gpio)
        self.assertEqual(self.gpio.pin, 13)
    
    def test_gpio_direction_constants(self):
        """Test that direction constants are defined correctly."""
        self.assertEqual(DIR_OUT, 1)
        self.assertEqual(DIR_IN, 0)
    
    def test_gpio_direction_setting(self):
        """Test that GPIO direction can be set."""
        # Test output direction
        self.gpio.dir(DIR_OUT)
        self.assertEqual(self.gpio.direction, DIR_OUT)
        
        # Test input direction
        self.gpio.dir(DIR_IN)
        self.assertEqual(self.gpio.direction, DIR_IN)
    
    def test_gpio_write_operations(self):
        """Test that GPIO write operations work correctly."""
        # No exceptions should be raised
        self.gpio.write(1)
        self.gpio.write(0)
    
    def test_multiple_gpio_pins(self):
        """Test that multiple GPIO pins can be created."""
        gpio1 = Gpio(11)
        gpio2 = Gpio(12)
        gpio3 = Gpio(13)
        
        self.assertEqual(gpio1.pin, 11)
        self.assertEqual(gpio2.pin, 12)
        self.assertEqual(gpio3.pin, 13)


if __name__ == '__main__':
    unittest.main()
