
from PyQt5 import QtWidgets, QtGui, QtCore
from widgets import Radio_Button, Label


NEW      = "icons/new_icon.png"
COLOR    = "icons/color_icon.png"
EDIT     = "icons/edit_icon.png"
REMOVE   = "icons/remove_icon.png"
MORE     = "icons/more_icon.png"
ACCEPT   = "icons/accept_icon.png"
REJECT   = "icons/reject_icon.png"
LOW      = "icons/low_priority_icon.png"
MEDIUM   = "icons/medium_priority_icon.png"
HIGH     = "icons/high_priority_icon.png"
VERYHIGH = "icons/veryhigh_priority_icon.png"
TASK     = "icons/task_icon.png"
NOTYET   = "icons/not_yet_icon.png"
PHOTO    = "icons/photo_icon.png"
PROGRESS = "icons/in_progress_icon.png"

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
