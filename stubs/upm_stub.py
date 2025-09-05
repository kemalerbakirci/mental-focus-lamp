class Sensor:
    """
    Base class for UPM sensor stubs.
    Provides a standardized interface for sensor implementations.
    """
    
    def __init__(self):
        """Initialize the sensor."""
        pass
    
    def read_value(self):
        """
        Read sensor value. Should be overridden by child classes.
        
        Returns:
            Any: Sensor reading value
        """
        raise NotImplementedError("read_value() must be implemented by child classes")