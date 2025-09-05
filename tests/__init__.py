"""
Mental Focus Desk Lamp - Test Suite

This module contains the complete test suite for the Mental Focus Desk Lamp project.
Run all tests using: python -m pytest tests/ or python -m unittest discover tests/
"""

import unittest
import sys
import os

# Add the parent directory to sys.path to import project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import all test modules
from test_noise_sensor import TestNoiseSensor
from test_light_sensor import TestLightSensor
from test_heartbeat_sensor import TestHeartbeatSensor
from test_lamp_controller import TestLampController
from test_mraa_stub import TestMraaStub
from test_upm_stub import TestUpmStub


def create_test_suite():
    """Create a test suite containing all test cases."""
    test_suite = unittest.TestSuite()
    
    # Add sensor tests
    test_suite.addTest(unittest.makeSuite(TestNoiseSensor))
    test_suite.addTest(unittest.makeSuite(TestLightSensor))
    test_suite.addTest(unittest.makeSuite(TestHeartbeatSensor))
    
    # Add controller tests
    test_suite.addTest(unittest.makeSuite(TestLampController))
    
    # Add stub tests
    test_suite.addTest(unittest.makeSuite(TestMraaStub))
    test_suite.addTest(unittest.makeSuite(TestUpmStub))
    
    return test_suite


def run_all_tests():
    """Run all tests and return the results."""
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = create_test_suite()
    result = runner.run(test_suite)
    return result


if __name__ == '__main__':
    print("🧪 Mental Focus Desk Lamp - Running All Tests")
    print("=" * 50)
    
    result = run_all_tests()
    
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print(f"❌ {len(result.failures)} test(s) failed")
        print(f"🔥 {len(result.errors)} test(s) had errors")
