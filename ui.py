# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TinyPngApp(object):
    def setupUi(self, TinyPngApp):
        TinyPngApp.setObjectName("TinyPngApp")
        TinyPngApp.resize(500, 270)
        self.verticalLayoutWidget = QtWidgets.QWidget(TinyPngApp)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(51, 35))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.apiText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.apiText.setObjectName("apiText")
        self.horizontalLayout_3.addWidget(self.apiText)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(51, 35))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.srcText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.srcText.setObjectName("srcText")
        self.horizontalLayout_2.addWidget(self.srcText)
        self.srcBrowseBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.srcBrowseBtn.sizePolicy().hasHeightForWidth())
        self.srcBrowseBtn.setSizePolicy(sizePolicy)
        self.srcBrowseBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.srcBrowseBtn.setAutoFillBackground(False)
        self.srcBrowseBtn.setObjectName("srcBrowseBtn")
        self.horizontalLayout_2.addWidget(self.srcBrowseBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(51, 35))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dstText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.dstText.setObjectName("dstText")
        self.horizontalLayout.addWidget(self.dstText)
        self.dstBrowseBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dstBrowseBtn.sizePolicy().hasHeightForWidth())
        self.dstBrowseBtn.setSizePolicy(sizePolicy)
        self.dstBrowseBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.dstBrowseBtn.setAutoFillBackground(False)
        self.dstBrowseBtn.setObjectName("dstBrowseBtn")
        self.horizontalLayout.addWidget(self.dstBrowseBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.startBtn = QtWidgets.QPushButton(TinyPngApp)
        self.startBtn.setGeometry(QtCore.QRect(420, 240, 75, 23))
        self.startBtn.setObjectName("startBtn")
        self.statusLabel = QtWidgets.QLabel(TinyPngApp)
        self.statusLabel.setGeometry(QtCore.QRect(10, 240, 391, 23))
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")

        self.retranslateUi(TinyPngApp)
        QtCore.QMetaObject.connectSlotsByName(TinyPngApp)

    def retranslateUi(self, TinyPngApp):
        _translate = QtCore.QCoreApplication.translate
        TinyPngApp.setWindowTitle(_translate("TinyPngApp", "TinyPngApp"))
        self.label.setText(_translate("TinyPngApp", "API Key"))
        self.label_2.setText(_translate("TinyPngApp", "Source:"))
        self.srcBrowseBtn.setText(_translate("TinyPngApp", "Browse"))
        self.label_3.setText(_translate("TinyPngApp", "Destination:"))
        self.dstBrowseBtn.setText(_translate("TinyPngApp", "Browse"))
        self.startBtn.setText(_translate("TinyPngApp", "Start"))
