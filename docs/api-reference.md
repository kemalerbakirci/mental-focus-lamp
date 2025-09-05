# 📚 API Reference - Mental Focus Desk Lamp

![API](https://img.shields.io/badge/API-Reference-blue?style=for-the-badge&logo=api)
![Documentation](https://img.shields.io/badge/Documentation-Complete-green?style=for-the-badge&logo=documentation)
![Python](https://img.shields.io/badge/Python-3.7+-yellow?style=for-the-badge&logo=python)
![Type Hints](https://img.shields.io/badge/Type%20Hints-Enabled-purple?style=for-the-badge&logo=typing)

## 📋 API Overview

This document provides comprehensive API reference for all classes and methods in the Mental Focus Desk Lamp project.

---

## 🔊 Sensors Module

### `sensors.noise_sensor`

#### **Class: `NoiseSensor`**
![Noise Sensor](https://img.shields.io/badge/Component-Noise%20Sensor-orange?style=flat-square)

Simulated noise sensor that returns random noise values in decibels.

**Constructor:**
```python
NoiseSensor()
```

**Methods:**

##### `read_value() -> int`
Read noise level in decibels.

**Returns:**
- `int`: Noise level between 30-90 dB

**Example:**
```python
from sensors.noise_sensor import NoiseSensor

sensor = NoiseSensor()
noise_level = sensor.read_value()
print(f"Current noise: {noise_level} dB")
```

---

### `sensors.light_sensor`

#### **Class: `LightSensor`**
![Light Sensor](https://img.shields.io/badge/Component-Light%20Sensor-yellow?style=flat-square)

Simulated light sensor that returns random light intensity values in lux.

**Constructor:**
```python
LightSensor()
```

**Methods:**

##### `read_value() -> int`
Read light intensity in lux.

**Returns:**
- `int`: Light intensity between 50-500 lux

**Example:**
```python
from sensors.light_sensor import LightSensor

sensor = LightSensor()
light_level = sensor.read_value()
print(f"Current light: {light_level} lux")
```

---

### `sensors.heartbeat_sensor`

#### **Class: `HeartbeatSensor`**
![Heartbeat Sensor](https://img.shields.io/badge/Component-Heartbeat%20Sensor-red?style=flat-square)

Simulated heartbeat sensor that returns random heart rate values in beats per minute.

**Constructor:**
```python
HeartbeatSensor()
```

**Methods:**

##### `read_value() -> int`
Read heart rate in beats per minute.

**Returns:**
- `int`: Heart rate between 60-120 bpm

**Example:**
```python
from sensors.heartbeat_sensor import HeartbeatSensor

sensor = HeartbeatSensor()
heart_rate = sensor.read_value()
print(f"Current heart rate: {heart_rate} bpm")
```

---

## 🎛️ Controllers Module

### `controllers.lamp_controller`

#### **Class: `LampController`**
![Lamp Controller](https://img.shields.io/badge/Component-Lamp%20Controller-blue?style=flat-square)

Controls an RGB LED lamp using GPIO pins based on sensor readings.

**Constructor:**
```python
LampController(red_pin: int = 11, green_pin: int = 12, yellow_pin: int = 13)
```

**Parameters:**
- `red_pin` (int, optional): GPIO pin for red LED. Default: 11
- `green_pin` (int, optional): GPIO pin for green LED. Default: 12  
- `yellow_pin` (int, optional): GPIO pin for yellow LED. Default: 13

**Class Attributes:**
- `GREEN = "GREEN"`: Green lamp state constant
- `YELLOW = "YELLOW"`: Yellow lamp state constant
- `RED = "RED"`: Red lamp state constant

**Methods:**

##### `update(noise: int, light: int, heartbeat: int) -> None`
Update lamp color based on sensor readings using decision rules.

**Parameters:**
- `noise` (int): Noise level in dB
- `light` (int): Light intensity in lux
- `heartbeat` (int): Heart rate in bpm

**Decision Rules:**
- **RED**: `noise > 70 OR light < 150 OR heartbeat > 100`
- **YELLOW**: `noise > 50 OR light < 300 OR heartbeat > 90` (and not RED)
- **GREEN**: All conditions within optimal ranges

**Example:**
```python
from controllers.lamp_controller import LampController

controller = LampController()
controller.update(noise=45, light=350, heartbeat=75)  # Should set GREEN
```

##### `get_current_state() -> str`
Get the current lamp color state.

**Returns:**
- `str`: Current lamp state ("GREEN", "YELLOW", or "RED")

**Example:**
```python
current_state = controller.get_current_state()
print(f"Lamp is currently: {current_state}")
```

---

## 🔧 Hardware Stubs Module

### `stubs.mraa_stub`

#### **Constants**
```python
DIR_OUT = 1  # GPIO output direction
DIR_IN = 0   # GPIO input direction
```

#### **Class: `Gpio`**
![GPIO Stub](https://img.shields.io/badge/Component-GPIO%20Stub-purple?style=flat-square)

Stub implementation of LibMRAA Gpio class for hardware simulation.

**Constructor:**
```python
Gpio(pin: int)
```

**Parameters:**
- `pin` (int): GPIO pin number

**Attributes:**
- `pin` (int): GPIO pin number
- `direction` (int): Current GPIO direction (DIR_OUT or DIR_IN)

**Methods:**

##### `dir(mode: int) -> None`
Set GPIO direction.

**Parameters:**
- `mode` (int): `DIR_OUT` (1) for output or `DIR_IN` (0) for input

**Example:**
```python
from stubs.mraa_stub import Gpio, DIR_OUT

gpio = Gpio(13)
gpio.dir(DIR_OUT)
```

##### `write(value: int) -> None`
Write value to GPIO pin.

**Parameters:**
- `value` (int): 0 for LOW, 1 for HIGH

**Side Effects:**
- Prints GPIO state to console

**Example:**
```python
gpio.write(1)  # Turn LED on
gpio.write(0)  # Turn LED off
```

---

### `stubs.upm_stub`

#### **Class: `Sensor`**
![UMP Stub](https://img.shields.io/badge/Component-UMP%20Stub-green?style=flat-square)

Base class for UPM sensor stubs providing standardized interface.

**Constructor:**
```python
Sensor()
```

**Methods:**

##### `read_value()`
Abstract method for reading sensor values. Must be implemented by child classes.

**Raises:**
- `NotImplementedError`: If called on base class

**Usage:**
```python
from stubs.upm_stub import Sensor

class CustomSensor(Sensor):
    def read_value(self):
        return 42

sensor = CustomSensor()
value = sensor.read_value()  # Returns 42
```

---

## 🚀 Main Application

### `main`

#### **Function: `main()`**
![Main Application](https://img.shields.io/badge/Component-Main%20App-teal?style=flat-square)

Main application entry point that orchestrates the entire system.

**Functionality:**
1. Initializes all sensors and controllers
2. Runs continuous monitoring loop
3. Displays sensor readings and lamp states
4. Handles graceful shutdown on Ctrl+C

**Example Output:**
```
🔬 Mental Focus Desk Lamp - Starting Simulation
==================================================
✅ All sensors and controllers initialized
📊 Starting sensor monitoring loop...

--- Cycle 1 ---
🔊 Noise: 45 dB
💡 Light: 320 lux
❤️  Heart Rate: 78 bpm
🚦 Lamp State: 🟢 GREEN
```

**Usage:**
```bash
python main.py
```

---

## 📊 Data Types Reference

### **Sensor Reading Types**
```python
# Type aliases for clarity
NoiseLevel = int      # Range: 30-90 dB
LightLevel = int      # Range: 50-500 lux  
HeartRate = int       # Range: 60-120 bpm
```

### **Lamp State Types**
```python
# Lamp state enumeration
LampState = Literal["GREEN", "YELLOW", "RED"]
```

### **GPIO Types**
```python
# GPIO related types
GpioPin = int         # GPIO pin number
GpioValue = int       # 0 (LOW) or 1 (HIGH)
GpioDirection = int   # DIR_OUT (1) or DIR_IN (0)
```

---

## ⚠️ Error Handling

### **Common Exceptions**

#### `NotImplementedError`
Raised when calling abstract methods on base classes.

```python
from stubs.upm_stub import Sensor

sensor = Sensor()
try:
    sensor.read_value()
except NotImplementedError:
    print("Must implement read_value() in child class")
```

#### `KeyboardInterrupt`
Handled gracefully in main application for clean shutdown.

```python
# In main.py
try:
    while True:
        # Main loop
        pass
except KeyboardInterrupt:
    print("\n🛑 Simulation stopped by user")
```

---

## 🔍 Usage Examples

### **Complete System Usage**
```python
#!/usr/bin/env python3
from sensors.noise_sensor import NoiseSensor
from sensors.light_sensor import LightSensor
from sensors.heartbeat_sensor import HeartbeatSensor
from controllers.lamp_controller import LampController
import time

# Initialize components
noise_sensor = NoiseSensor()
light_sensor = LightSensor()
heartbeat_sensor = HeartbeatSensor()
lamp_controller = LampController()

# Single reading cycle
noise = noise_sensor.read_value()
light = light_sensor.read_value()
heartbeat = heartbeat_sensor.read_value()

print(f"Sensors: {noise}dB, {light}lux, {heartbeat}bpm")

# Update lamp based on readings
lamp_controller.update(noise, light, heartbeat)
state = lamp_controller.get_current_state()
print(f"Lamp State: {state}")
```

### **Custom GPIO Configuration**
```python
from controllers.lamp_controller import LampController

# Custom GPIO pin assignment
custom_controller = LampController(
    red_pin=21,
    green_pin=22, 
    yellow_pin=23
)
```

### **Testing Individual Components**
```python
from sensors.noise_sensor import NoiseSensor

# Test sensor range
sensor = NoiseSensor()
readings = [sensor.read_value() for _ in range(10)]
print(f"Min: {min(readings)}, Max: {max(readings)}")
assert all(30 <= r <= 90 for r in readings), "Values out of range"
```

---

## 🔧 Extension Points

### **Adding New Sensors**
```python
from stubs.upm_stub import Sensor
import random

class TemperatureSensor(Sensor):
    """Temperature sensor returning values in Celsius."""
    
    def read_value(self) -> int:
        return random.randint(18, 30)  # 18-30°C
```

### **Custom Decision Logic**
```python
from controllers.lamp_controller import LampController

class CustomLampController(LampController):
    def update(self, noise: int, light: int, heartbeat: int):
        # Custom decision algorithm
        stress_score = (noise / 90) + (1 - light / 500) + (heartbeat / 120)
        
        if stress_score > 2.0:
            self._set_color(self.RED)
        elif stress_score > 1.0:
            self._set_color(self.YELLOW)
        else:
            self._set_color(self.GREEN)
```

---

**Complete API Coverage! 📚✨**
