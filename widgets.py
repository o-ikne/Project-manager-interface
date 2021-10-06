
from PyQt5 import QtWidgets, QtGui, QtCore

class Button(QtWidgets.QPushButton):

    def __init__(self, parent=None, image=None, text=None, function=None, shortcut=""):
        super().__init__()
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(20, 20))
        self.clicked.connect(function)
        self.setShortcut(shortcut)
        self.setText(text)

class Radio_Button(QtWidgets.QRadioButton):

    def __init__(self,image=None, parent=None, function=None, text=None):
        super().__init__(parent)
        self.setText(text)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.toggled.connect(function)
 

class Label(QtWidgets.QLabel):

    def __init__(self,parent=None, image=None, text=None, color=None, function=None, hand=False, rename=False):
        super().__init__(parent)
        if image:
            self.image = QtGui.QImage(image)#.scaled(20, 20)
            self.setPixmap(QtGui.QPixmap.fromImage(self.image))
        if hand:
            self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setText(text)
        self.setStyleSheet(color)
        self.mouseReleaseEvent = function
        #self.setFixedHeight(30)
        #self.setFixedWidth(30)
        self.setScaledContents(True)
        #self.setStyleSheet("background-color: rgba(255, 255, 0); border: 1px solid black;")
        self.is_renamable = rename

    def mouseDoubleClickEvent(self, event):
        if self.is_renamable:
            text, ok = QtWidgets.QInputDialog.getText(self, 'Setting Text', 'new text :')
            if ok:
                self.setText("   " + text) 

    def rename(self, event):
        self.mouseDoubleClickEvent(event)