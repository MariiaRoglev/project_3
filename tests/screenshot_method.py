import pyautogui

var_shot=pyautogui.screenshot()
var_shot.save('C:\screenshot.png')




def capture_screenshot(test_name):
    screenshot = pyautogui.screenshot()
    screenshot_path = os.path.join(os.getcwd(), f"{test_name}_failed.png")
    screenshot.save(screenshot.png)
    print(f"Screenshot saved at {screenshot_path}")