#!/usr/bin/env python3
"""
Mental Focus Desk Lamp - Main Entry Point

This is the main simulation for a smart desk lamp that adapts to focus conditions
using simulated sensors (noise, light, heartbeat) and an RGB LED controller.
"""

import time
from sensors.noise_sensor import NoiseSensor
from sensors.light_sensor import LightSensor
from sensors.heartbeat_sensor import HeartbeatSensor
from controllers.lamp_controller import LampController


def main():
    """Main function to run the Mental Focus Desk Lamp simulation."""
    print("🔬 Mental Focus Desk Lamp - Starting Simulation")
    print("=" * 50)
    
    # Initialize sensors
    noise_sensor = NoiseSensor()
    light_sensor = LightSensor()
    heartbeat_sensor = HeartbeatSensor()
    
    # Initialize lamp controller
    lamp_controller = LampController()
    
    print("✅ All sensors and controllers initialized")
    print("📊 Starting sensor monitoring loop...")
    print("Press Ctrl+C to stop\n")
    
    try:
        cycle = 1
        while True:
            print(f"--- Cycle {cycle} ---")
            
            # Read sensor values
            noise = noise_sensor.read_value()
            light = light_sensor.read_value()
            heartbeat = heartbeat_sensor.read_value()
            
            # Display sensor readings
            print(f"🔊 Noise: {noise} dB")
            print(f"💡 Light: {light} lux")
            print(f"❤️  Heart Rate: {heartbeat} bpm")
            
            # Update lamp based on sensor readings
            lamp_controller.update(noise, light, heartbeat)
            
            # Display current lamp state
            current_state = lamp_controller.get_current_state()
            state_emoji = {"GREEN": "🟢", "YELLOW": "🟡", "RED": "🔴"}
            print(f"🚦 Lamp State: {state_emoji.get(current_state, '⚪')} {current_state}")
            
            print()  # Empty line for readability
            
            # Wait before next cycle
            time.sleep(1)
            cycle += 1
            
    except KeyboardInterrupt:
        print("\n🛑 Simulation stopped by user")
        print("👋 Mental Focus Desk Lamp - Goodbye!")


if __name__ == "__main__":
    main()