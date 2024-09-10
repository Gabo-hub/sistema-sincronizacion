import sys
from PySide6 import QtWidgets
from controllers.main_windows import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
