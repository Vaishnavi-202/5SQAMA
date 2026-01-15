import os
import datetime
from PIL import ImageGrab


def capture_screenshot(step_name: str):
    """
    Capture screenshot at a meaningful moment during execution.
    """
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_step = step_name.replace(" ", "_").replace("/", "_")

    file_name = f"{safe_step}_{timestamp}.png"
    file_path = os.path.join(screenshots_dir, file_name)

    try:
        img = ImageGrab.grab(all_screens=True)
        img.save(file_path)
    except Exception as e:
        print(f"[Screenshot Error at {step_name}] {e}")
