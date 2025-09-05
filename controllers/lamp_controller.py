from stubs.mraa_stub import Gpio, DIR_OUT


class LampController:
    """
    Controls an RGB LED lamp using GPIO pins.
    Uses decision rules based on sensor readings to determine lamp color.
    """
    
    # LED states
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"
    
    def __init__(self, red_pin: int = 11, green_pin: int = 12, yellow_pin: int = 13):
        """
        Initialize the lamp controller with GPIO pins.
        
        Args:
            red_pin (int): GPIO pin for red LED
            green_pin (int): GPIO pin for green LED
            yellow_pin (int): GPIO pin for yellow LED
        """
        self.red_gpio = Gpio(red_pin)
        self.green_gpio = Gpio(green_pin)
        self.yellow_gpio = Gpio(yellow_pin)
        
        # Set all pins as output
        self.red_gpio.dir(DIR_OUT)
        self.green_gpio.dir(DIR_OUT)
        self.yellow_gpio.dir(DIR_OUT)
        
        # Initialize all LEDs as off
        self._turn_off_all()
        self.current_state = None
    
    def _turn_off_all(self):
        """Turn off all LEDs."""
        self.red_gpio.write(0)
        self.green_gpio.write(0)
        self.yellow_gpio.write(0)
    
    def _set_color(self, color: str):
        """
        Set the lamp to a specific color.
        
        Args:
            color (str): Color to set (GREEN, YELLOW, RED)
        """
        self._turn_off_all()
        
        if color == self.GREEN:
            self.green_gpio.write(1)
        elif color == self.YELLOW:
            self.yellow_gpio.write(1)
        elif color == self.RED:
            self.red_gpio.write(1)
        
        self.current_state = color
        print(f"🔴🟡🟢 Lamp set to {color}")
    
    def update(self, noise: int, light: int, heartbeat: int):
        """
        Update lamp color based on sensor readings.
        
        Decision rules:
        - If noise > 70 OR light < 150 OR heartbeat > 100 → RED
        - Else if noise > 50 OR light < 300 OR heartbeat > 90 → YELLOW
        - Else → GREEN
        
        Args:
            noise (int): Noise level in dB
            light (int): Light intensity in lux
            heartbeat (int): Heart rate in bpm
        """
        # Check for RED conditions (poor focus environment)
        if noise > 70 or light < 150 or heartbeat > 100:
            self._set_color(self.RED)
        # Check for YELLOW conditions (moderate focus environment)
        elif noise > 50 or light < 300 or heartbeat > 90:
            self._set_color(self.YELLOW)
        # GREEN conditions (good focus environment)
        else:
            self._set_color(self.GREEN)
    
    def get_current_state(self) -> str:
        """
        Get the current lamp state.
        
        Returns:
            str: Current lamp color state
        """
        return self.current_state