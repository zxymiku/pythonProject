import pyautogui
import time
import pygetwindow as gw
import win32gui

window_title = "SRC"

while True:
    try:
        # 尝试找到窗口
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            window = windows[0]
            # 将窗口带到最前端
            window.activate()
            win32gui.SetForegroundWindow(window._hWnd)

            # 等待窗口激活
            time.sleep(1)

            # 计算点击位置
            window_corner = window.topleft
            click_point = (window_corner[0] + 530, window_corner[1] + 90)
            time.sleep(15)  # 点击后等待10秒
            pyautogui.moveTo(click_point)
            pyautogui.click()
            break  # 如果点击成功，退出循环
        else:
            # 如果没有找到窗口，等待一段时间后重试
            time.sleep(1)
    except Exception as e:
        print(f"发生错误：{e}")
        break  # 如果发生错误，退出循环
