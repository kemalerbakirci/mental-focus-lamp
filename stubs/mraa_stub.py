# Constants for GPIO direction
DIR_OUT = 1
DIR_IN = 0


class Gpio:
    """
    Stub implementation of LibMRAA Gpio class.
    Instead of controlling real hardware, prints messages to simulate GPIO operations.
    """
    
    def __init__(self, pin: int):
        """
        Initialize GPIO pin.
        
        Args:
            pin (int): GPIO pin number
        """
        self.pin = pin
        self.direction = None
        print(f"GPIO {self.pin} initialized")
    
    def dir(self, mode: int):
        """
        Set GPIO direction.
        
        Args:
            mode (int): DIR_OUT or DIR_IN
        """
        self.direction = mode
        direction_str = "OUTPUT" if mode == DIR_OUT else "INPUT"
        print(f"GPIO {self.pin} set to {direction_str}")
    
    def write(self, value: int):
        """
        Write value to GPIO pin.
        
        Args:
            value (int): 0 for LOW, 1 for HIGH
        """
        state = "HIGH (LED ON)" if value == 1 else "LOW (LED OFF)"
        print(f"GPIO {self.pin} → {state}")