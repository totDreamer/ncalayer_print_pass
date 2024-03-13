import pygetwindow as gw
import pyautogui
import time


def find_window(window_title):
    windows_list = gw.getAllTitles()
    for window in windows_list:
        if window_title in window:
            return gw.getWindowsWithTitle(window)[0]
    return None


def enter_password(window, password):
    if window is None:
        print("Окно не найдено")
        return

    else:
        window.activate()

        pyautogui.write(password)
        pyautogui.press('enter')
        time.sleep(5)  # Добавим задержку, чтобы дать приложению время для загрузки


def select_line():
    # Сделать пять нажатий клавиши "tab"
    for _ in range(5):
        pyautogui.press('tab')


# Задаем заголовок окна, которое нужно найти
window_title = "NCALayer"
# Задаем заранее подготовленный пароль
password = ("qwerty1234567890")

# Бесконечный цикл для того, чтобы программа не закрывалась сама
while True:
# Ищем окно
    window = find_window(window_title)
# Выполняем проверку найдено ли окно, если да, то переходим на нужную строку и вводим пароль
    if window is not None:
        select_line()
        enter_password(window, password)
# Вводим пароль



