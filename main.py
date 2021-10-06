
from PyQt5 import QtWidgets
from account import Log_in





if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Log_in()
    window.show()
    sys.exit(app.exec())
