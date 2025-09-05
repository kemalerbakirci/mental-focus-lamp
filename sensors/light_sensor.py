import random


class LightSensor:
    """
    Simulated light sensor that returns random light intensity values in lux (50-500).
    This mimics a LibUPM sensor interface but uses random values for simulation.
    """
    
    def __init__(self):
        """Initialize the light sensor."""
        pass
    
    def read_value(self) -> int:
        """
        Read light intensity in lux.
        
        Returns:
            int: Light intensity between 50-500 lux
        """
        return random.randint(50, 500)