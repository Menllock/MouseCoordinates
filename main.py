import pyautogui
import time
from datetime import datetime

def track_mouse_position(interval=3):
    """
    Track mouse cursor position every 'interval' seconds and number each reading.
    
    Args:
        interval (int): Time in seconds between readings (default: 3)
    """
    counter = 1
    
    print("Mouse position tracker started. Press Ctrl+C to stop.\n")
    print("-" * 40)
    
    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()
            
            # Get current timestamp
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            # Print numbered position
            print(f"{counter}: [{timestamp}] x={x}; y={y}")
            
            # Increment counter
            counter += 1
            
            # Wait for specified interval
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\n" + "-" * 40)
        print(f"Tracking stopped. Total readings: {counter - 1}")

if __name__ == "__main__":
    # You can change the interval here if needed (in seconds)
    track_mouse_position(interval=3)
