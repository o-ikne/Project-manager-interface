

from PyQt5 import QtCore, QtGui, QtWidgets
from widgets import Button, Radio_Button, Label
from task import Task



NEW      = "icons/new_icon.png"
COLOR    = "icons/color_icon.png"
EDIT     = "icons/edit_icon.png"
REMOVE   = "icons/remove_icon.png"
MORE     = "icons/more_icon.png"
ACCEPT   = "icons/accept_icon.png"
CALENDER = "icons/calender_icon.png"
PHOTO    = "icons/photo_icon.png"
TIME     = "icons/time_icon.png"
FROMTO   = "icons/fromto_icon.png"
LTIME    = "icons/lefttime_icon.png"
REJECT   = "icons/reject_icon.png"



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