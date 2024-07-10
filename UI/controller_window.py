# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller_windoww.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(292, 153)
        self.move_to_initial_position_pushButton = QtWidgets.QPushButton(Form)
        self.move_to_initial_position_pushButton.setGeometry(QtCore.QRect(0, 10, 161, 31))
        self.move_to_initial_position_pushButton.setObjectName("move_to_initial_position_pushButton")
        self.pick_up_pushButton = QtWidgets.QPushButton(Form)
        self.pick_up_pushButton.setGeometry(QtCore.QRect(190, 10, 101, 31))
        self.pick_up_pushButton.setObjectName("pick_up_pushButton")
        self.ompl_checkBox = QtWidgets.QCheckBox(Form)
        self.ompl_checkBox.setGeometry(QtCore.QRect(10, 50, 92, 23))
        self.ompl_checkBox.setObjectName("ompl_checkBox")
        self.chomp_checkBox = QtWidgets.QCheckBox(Form)
        self.chomp_checkBox.setGeometry(QtCore.QRect(10, 90, 92, 23))
        self.chomp_checkBox.setObjectName("chomp_checkBox")
        self.grab_pushButton = QtWidgets.QPushButton(Form)
        self.grab_pushButton.setGeometry(QtCore.QRect(200, 50, 89, 25))
        self.grab_pushButton.setObjectName("grab_pushButton")
        self.open_pushButton = QtWidgets.QPushButton(Form)
        self.open_pushButton.setGeometry(QtCore.QRect(200, 120, 89, 25))
        self.open_pushButton.setObjectName("open_pushButton")
        self.place_on_red_pushButton = QtWidgets.QPushButton(Form)
        self.place_on_red_pushButton.setGeometry(QtCore.QRect(10, 120, 191, 25))
        self.place_on_red_pushButton.setObjectName("place_on_red_pushButton")
        self.pick_and_place_pushButton = QtWidgets.QPushButton(Form)
        self.pick_and_place_pushButton.setGeometry(QtCore.QRect(180, 80, 111, 25))
        self.pick_and_place_pushButton.setObjectName("pick_and_place_pushButton")

        self.retranslateUi(Form)
        self.move_to_initial_position_pushButton.clicked.connect(Form.Move_to_initial_position)
        self.pick_up_pushButton.clicked.connect(Form.Pick_up_the_block)
        self.place_on_red_pushButton.clicked.connect(Form.Place_on_red)
        self.grab_pushButton.clicked.connect(Form.Grab)
        self.open_pushButton.clicked.connect(Form.Open)
        self.pick_and_place_pushButton.clicked.connect(Form.Pick_and_place)
        self.ompl_checkBox.clicked.connect(Form.OMPL_planner)
        self.chomp_checkBox.clicked.connect(Form.CHOMP_planner)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "controller"))
        self.move_to_initial_position_pushButton.setText(_translate("Form", "Move to initial postion "))
        self.pick_up_pushButton.setText(_translate("Form", "Move the arm"))
        self.ompl_checkBox.setText(_translate("Form", "OMPL"))
        self.chomp_checkBox.setText(_translate("Form", "CHOMP"))
        self.grab_pushButton.setText(_translate("Form", "Grab"))
        self.open_pushButton.setText(_translate("Form", "Open"))
        self.place_on_red_pushButton.setText(_translate("Form", "Place on the red cylinder"))
        self.pick_and_place_pushButton.setText(_translate("Form", "Pick and Place"))