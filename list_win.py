import pygetwindow as gw

def list_windows():
    windows_list = gw.getAllTitles()
    for i, window in enumerate(windows_list):
        print(f"{i}: {window}")

def find_window(window_title):
    windows_list = gw.getAllTitles()
    for window in windows_list:
        if window_title in window:
            return gw.getWindowsWithTitle(window)[0]
    return None

# Вывести список доступных окон и их заголовков
list_windows()
