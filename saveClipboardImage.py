import keyboard
import os
import time

def save_edit_screenshot():
  time.sleep(0.5)
  keyboard.press_and_release("prtscn")
  dir_path = os.path.dirname(os.path.realpath(__file__))
  os.startfile(dir_path + "\saveClipboardImage.bat")

print("Please press Alt+E to copy the path to the current screenshot saved to file.")

keyboard.add_hotkey('alt+E', lambda: save_edit_screenshot())
keyboard.wait()