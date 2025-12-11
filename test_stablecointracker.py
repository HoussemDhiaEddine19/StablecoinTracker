# test_stablecointracker.py
"""
Tests for StablecoinTracker module.
"""

import unittest
from stablecointracker import StablecoinTracker

class TestStablecoinTracker(unittest.TestCase):
    """Test cases for StablecoinTracker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StablecoinTracker()
        self.assertIsInstance(instance, StablecoinTracker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StablecoinTracker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
