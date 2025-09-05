import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the parent directory to sys.path to import project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controllers.lamp_controller import LampController


class TestLampController(unittest.TestCase):
    """Test cases for LampController class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Capture stdout to prevent GPIO messages during testing
        self.held, sys.stdout = sys.stdout, StringIO()
        self.lamp_controller = LampController()
    
    def tearDown(self):
        """Clean up after each test method."""
        sys.stdout = self.held
    
    def test_controller_initialization(self):
        """Test that controller initializes correctly."""
        self.assertIsInstance(self.lamp_controller, LampController)
        self.assertIsNone(self.lamp_controller.current_state)
    
    def test_red_conditions(self):
        """Test that RED conditions trigger correctly."""
        # Test high noise condition
        self.lamp_controller.update(noise=75, light=400, heartbeat=70)
        self.assertEqual(self.lamp_controller.get_current_state(), "RED")
        
        # Test low light condition
        self.lamp_controller.update(noise=40, light=100, heartbeat=70)
        self.assertEqual(self.lamp_controller.get_current_state(), "RED")
        
        # Test high heartbeat condition
        self.lamp_controller.update(noise=40, light=400, heartbeat=110)
        self.assertEqual(self.lamp_controller.get_current_state(), "RED")
    
    def test_yellow_conditions(self):
        """Test that YELLOW conditions trigger correctly."""
        # Test moderate noise condition
        self.lamp_controller.update(noise=60, light=400, heartbeat=70)
        self.assertEqual(self.lamp_controller.get_current_state(), "YELLOW")
        
        # Test moderate light condition
        self.lamp_controller.update(noise=40, light=200, heartbeat=70)
        self.assertEqual(self.lamp_controller.get_current_state(), "YELLOW")
        
        # Test moderate heartbeat condition
        self.lamp_controller.update(noise=40, light=400, heartbeat=95)
        self.assertEqual(self.lamp_controller.get_current_state(), "YELLOW")
    
    def test_green_conditions(self):
        """Test that GREEN conditions trigger correctly."""
        # Test optimal conditions
        self.lamp_controller.update(noise=30, light=400, heartbeat=70)
        self.assertEqual(self.lamp_controller.get_current_state(), "GREEN")
        
        # Test boundary conditions for green
        self.lamp_controller.update(noise=50, light=300, heartbeat=90)
        self.assertEqual(self.lamp_controller.get_current_state(), "GREEN")
    
    def test_priority_red_over_yellow(self):
        """Test that RED conditions take priority over YELLOW."""
        # Mixed conditions where RED should take priority
        self.lamp_controller.update(noise=75, light=250, heartbeat=95)
        self.assertEqual(self.lamp_controller.get_current_state(), "RED")
    
    def test_state_changes(self):
        """Test that state changes are tracked correctly."""
        # Start with green
        self.lamp_controller.update(noise=30, light=400, heartbeat=70)
        self.assertEqual(self.lamp_controller.get_current_state(), "GREEN")
        
        # Change to yellow
        self.lamp_controller.update(noise=60, light=400, heartbeat=70)
        self.assertEqual(self.lamp_controller.get_current_state(), "YELLOW")
        
        # Change to red
        self.lamp_controller.update(noise=80, light=400, heartbeat=70)
        self.assertEqual(self.lamp_controller.get_current_state(), "RED")


if __name__ == '__main__':
    unittest.main()
