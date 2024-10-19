import pyautogui
from PIL import Image
import time

def is_green(pixel):
    # Define what constitutes a "green" pixel
    r, g, b = pixel
    return g > 200 and r < 100 and b < 100

def find_and_click_green_pixel(x_start, y_start, x_end, y_end):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
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
                # Print message when green pixel is found
                print(f"Found green at ({x}, {y})")
                # Move the mouse to the pixel and click
                pyautogui.click(x, y)
                return

if __name__ == "__main__":
    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()
    
    # Define the custom range as a percentage of the screen dimensions
    x_start_pct, y_start_pct = 0.2, 0.2  # 40% from the left and top
    x_end_pct, y_end_pct = 0.5, 0.5    # 70% from the left and top
    
    # Convert percentage-based coordinates to absolute coordinates
    x_start = int(screen_width * x_start_pct)
    y_start = int(screen_height * y_start_pct)
    x_end = int(screen_width * x_end_pct)
    y_end = int(screen_height * y_end_pct)
    
    while True:
        find_and_click_green_pixel(x_start, y_start, x_end, y_end)
        # Add a small delay to avoid excessive CPU usage
        time.sleep(1)