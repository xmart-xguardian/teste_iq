from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QApplication
import sys

if sys.platform.startswith('win'):
    import ctypes
    def is_capslock_on():
        return bool(ctypes.WinDLL("User32.dll").GetKeyState(0x14))
else:
    def is_capslock_on():
        try:
            import keyboard
            return keyboard.is_toggled('caps lock')
        except ImportError:
            return False

class CapsLockWatcher(QObject):
    def __init__(self, label):
        super().__init__()
        self.label = label

    def eventFilter(self, obj, event):
        if event.type() in (QEvent.KeyPress, QEvent.KeyRelease, QEvent.FocusIn):
            if is_capslock_on():
                self.label.setText("⚠️ Caps Lock ATIVADO")
                self.label.setVisible(True)
            else:
                self.label.setVisible(False)
        return super().eventFilter(obj, event)