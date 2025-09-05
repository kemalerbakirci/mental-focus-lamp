import random


class NoiseSensor:
    """
    Simulated noise sensor that returns random noise values in decibels (30-90 dB).
    This mimics a LibUPM sensor interface but uses random values for simulation.
    """
    
    def __init__(self):
        """Initialize the noise sensor."""
        pass
    
    def read_value(self) -> int:
        """
        Read noise level in decibels.
        
        Returns:
            int: Noise level between 30-90 dB
        """
        return random.randint(30, 90)