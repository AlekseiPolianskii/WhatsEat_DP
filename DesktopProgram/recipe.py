# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recipe.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class RecipeWidgets(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 502)
        self.name_recipe = QtWidgets.QLabel(Form)
        self.name_recipe.setGeometry(QtCore.QRect(60, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name_recipe.setFont(font)
        self.name_recipe.setObjectName("name_recipe")
        self.image_recipe = QtWidgets.QLabel(Form)
        self.image_recipe.setGeometry(QtCore.QRect(20, 20, 361, 151))
        self.image_recipe.setStyleSheet("border-radius: 20px;")
        self.image_recipe.setText("")
        self.image_recipe.setObjectName("image_recipe")
        self.list_ingridients = QtWidgets.QWidget(Form)
        self.list_ingridients.setGeometry(QtCore.QRect(19, 249, 361, 241))
        self.list_ingridients.setObjectName("list_ingridients")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_recipe.setText(_translate("Form", "TextLabel"))