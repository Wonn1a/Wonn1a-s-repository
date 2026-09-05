import pyautogui
import time
import threading
import keyboard


class Clicker:
    def __init__(self, interval=0.01, button='left'):
        self.interval = interval  # 点击间隔（秒）
        self.button = button  # 'left' 或 'right'
        self.running = False
        self.thread = None

    def click_loop(self):
        """循环点击"""
        print(f"连点已启动，间隔 {self.interval} 秒，按 F2 停止")
        while self.running:
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

    def start(self):
        """启动连点"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.click_loop, daemon=True)
            self.thread.start()

    def stop(self):
        """停止连点"""
        self.running = False
        print("连点已停止")


if __name__ == "__main__":
    clicker = Clicker(interval=0.05, button='left')  # 每秒20次

    print("按 F1 启动连点，按 F2 停止连点")
    keyboard.add_hotkey('f1', clicker.start)
    keyboard.add_hotkey('f2', clicker.stop)

    keyboard.wait('esc')  # 按 ESC 退出程序
    clicker.stop()
