cd /d "%~dp0"
pyinstaller --onefile saveClipboardImage.py
copy /Y .\dist\saveClipboardImage.exe .\
start cmd /k saveClipboardImage.exe
pause
exit