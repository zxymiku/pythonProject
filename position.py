import pygetwindow as gw
import pyautogui

window_title = "SRC"

all_windows = gw.getAllTitles()

target_window = None
for title in all_windows:
    if window_title in title:
        target_window = gw.getWindowsWithTitle(title)[0]
        break

if target_window:
    window_corner = target_window.left, target_window.top
    print(f"Window '{window_title}' corner: {window_corner}")
    screen_click_point = target_window.left + target_window.width / 2, target_window.top + target_window.height / 2

    # 模拟鼠标移动到指定坐标并点击
    pyautogui.moveTo(screen_click_point)
    pyautogui.click()
    mouse_position = pyautogui.position()
    # 计算相对于窗口左上角的坐标
    relative_click_point = mouse_position[0] - window_corner[0], mouse_position[1] - window_corner[1]

    # 输出鼠标点击位置相对于窗口左上角的坐标
    print(f"Mouse click position relative to window corner: {relative_click_point}")
else:
    print(f"No window found with title '{window_title}'.")
