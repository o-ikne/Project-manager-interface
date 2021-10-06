from PyQt5 import QtCore, QtGui, QtWidgets

class User(QtWidgets.QLabel):
    def __init__(self, parent=None, email=None, name=None, password=None, image=None):
        super().__init__(parent)
        self.parent   = parent
        self.name     = name
        self.password = password
        self.image    = image
        self.email    = email

        self.setFixedWidth(30)
        self.setFixedHeight(30)
        if image:
            self.image = QtGui.QImage(image)
            self.setPixmap(QtGui.QPixmap.fromImage(self.image)) 
            self.setScaledContents(True)       


    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.create_menu(QMouseEvent)

    def create_menu(self, event):
        menu  = QtWidgets.QMenu(self)
        #menu.setStyleSheet("background-color : lightgreen; border: 1px solid black;")
        name_action   = menu.addAction(self.name)
        projects_action = menu.addAction("my projects")
        change          = menu.addAction("change account")
        invite          = menu.addAction("Add a collaborator")
        parameters_action = menu.addAction("parameters")

        log_out = menu.addAction("log out")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == log_out:
            self.parent.show()
            self.parent.window.close()  

#========================================================================================

class Settings(QtWidgets.QWidget):
    def __init__(self):
        super(Settings, self).__init__() 


#=============================================================================================

class Restart_password(QtWidgets.QWidget):
    def __init__(self):
        super(Restart_password, self).__init__() 