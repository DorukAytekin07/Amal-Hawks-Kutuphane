from PySide6.QtWidgets import QApplication
import sys
from Kütüphane_Raflar import Widget
app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()