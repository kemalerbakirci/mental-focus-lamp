import random


class HeartbeatSensor:
    """
    Simulated heartbeat sensor that returns random heart rate values (60-120 bpm).
    This mimics a LibUPM sensor interface and is used to check if a student is stressed or calm.
    """
    
    def __init__(self):
        """Initialize the heartbeat sensor."""
        pass
    
    def read_value(self) -> int:
        """
        Read heart rate in beats per minute.
        
        Returns:
            int: Heart rate between 60-120 bpm
        """
        return random.randint(60, 120)