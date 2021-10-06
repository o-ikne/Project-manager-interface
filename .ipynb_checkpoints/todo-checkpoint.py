
from PyQt5 import QtCore, QtGui, QtWidgets

NEW      = "new_icon10.png"
COLOR    = "color10.png"
EDIT     = "edit10.png"
REMOVE   = "remove10.png"
PHOTO    = "photo10.png"
MORE     = "more10.png"
CALENDER = "calender10.png"
TIME     = "time.png"
USER     = "user.png"
EYE      = "eye.png"
ACCEPT   = "accept.png"
REJECT   = "reject.png"
LOW      = "low_priority1.png"
MEDIUM   = "medium_priority1.png"
HIGH     = "high_priority1.png"
VERYHIGH = "veryhigh_priority1.png"
NOTES    = "notes1.png"
LTIME    = "lefttime.png"
FROMTO   = "fromto.png"
TASK     = "task.png"
UP       = "move_up.png"
DOWN     = "move_down.png"
SHOW     = "show_projects.png"
TABLE    = "table.png"
NOTYET   = "not_yet.png"
PROGRESS = "in_progress.png"


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

#===================================================================================================

class User(QtWidgets.QLabel):
    def __init__(self, parent=None, email=None, name=None, password=None, image=USER):
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
        menu.setStyleSheet("background-color : lightgreen; border: 1px solid black;")
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


#=================================================================================================

class Task(QtWidgets.QLabel):
    def __init__(self, parent=None, image=None, text=""):
        super().__init__(parent)
        self.text       = text
        self.parent     = parent
        self.entred_text = text
        self.priority = LOW
        self.editing = False
        self.images  = []
        self.image_labels = []
        self.setStyleSheet(" border: 1px solid lightgray;")
        self.setText(" Task " + str(len(parent._tasks)))
        self.create_priority_box()
        self.create_done_box()
        self.create_labels()
        self.set_priority()
        self.setFixedHeight(30)
        self.data = [self.text, self.parent.parent.user.name, self.priority, "in progress"]
        self.parent.insert_data(self.data)

    def set_color(self):
        image = QtGui.QImage(self.priority)   
        self.task_label.setPixmap(QtGui.QPixmap.fromImage(image))

    def create_labels(self): 
        self.gbox  = QtWidgets.QGroupBox()
        self._hbox = QtWidgets.QHBoxLayout()
        self._vbox = QtWidgets.QVBoxLayout()
        self.vbox = QtWidgets.QVBoxLayout()
        self.space2     = Label()
        self.space2.setFixedWidth(30) 
        self.dialog = QtWidgets.QLineEdit()
        self.dialog.insert(self.text)
        self.dialog.textChanged.connect(self.get_dialog_text)
        self.dialog.hide()

        self.button_acc_text = Label(image=ACCEPT, function=self.accept_text, hand=True)
        self.button_rej_text = Label(image=REJECT, function=self.reject_text, hand=True)

        self.button_acc_text.hide()
        self.button_rej_text.hide()

        self.button_acc_text.setFixedHeight(20)
        self.button_acc_text.setFixedWidth(20)
        self.button_rej_text.setFixedWidth(20)
        self.button_rej_text.setFixedHeight(20)

        self.option_box = QtWidgets.QHBoxLayout()  
        self.edit = Label(image=EDIT,   function=self.set_text, hand=True)
        self.edit.setFixedHeight(20)
        self.edit.setFixedWidth(20)
        self.delete = Label(image=REMOVE, function=self.remove, hand=True)
        self.delete.setFixedHeight(20)
        self.delete.setFixedWidth(20)
        self.see_more = Label(image=MORE, function=self.see_more, hand=True)
        self.see_more.setFixedHeight(20)
        self.see_more.setFixedWidth(20) 
        self.notes_hbox = QtWidgets.QHBoxLayout() 
        self.notes_hbox.setAlignment(QtCore.Qt.AlignLeft) 
        self.notes = Label(text="Notes")
        self.notes.setStyleSheet("""QLabel {color: gray }""")
        self.edit_notes = Label(image=EDIT, function=self.set, hand=True)
        self.edit_notes.setFixedHeight(20)
        self.edit_notes.setFixedWidth(20) 
        self.add_photo = Label(image=PHOTO, function=self.new_photo, hand=True)
        self.add_photo.setFixedHeight(20)
        self.add_photo.setFixedWidth(20) 

        self.notes_hbox.addWidget(self.notes)
        self.notes_hbox.addWidget(self.edit_notes)
        self.notes_hbox.addWidget(self.add_photo)
        self.discription = QtWidgets.QTextEdit()  
        self.discription.setPlaceholderText("write your notes here ...!")  
        self.discription.setReadOnly(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok| QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.hide()

        self.option_box.addWidget(self.task_label)
        self.option_box.addWidget(self)

        self.option_box.addWidget(self.dialog)
        self.option_box.addWidget(self.button_acc_text)
        self.option_box.addWidget(self.button_rej_text)

        self.option_box.addWidget(self.see_more)
        self.option_box.addWidget(self.edit)
        self.option_box.addWidget(self.delete)

        self.vbox.addWidget(self.priority_gbox)
        self.vbox.addWidget(self.done_gbox)
        self.vbox.addLayout(self.notes_hbox)
        self.vbox.addWidget(self.discription)
        self.vbox.addWidget(self.buttonBox)

        self.gbox.setLayout(self.vbox)

        self._hbox.addWidget(self.space2)
        self._hbox.addWidget(self.gbox)

        self._vbox.addLayout(self.option_box)
        self._vbox.addLayout(self._hbox)       

    def create_priority_box(self):
        self.priority_gbox = QtWidgets.QGroupBox()
        self.done_gbox     = QtWidgets.QGroupBox()
        self.priority_box  = QtWidgets.QHBoxLayout()

        self.task_label = Label(function=self.hide_priorities, hand=True)
        self.task_label.setFixedWidth(30)
        self.task_label.setFixedHeight(30)

        self.priority_label = Label(text="Priority : ")
        self.low_level      = Radio_Button(image=LOW,      text="Low",       function=self.set_priority)
        self.medium_level   = Radio_Button(image=MEDIUM,   text="Medium",    function=self.set_priority)
        self.high_level     = Radio_Button(image=HIGH,     text="High",      function=self.set_priority)
        self.veryhigh_level = Radio_Button(image=VERYHIGH, text="Very High", function=self.set_priority)

        self.priority_label.setStyleSheet("""QLabel {color: gray }""")
        self.low_level.setChecked(True)

        self.priority_box.addWidget(self.priority_label)
        self.priority_box.addWidget(self.low_level)
        self.priority_box.addWidget(self.medium_level)
        self.priority_box.addWidget(self.high_level)
        self.priority_box.addWidget(self.veryhigh_level)
        self.priority_gbox.setLayout(self.priority_box)
        self.priority_gbox.setHidden(True)

    def create_done_box(self):
        self.done_box  = QtWidgets.QHBoxLayout()

        self.done_label  = Label(text="Done : ")
        self.no          = Radio_Button(image=REJECT,   text="No",          function=self.set_done)
        self.not_yet     = Radio_Button(image=NOTYET,   text="Not yet",     function=self.set_done)
        self.in_progress = Radio_Button(image=PROGRESS, text="In progress", function=self.set_done)
        self.yes         = Radio_Button(image=ACCEPT,   text="Yes",         function=self.set_done)

        self.done_label.setStyleSheet("""QLabel {color: gray }""")
        self.not_yet.setChecked(True)

        self.done_box.addWidget(self.done_label)
        self.done_box.addWidget(self.yes)
        self.done_box.addWidget(self.in_progress)
        self.done_box.addWidget(self.not_yet)
        self.done_box.addWidget(self.no)
        self.done_gbox.setLayout(self.done_box)
        self.done_gbox.setHidden(True)

    def set_done(self, event):
        self._no          = self.no.isChecked()
        self._not_yet     =  self.not_yet.isChecked()
        self._in_progress = self.in_progress.isChecked()
        self._yes         = self.yes.isChecked()
        self.set_done_color()
        self.done_gbox.setHidden(True)
        self.priority_gbox.setHidden(True)

    def set_done_color(self):
        if self._no:
            self.setStyleSheet("border: 1px solid red;")
        elif self._yes:
            self.setStyleSheet("border: 1px solid green;")
        elif self._in_progress:
            self.setStyleSheet("border: 1px solid yellow;")
        else:
            self.setStyleSheet("border: 1px solid lightgray;")

    def hide_priorities(self, event):
        self.priority_gbox.setHidden(not self.priority_gbox.isHidden())
        self.done_gbox.setHidden(not self.done_gbox.isHidden())

    def see_more(self, event):
        self.rotate_image(self.see_more)
        self.gbox.setHidden(not self.gbox.isHidden())

    def set_priority(self):
        if self.low_level.isChecked():
            self.priority = LOW
        elif self.medium_level.isChecked():
            self.priority = MEDIUM
        elif self.high_level.isChecked():
            self.priority = HIGH
        else:
            self.priority = VERYHIGH
        self.set_color()
        self.priority_gbox.setHidden(True)
        self.done_gbox.setHidden(True)

    def accept(self):
        self.discription.setReadOnly(True)
        self.buttonBox.hide()

    def accept_text(self, event):
        self.text = self.entred_text
        self.button_acc_text.hide()
        self.button_rej_text.hide()
        self.dialog.hide()
        self.setText(self.text) 
        self.see_more.show()
        self.edit.show()
        self.delete.show()
        self.show()
        self.editing = False

    def reject_text(self, event):
        self.button_acc_text.hide()
        self.button_rej_text.hide()
        self.dialog.hide()
        self.see_more.show()
        self.edit.show()
        self.delete.show()
        self.show()

    def get_dialog_text(self, text):
        self.entred_text = text

    def set_text(self, event):
        self.editing = True
        self.dialog.setVisible(not self.dialog.isVisible())
        self.button_acc_text.show()
        self.button_rej_text.show()
        self.see_more.hide()
        self.edit.hide()
        self.delete.hide()
        self.hide()

    def reject(self):
        self.discription.setReadOnly(True)
        self.buttonBox.hide()


    def remove(self, event):
        self.parent._tasks.remove(self)
        self.deleteLater() 
        self.see_more.deleteLater()  
        self.edit.deleteLater()
        self.delete.deleteLater()
        self.task_label.deleteLater()
        self.space2.deleteLater()
        self.gbox.deleteLater()

    def new_photo(self, event):
        image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '', " (*.png *.jpg)")
        image  = Label(image=image_path)
        image.setFixedWidth(300)
        image.setFixedHeight(180)
        image_label = Label(text="image " + str(len(self.image_labels) + 1), rename=True)
        layout = self.vbox.layout()
        layout.insertWidget(layout.count()+1, image_label)
        layout.insertWidget(layout.count()+1, image)
        self.images.append(image)
        self.image_labels.append(image_label)

    def set(self, event):
        if self.discription.isVisible():
            self.buttonBox.setVisible(self.discription.isReadOnly())
            self.discription.setReadOnly(not self.discription.isReadOnly())

    def mouseDoubleClickEvent(self, event):
        self.set_text(event)

    def keyPressEvent(self, event):
        if event.key()  == QtCore.Qt.Key_Return:
            self.accept_text(event)

    def rotate_image(self, label):
        transform = QtGui.QTransform().rotate(180)
        image_ = label.image.transformed(transform, QtCore.Qt.SmoothTransformation)
        label.image = image_
        label.setPixmap(QtGui.QPixmap.fromImage(image_))

#==========================================================================================


class Project(QtWidgets.QLabel):

    def __init__(self, parent=None, image=None, color=None, text="", range_=None):
        super().__init__(parent)
        self.start_time = QtCore.QDate.currentDate()
        self.color      = "lightgreen"
        self.text       = text
        self.parent     = parent
        self.details    = self.get_info()
        self._tasks     = []
        self.end_time   = 5
        self.editing    = False
        self.entred_text = text
        self.range       = range_

        self.table = Create_table()
        self.table.resize(self.width(), self.height())
        
        self.setFixedHeight(50)
        self.setFont(QtGui.QFont('Arial', 10.5))
        self.setStyleSheet(" border: 1px solid lightgray;")
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.setScaledContents(True)
        self.setText("   " + text)
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.create_options_label()
        self.create_task0()

    def create_options_label(self):
        self.vbox = QtWidgets.QHBoxLayout()

        self.dialog = QtWidgets.QLineEdit()
        self.dialog.insert(self.text)
        self.dialog.textChanged.connect(self.get_dialog_text)

        self.button_acc_text = Label(image=ACCEPT, function=self.accept_text, hand=True)
        self.button_rej_text = Label(image=REJECT, function=self.reject_text, hand=True)

        self.button_acc_text.hide()
        self.button_rej_text.hide()

        self.button_acc_text.setFixedHeight(20)
        self.button_acc_text.setFixedWidth(20)
        self.button_rej_text.setFixedWidth(20)
        self.button_rej_text.setFixedHeight(20)


        self.delete_label = Label(image=REMOVE, function=self.remove)
        self.color_label  = Label(image=COLOR,  function=self.set_color)
        self.text_label   = Label(image=EDIT,   function=self.set_text)
        self.delete_label.setFixedWidth(25)
        self.delete_label.setFixedHeight(25)
        self.text_label.setFixedWidth(25)
        self.text_label.setFixedHeight(25)
        self.color_label.setFixedWidth(25)
        self.color_label.setFixedHeight(25)

        self.delete_label.hide()
        self.color_label.hide()
        self.text_label.hide()

        self.vbox.addWidget(self.dialog)
        self.vbox.addWidget(self.button_acc_text)
        self.vbox.addWidget(self.button_rej_text)
        self.vbox.addWidget(self.text_label) 
        self.vbox.addWidget(self.color_label)
        self.vbox.addWidget(self.delete_label)
        self.vbox.setAlignment(QtCore.Qt.AlignRight)
        self.hbox.addLayout(self.vbox) 

        self.dialog.hide()

    def accept_text(self, event):
        self.text = self.entred_text
        self.button_acc_text.hide()
        self.button_rej_text.hide()
        self.dialog.hide()
        self.setText("   " + self.text) 
        self.name_label.setText(self.text)
        self.delete_label.show()
        self.color_label.show()
        self.text_label.show()
        self.editing = False

    def reject_text(self, event):
        self.button_acc_text.hide()
        self.button_rej_text.hide()
        self.dialog.hide()
        self.delete_label.show()
        self.color_label.show()
        self.text_label.show()

    def keyPressEvent(self, event):
        if event.key()  == QtCore.Qt.Key_Return:
            self.accept_text(event)

    def insert_data(self, data):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        for element in range(len(data)):
            self.table.setItem(rowPosition , element, QtWidgets.QTableWidgetItem(str(data[element])))

    def remove(self, event):
        self.parent.projects_box.removeWidget(self)
        self.parent._projects.remove(self)
        self.parent.project_box.removeWidget(self.info)
        self.info.deleteLater()
        self.deleteLater()

    def set_color(self, event):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet("background-color:" + color.name() + ";") 
            self.color = color.name()

    def set_text(self, event):
        self.editing = True
        self.dialog.setVisible(not self.dialog.isVisible())
        self.button_acc_text.show()
        self.button_rej_text.show()
        self.delete_label.hide()
        self.color_label.hide()
        self.text_label.hide()

    def show_table(self):
        self.table.show()

    def get_dialog_text(self, text):
        self.entred_text = text

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.RightButton:
            self.create_menu(QMouseEvent)
        if QMouseEvent.button() == QtCore.Qt.LeftButton and not self.editing:
            self.delete_label.show()
            self.color_label.show()
            self.text_label.show()
            self.setStyleSheet("background-color :" + self.color + ";")
            self.parent.project_box.setCurrentWidget(self.info)
            self.parent.current_project = self
            for project in self.parent._projects :
                if project != self:
                    #project.setStyleSheet("QLabel::hover""{""background-color :" + project.color + ";""};")
                    project.setStyleSheet(" border: 1px solid lightgray;")
                    project.delete_label.hide()
                    project.color_label.hide()
                    project.text_label.hide()


    def mouseDoubleClickEvent(self, event):
        #self.set_text(event)
        self.table.resize(640, 480)

        self.show_table()

    def create_task0(self):
        layout = self.tasks_box.layout()
        task = Task(parent=self)
        layout.insertLayout(layout.count() + 1, task._vbox)
        self._tasks += [task] 

    def get_info(self):
            self.info  = QtWidgets.QWidget()
            self.tasks = QtWidgets.QWidget()
            self.task_scroll = QtWidgets.QScrollArea()
            self.task_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.task_scroll.setWidgetResizable(True)
            new_task = Label(image=NEW, function=self.new_task, hand=True)
            new_task.setAlignment(QtCore.Qt.AlignLeft)
            #new_task.setStyleSheet("QLabel::hover""{""background-color : lightblue;""}")
            new_task.setFixedHeight(20)
            new_task.setFixedWidth(20)
            edit_disp = Label(image=EDIT,   function=self.set_disp, hand=True)      
            #edit_disp.setStyleSheet(  "QLabel::hover""{""background-color : yellow;""};")
            edit_disp.setFixedWidth(20)
            edit_disp.setFixedHeight(20)
            edit_disp.setAlignment(QtCore.Qt.AlignLeft)
            self.vbox_info = QtWidgets.QVBoxLayout()
            self.disp_box  = QtWidgets.QHBoxLayout()
            self.tasks_box = QtWidgets.QVBoxLayout()
            self.name_label = Label(text=self.text)
            self.name_label.setFixedHeight(20)
            self.name_label.setFont(QtGui.QFont('Arial', 15, QtGui.QFont.Bold))
            calendar_label = Label(image=CALENDER, function=self.set_end_date, hand=True)
            calendar_label.setFixedWidth(20)
            calendar_label.setFixedHeight(20)    
            calendar_label.setStyleSheet("QLabel::hover""{""background-color : yellow;""};")        
            bgrd_color = Label(image=COLOR, function=self.set_bgrd_color, hand=True)
            #bgrd_color.setStyleSheet("QLabel::hover""{""background-color : yellow;""};")
            bgrd_color.setFixedWidth(20)
            bgrd_color.setFixedHeight(20)
            bgrd_image = Label(image=PHOTO, function=self.set_bgrd_image, hand=True)
            #bgrd_image.setStyleSheet("QLabel::hover""{""background-color : yellow;""};")
            bgrd_image.setFixedWidth(20)
            bgrd_image.setFixedHeight(20)

            separator1 = QtWidgets.QFrame()
            separator1.setFrameShape(QtWidgets.QFrame.HLine)
            separator1.setFrameShadow(QtWidgets.QFrame.Sunken)
            separator1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            separator1.setFixedHeight(10)

            separator2 = QtWidgets.QFrame()
            separator2.setFrameShape(QtWidgets.QFrame.HLine)
            separator2.setFrameShadow(QtWidgets.QFrame.Sunken)
            separator2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            separator2.setFixedHeight(10)

            self.calendar = QtWidgets.QCalendarWidget()
            self.calendar.setGridVisible(True)

            self.calendar.clicked.connect(self.set_date)

            time_hbox = QtWidgets.QHBoxLayout()
            time_hbox.setAlignment(QtCore.Qt.AlignLeft)

            time_label = Label(image=TIME)
            time_label.setFixedWidth(20)
            time_label.setFixedHeight(20) 

            self.fromto_label = Label(image=FROMTO)
            self.fromto_label.setFixedWidth(20)
            self.fromto_label.setFixedHeight(20)  
            self.fromto_label.hide()          

            self.ltime_label = Label(image=LTIME)
            self.ltime_label.setFixedWidth(20)
            self.ltime_label.setFixedHeight(20)  
            self.ltime_label.hide() 

            self.time_left_label = Label(text="") 
            self.start_time_label = Label(text='{0}/{1}/{2}'.format(self.start_time.day(), self.start_time.month(), self.start_time.year()))       

            self.end_time_label = Label(text="")

            time_hbox.addWidget(time_label)
            time_hbox.addWidget(self.start_time_label)
            time_hbox.addWidget(self.fromto_label)
            time_hbox.addWidget(self.end_time_label)
            time_hbox.addWidget(self.ltime_label)
            time_hbox.addWidget(self.time_left_label)
            
            discription_label = Label(text="Description : ")
            discription_label.setFixedHeight(20)
            discription_label.setAlignment(QtCore.Qt.AlignLeft)
            tasks_label = Label(text="Tasks : ")
            tasks_label.setFixedHeight(20)
            tasks_label.setAlignment(QtCore.Qt.AlignLeft)
            self.discription = QtWidgets.QTextEdit(edit_disp)
            self.discription.setFixedHeight(100)
            self.discription.setPlaceholderText("write your discription here ...!")
            self.discription.setReadOnly(True)

            self.cal_buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok| QtWidgets.QDialogButtonBox.Cancel)
            self.cal_buttonBox.accepted.connect(self.accept_date)
            self.cal_buttonBox.rejected.connect(self.reject_date)
            self.cal_buttonBox.hide()

            self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok| QtWidgets.QDialogButtonBox.Cancel)
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
            self.buttonBox.hide()

            tasks = QtWidgets.QHBoxLayout()
            self.disp_box.addWidget(discription_label)
            self.disp_box.addWidget(separator1)
            self.disp_box.addWidget(edit_disp)

            tasks.addWidget(tasks_label)
            tasks.addWidget(separator2)
            tasks.addWidget(new_task)

            self.tasks_box.addLayout(self.disp_box)
            self.tasks_box.addWidget(self.discription)
            self.tasks_box.addWidget(self.buttonBox)
            self.tasks_box.addLayout(tasks)

            self.tasks.setLayout(self.tasks_box)
            self.task_scroll.setWidget(self.tasks)

            top_label = QtWidgets.QHBoxLayout()
            top_label.addWidget(self.name_label)
            top_label.addWidget(calendar_label)
            top_label.addWidget(bgrd_color)
            top_label.addWidget(bgrd_image)

            self.vbox_info.addLayout(top_label)
            self.vbox_info.addLayout(time_hbox)
            self.vbox_info.addWidget(self.calendar)
            self.vbox_info.addWidget(self.cal_buttonBox)
            self.vbox_info.addWidget(self.task_scroll)
            self.info.setLayout(self.vbox_info)

            self.calendar.hide()

    def accept(self):
        self.discription.setReadOnly(True)
        self.buttonBox.hide()

    def reject(self):
        self.discription.setReadOnly(True)
        self.buttonBox.hide()

    def new_task(self, event):  
        layout = self.tasks_box.layout()
        task = Task(parent=self)
        layout.insertLayout(layout.count() + 1, task._vbox)
        self._tasks += [task]      

    def set_disp(self, event):
        self.discription.setReadOnly(not self.discription.isReadOnly())
        self.buttonBox.setVisible(not self.discription.isReadOnly())

    def set_bgrd_color(self, event):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.task_scroll.setStyleSheet("background-color:" + color.name() + " ; ")

    def set_bgrd_image(self, event):
        image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '', " (*.png *.jpg)")
        self.task_scroll.setStyleSheet("background-image : url(" + image_path + ");")

    def set_end_date(self, event):
        self.calendar.setVisible(not self.calendar.isVisible())
        self.cal_buttonBox.setVisible(self.calendar.isVisible())

    def printDateInfo(self, qDate):
        print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        print(f'Day Number of the year: {qDate.dayOfYear()}')
        print(f'Day Number of the week: {qDate.dayOfWeek()}')

        end_time   = ', {0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year())
        start_time = '{0}/{1}/{2}'.format(self.start_time.day(), self.start_time.month(), self.start_time.year())

        self.end_time_label.setText(start_time + end_time)

    def accept_date(self):
        self.cal_buttonBox.hide()
        self.start_time_label.setText(self.start_timing)
        self.end_time_label.setText(self.end_timing)
        self.calendar.hide()
        self.ltime_label.show()
        self.fromto_label.show()
        self.time_left_label.setText(self.time_left)

    def reject_date(self):
        self.cal_buttonBox.hide()
        self.calendar.hide()


    def set_date(self, qDate):
        self.end_time     = qDate
        time_left = 30*(self.end_time.month()  - self.start_time.month()) + (self.end_time.day()  - self.start_time.day())
        self.end_timing   = '{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year())
        self.start_timing = '{0}/{1}/{2}'.format(self.start_time.day(), self.start_time.month(), self.start_time.year())
        self.time_left    = "{0} days".format(time_left)

#================================================================================================


class Create_table(QtWidgets.QTableWidget):
    def __init__(self):
        super(Create_table, self).__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.setFont(font)
        self.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setColumnCount(4)
        self.setObjectName("Data_table")
        self.setHorizontalHeaderLabels(["Task", "Collaborators", "Priority", "Done"]) 
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setAlternatingRowColors(True)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #self.horizontalHeader().setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)

#====================================================================================================

class Create_account(QtWidgets.QWidget):
    def __init__(self):
        super(Create_account, self).__init__()
        self.setWindowTitle("Create an account")
        self.create_login()
        self.showMaximized()


    def create_login(self):
        centrale_box = QtWidgets.QVBoxLayout(self)
        centrale_box.setAlignment(QtCore.Qt.AlignCenter)
        create_account_label = Label(text="Create my account")
        self.photo_label  = Label(image=USER, function=self.set_profile_pec, hand=True)
        first_name_label = Label(text="First name")
        last_name_label = Label(text="Last name")
        email_label = Label(text="E-mail")
        password_label = Label(text="Password")
        cpassword_label = Label(text="Confirm password")
        self.first_name = QtWidgets.QLineEdit()
        self.last_name = QtWidgets.QLineEdit()
        self.email = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.cpassword = QtWidgets.QLineEdit()
        create = Button(text="create", function=self.create_account)
        back   = Button(text="back", function=self.back)
        create_account_label.setFont(QtGui.QFont('Arial', 30, QtGui.QFont.Bold))
        self.photo_label.setScaledContents(True)
        self.photo_label.setStyleSheet("QLabel::hover""{""background-color : lightblue;""}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.textChanged.connect(self.get_password)
        self.cpassword.textChanged.connect(self.get_cpassword)

        create.setStyleSheet("background-color : lightgreen;")

        self.show_pass = Label(image=EYE, function= self.show_password, hand=True)
        self.show_pass.setFixedWidth(15)
        self.show_pass.setFixedHeight(15)
        self.show_pass.hide()
        eye_pass      = QtWidgets.QHBoxLayout(self.password)
        eye_pass.setAlignment(QtCore.Qt.AlignRight)
        eye_pass.addWidget(self.show_pass)

        self.show_cpass = Label(image=EYE, function= self.show_cpassword, hand=True)
        self.show_cpass.setFixedWidth(15)
        self.show_cpass.setFixedHeight(15)
        self.show_cpass.hide()
        eye_pass      = QtWidgets.QHBoxLayout(self.cpassword)
        eye_pass.setAlignment(QtCore.Qt.AlignRight)
        eye_pass.addWidget(self.show_cpass)

        create_account_label.setFixedHeight(100)

        self.photo_label.setFixedWidth(100)
        self.photo_label.setFixedHeight(100)

        first_name_label.setFixedWidth(120)
        first_name_label.setFixedHeight(30)

        last_name_label.setFixedWidth(120)
        last_name_label.setFixedHeight(30)

        email_label.setFixedWidth(120)
        email_label.setFixedHeight(30)

        password_label.setFixedWidth(120)
        password_label.setFixedHeight(30)

        cpassword_label.setFixedWidth(120)
        cpassword_label.setFixedHeight(30)

        self.first_name.setFixedWidth(300)
        self.first_name.setFixedHeight(30)

        self.last_name.setFixedWidth(300)
        self.last_name.setFixedHeight(30)

        self.email.setFixedWidth(300)
        self.email.setFixedHeight(30)

        self.password.setFixedWidth(300)
        self.password.setFixedHeight(30)

        self.cpassword.setFixedWidth(300)
        self.cpassword.setFixedHeight(30)

        create.setFixedWidth(430)
        create.setFixedHeight(30)

        back.setFixedWidth(430)
        back.setFixedHeight(30)        


        create_account_hbox = QtWidgets.QHBoxLayout()
        photo_hbox          = QtWidgets.QHBoxLayout()
        first_name_hbox     = QtWidgets.QHBoxLayout()
        last_name_hbox      = QtWidgets.QHBoxLayout()
        email_hbox          = QtWidgets.QHBoxLayout()
        password_hbox       = QtWidgets.QHBoxLayout()
        cpassword_hbox      = QtWidgets.QHBoxLayout()
        create_hbox         = QtWidgets.QHBoxLayout()
        back_hbox           = QtWidgets.QHBoxLayout()

        create_account_hbox.setAlignment(QtCore.Qt.AlignCenter)
        photo_hbox.setAlignment(QtCore.Qt.AlignCenter)
        first_name_hbox.setAlignment(QtCore.Qt.AlignCenter)
        last_name_hbox.setAlignment(QtCore.Qt.AlignCenter)
        email_hbox.setAlignment(QtCore.Qt.AlignCenter)
        password_hbox.setAlignment(QtCore.Qt.AlignCenter)
        cpassword_hbox.setAlignment(QtCore.Qt.AlignCenter)
        create_hbox.setAlignment(QtCore.Qt.AlignCenter)
        back_hbox.setAlignment(QtCore.Qt.AlignCenter)

        create_account_hbox.addWidget(create_account_label)

        first_name_hbox.addWidget(first_name_label)
        first_name_hbox.addWidget(self.first_name)

        last_name_hbox.addWidget(last_name_label)
        last_name_hbox.addWidget(self.last_name)

        email_hbox.addWidget(email_label)
        email_hbox.addWidget(self.email)

        password_hbox.addWidget(password_label)
        password_hbox.addWidget(self.password)

        cpassword_hbox.addWidget(cpassword_label)
        cpassword_hbox.addWidget(self.cpassword)


        create_hbox.addWidget(create)

        back_hbox.addWidget(back)

        photo_hbox.addWidget(self.photo_label)

        centrale_box.addLayout(create_account_hbox)
        centrale_box.addLayout(photo_hbox)
        centrale_box.addLayout(first_name_hbox)
        centrale_box.addLayout(last_name_hbox)
        centrale_box.addLayout(email_hbox)
        centrale_box.addLayout(password_hbox)
        centrale_box.addLayout(cpassword_hbox)
        centrale_box.addLayout(create_hbox)
        centrale_box.addLayout(back_hbox)

    def get_password(self, text):
        if text:
            self.show_pass.show()
        else:
            self.show_pass.hide()

    def get_cpassword(self, text):
        if text:
            self.show_cpass.show()
        else:
            self.show_cpass.hide()

    def set_profile_pec(self, event):
        image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '', " (*.png *.jpg)")
        if image_path:
            image = QtGui.QImage(image_path)
            self.photo_label.setPixmap(QtGui.QPixmap.fromImage(image))
            self.photo_label.image = image

    def create_account(self, event):
        username = self.last_name.text() + self.first_name.text()[0]
        password = self.password.text()
        self.user = User(parent=self, name=username, password=password, image=self.photo_label.image)
        self.log_in()

    def show_password(self, event):
        self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        QtCore.QTimer.singleShot(1500, lambda:self.password.setEchoMode(QtWidgets.QLineEdit.Password))

    def show_cpassword(self, event):
        self.cpassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        QtCore.QTimer.singleShot(1500, lambda:self.cpassword.setEchoMode(QtWidgets.QLineEdit.Password))

    def log_in(self):
        self.window1 = Mainwindow(user=self.user)
        self.window1.show()
        self.close() 

    def back(self):
        self.window = Log_in()
        self.window.show()
        self.close() 

#=====================================================================================================

class Log_in(QtWidgets.QWidget):
    def __init__(self):
        super(Log_in, self).__init__()
        self.setWindowTitle("Log in")
        self.showMaximized()
        self.create_login()

    def create_login(self):
        centrale_box = QtWidgets.QVBoxLayout(self)
        centrale_box.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_label  = Label(image=USER)
        username_label = Label(text="username")
        password_label = Label(text="password")
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.textChanged.connect(self.get_password)
        submit = Button(text="submit", function=self.connect)
        separator1 = QtWidgets.QFrame()
        separator2 = QtWidgets.QFrame()
        or_label = Label(text=" or ")
        create_account = Button(text="create an account", function=self.new_account)
        self.photo_label.setScaledContents(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        create_account.setStyleSheet("background-color : lightgreen;")
        separator1.setFrameShape(QtWidgets.QFrame.HLine)
        separator1.setFrameShadow(QtWidgets.QFrame.Sunken)
        separator2.setFrameShape(QtWidgets.QFrame.HLine)
        separator2.setFrameShadow(QtWidgets.QFrame.Sunken)
        separator1.setFixedWidth(130)
        separator2.setFixedWidth(130)

        self.show_pass = Label(image=EYE, function= self.show_password, hand=True)
        self.show_pass.setFixedWidth(15)
        self.show_pass.setFixedHeight(15)
        self.show_pass.hide()
        eye_pass      = QtWidgets.QHBoxLayout(self.password)
        eye_pass.setAlignment(QtCore.Qt.AlignRight)
        eye_pass.addWidget(self.show_pass)


        self.photo_label.setFixedWidth(200)
        self.photo_label.setFixedHeight(200)

        username_label.setFixedWidth(100)
        username_label.setFixedHeight(30)

        password_label.setFixedWidth(100)
        password_label.setFixedHeight(30)

        self.username.setFixedWidth(200)
        self.username.setFixedHeight(30)

        self.password.setFixedWidth(200)
        self.password.setFixedHeight(30)

        submit.setFixedWidth(310)
        submit.setFixedHeight(30)

        create_account.setFixedWidth(310)
        create_account.setFixedHeight(30)

        photo_hbox      = QtWidgets.QHBoxLayout()
        username_hbox   = QtWidgets.QHBoxLayout()
        password_hbox   = QtWidgets.QHBoxLayout()
        submit_hbox     = QtWidgets.QHBoxLayout()
        or_hbox         = QtWidgets.QHBoxLayout()
        new_acount_hbox = QtWidgets.QHBoxLayout()

        photo_hbox.setAlignment(QtCore.Qt.AlignCenter)
        username_hbox.setAlignment(QtCore.Qt.AlignCenter)
        password_hbox.setAlignment(QtCore.Qt.AlignCenter)
        submit_hbox.setAlignment(QtCore.Qt.AlignCenter)
        or_hbox.setAlignment(QtCore.Qt.AlignCenter)
        new_acount_hbox.setAlignment(QtCore.Qt.AlignCenter)

        photo_hbox.addWidget(self.photo_label)

        username_hbox.addWidget(username_label)
        username_hbox.addWidget(self.username)

        password_hbox.addWidget(password_label)
        password_hbox.addWidget(self.password)

        submit_hbox.addWidget(submit)

        or_hbox.addWidget(separator1)
        or_hbox.addWidget(or_label)
        or_hbox.addWidget(separator2)

        new_acount_hbox.addWidget(create_account)

        centrale_box.addLayout(photo_hbox)
        centrale_box.addLayout(username_hbox)
        centrale_box.addLayout(password_hbox)
        centrale_box.addLayout(submit_hbox)
        centrale_box.addLayout(or_hbox)
        centrale_box.addLayout(new_acount_hbox)

    def new_account(self, event):
        self.window1 = Create_account()
        self.window1.show()
        self.close() 


    def submit(self):
        username = self.username.text()
        password = self.password.text()
        #if username in USERS:
            #if username.password == password:
        self.user = User(parent=self, name=username, password=password)

    def show_password(self, event):
        self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        QtCore.QTimer.singleShot(1500, lambda:self.password.setEchoMode(QtWidgets.QLineEdit.Password))

    def get_password(self, text):
        if text:
            self.show_pass.show()
        else:
            self.show_pass.hide()

    def set_profile_pec(self, event):
        image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '', " (*.png *.jpg)")
        if image_path:
            image = QtGui.QImage(image_path)
            self.photo_label.setPixmap(QtGui.QPixmap.fromImage(image))
            self.photo_label.image = image

    def connect(self):
        self.submit()
        self.window = Mainwindow(user=self.user)
        self.window.show()
        self.close() 


#======================================================================================================

class Mainwindow(QtWidgets.QWidget):
    def __init__(self, user):
        super(Mainwindow, self).__init__()
        self.setWindowTitle("Handle my projects")
        self.user = user

        self.create_project_box()
        self.create_up_box()
        self.initiate_parameters()
        self.create_projects_scroll()

        main_layout     = QtWidgets.QVBoxLayout()
        centrale_layout = QtWidgets.QHBoxLayout()
        centrale_layout.addLayout(self.projects_box)
        centrale_layout.addLayout(self.project_box)
        main_layout.addLayout(self.up_box)
        main_layout.addLayout(centrale_layout)
        self.setLayout(main_layout)
        self.showMaximized()

    def initiate_parameters(self):
        self.projects_count = 1
        self._projects       = []

    def create_up_box(self):
        self.up_box = QtWidgets.QHBoxLayout()
        self.up_box.setAlignment(QtCore.Qt.AlignRight)
        self.up_box.addWidget(self.user) 
        self.up_box.addWidget(Label(text=self.user.name))       


    def create_projects_scroll(self):
        self.projects = QtWidgets.QWidget()
        self.projects_box  = QtWidgets.QVBoxLayout()
        self.projects_vbox = QtWidgets.QVBoxLayout()
        self.projects_scroll = QtWidgets.QScrollArea()
        self.projects_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.projects_scroll.setWidgetResizable(True)
        self.projects_scroll.setFixedWidth(300)

        self.projects_label = Label(text="My Projects")
        self.projects_label.setFont(QtGui.QFont('Arial', 10, QtGui.QFont.Bold))
        self.projects_label.setAlignment(QtCore.Qt.AlignLeft)

        self.show_project = Label(image=SHOW, function=self.hide_projects, hand=True)
        self.show_project.setFixedHeight(20)
        self.show_project.setFixedWidth(20)

        self.move_up   = Label(image=UP,   function=self.move_up,   hand=True)
        self.move_down = Label(image=DOWN, function=self.move_down, hand=True)
        self.move_up.setFixedHeight(20)
        self.move_up.setFixedWidth(20)
        self.move_down.setFixedHeight(20)
        self.move_down.setFixedWidth(20)

        self.new_project = Label(image=NEW, function=self.new_project, hand=True)
        self.new_project.setAlignment(QtCore.Qt.AlignRight)
        #new_project.setStyleSheet("QLabel::hover""{""background-color : lightblue;""}")
        self.new_project.setFixedHeight(20)
        self.new_project.setFixedWidth(20)
        projects_hbox = QtWidgets.QHBoxLayout()

        projects_group_box = QtWidgets.QGroupBox()

        projects_hbox.addWidget(self.projects_label)
        projects_hbox.addWidget(self.show_project)
        projects_hbox.addWidget(self.move_down)
        projects_hbox.addWidget(self.move_up)
        projects_hbox.addWidget(self.new_project)

        self.projects_box.addLayout(projects_hbox)

        self.projects.setLayout(self.projects_vbox)
        self.projects_scroll.setWidget(self.projects)
        self.projects_box.addWidget(self.projects_scroll)

        layout = self.projects_vbox.layout()
        project0 = Project(parent=self, text="My First Project", range_=1)
        project0.delete_label.show()
        project0.color_label.show()
        project0.text_label.show()
        project0.setStyleSheet("background-color :" + project0.color + ";")
        self.current_project = project0
        layout.insertWidget(layout.count() + 1, project0)
        self.project_box.addWidget(project0.info)
        self._projects += [project0]

    def create_project_box(self):
        self.project_box = QtWidgets.QStackedLayout()

    def new_project(self, event):
        layout = self.projects_vbox.layout()
        project = Project(parent=self, text="Project " + str(layout.count() + 1), range_=layout.count() + 1)
        layout.insertWidget(layout.count() + 1, project)
        self.project_box.addWidget(project.info)
        self._projects += [project]

    def move_up(self, event):
        layout = self.projects_vbox.layout()
        if self.current_project.range > 1 :
            previous_p = self.previous_project()
            self.current_project.range , previous_p.range = previous_p.range, self.current_project.range
            layout.insertWidget(self.current_project.range - 1, self.current_project)

    def move_down(self, event):
        layout = self.projects_vbox.layout()
        if self.current_project.range < layout.count():
            next_p = self.next_project()
            self.current_project.range , next_p.range = next_p.range, self.current_project.range
            layout.insertWidget(self.current_project.range - 1, self.current_project)

    def next_project(self):
        for project in self._projects:
            if project.range == self.current_project.range + 1:
                return project      

    def previous_project(self):
        for project in self._projects:
            if project.range == self.current_project.range - 1:
                return project   

    def hide_projects(self, event):
        self.projects_scroll.setHidden(not self.projects_scroll.isHidden())
        self.new_project.setVisible(not self.new_project.isVisible())
        self.projects_label.setVisible(not self.projects_label.isVisible())
        self.move_down.setVisible(not self.move_down.isVisible())
        self.move_up.setVisible(not self.move_up.isVisible())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Log_in()
    window.show()
    sys.exit(app.exec())