import keyboard
import os

print("Please press Ctrl+Shift+1 to copy the path to the current screenshot saved to file.")

dir_path = os.path.dirname(os.path.realpath(__file__))

keyboard.add_hotkey('ctrl+shift+1', lambda: os.startfile(dir_path + "\saveClipboardImage.bat"))
keyboard.wait()