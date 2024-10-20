import pyautogui
import time
from pynput import keyboard
from PIL import ImageGrab
import pygetwindow as gw

# Global variable to control the loop


running = True
stop_key = "s"
range_x = 0.35, 0.5 # Custom range for green pixel search x axis
range_y = 0.4, 0.5 # Custom range for green pixel search y axis

def on_press(key, stop_key):
    global running
    try:
        if key.char == stop_key:
            running = False
            print("\nShutting down...")
            return False  # Stop the listener
    except AttributeError:
        pass

def is_green(pixel):
    # Define what constitutes a green pixel
    r, g, b = pixel
    return g > 200 and r < 100 and b < 100

def find_and_click_green_pixel(x_start, y_start, x_end, y_end):
    # Take a screenshot using Pillow
    screenshot = ImageGrab.grab()
    width, height = screenshot.size

    # Ensure the custom range is within the screenshot dimensions
    x_start = max(0, x_start)
    y_start = max(0, y_start)
    x_end = min(width, x_end)
    y_end = min(height, y_end)

    # Loop through each pixel in the specified range
    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            pixel = screenshot.getpixel((x, y))
            if is_green(pixel):
                # Calculate the percentage position
                x_percent = (x / width) * 100
                y_percent = (y / height) * 100
                # Print message when green pixel is found
                print(f"Found green at ({x}, {y}) - {x_percent:.2f}% x, {y_percent:.2f}% y")
                # Move the mouse to the pixel and click
                pyautogui.click(x, y)
                return

if __name__ == "__main__":
    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()
    
       # Convert percentage-based coordinates to absolute coordinates
    x_start = int(screen_width * range_x[0])
    y_start = int(screen_height * range_y[0])
    x_end = int(screen_width * range_x[1])
    y_end = int(screen_height * range_y[1])
    
    # Start the keyboard listener in a separate thread
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    while running:
        # Check if Counter-Strike 2 is the active window
        active_window = gw.getActiveWindow()
        if active_window and "Counter-Strike 2" in active_window.title:
            find_and_click_green_pixel(x_start, y_start, x_end, y_end)
        # Add a small delay to avoid excessive CPU usage
        time.sleep(1)
    
    listener.join()
