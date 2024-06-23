import pyautogui

window_title = "SRC"

window = pyautogui.getWindowsWithTitle(window_title)[0]
window_corner = window.topleft

click_point = (window_corner[0] + 530, window_corner[1] + 90)

pyautogui.moveTo(click_point)

pyautogui.click()
