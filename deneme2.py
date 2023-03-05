import sys
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLineEdit,QLabel

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.line_edit.textChanged.connect(self.line_edit_text_changed)

        self.show()

    def line_edit_text_changed(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
mw = MainWindow()
app.exec_()