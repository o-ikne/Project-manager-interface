
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets import Button, Radio_Button, Label
from user import User
from task import Task
from project import Project

NEW      = "icons/new_icon.png"
COLOR    = "icons/color_icon.png"
EDIT     = "icons/edit_icon.png"
REMOVE   = "icons/remove_icon.png"
PHOTO    = "icons/photo_icon.png"
MORE     = "icons/more_icon.png"
CALENDER = "icons/calender_icon.png"
TIME     = "icons/time_icon.png"
USER     = "icons/user_icon.png"
EYE      = "icons/eye_icon.png"
ACCEPT   = "icons/accept_icon.png"
REJECT   = "icons/reject_icon.png"
LTIME    = "icons/lefttime_icon.png"
FROMTO   = "icons/fromto_icon.png"
TASK     = "icons/task_icon.png"
UP       = "icons/move_up_icon.png"
DOWN     = "icons/move_down_icon.png"
SHOW     = "icons/show_projects_icon.png"
NOTYET   = "icons/not_yet_icon.png"
PROGRESS = "icons/in_progress_icon.png"


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
        self.projects_count = 10
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

        self.new_project = Label(image=NEW, function=self.new_project_, hand=True)
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

        for _ in range(10):
            self.new_project_(None)


    def create_project_box(self):
        self.project_box = QtWidgets.QStackedLayout()

    def new_project_(self, event):
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