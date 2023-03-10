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
        TinyPngApp.resize(522, 283)
        self.layoutWidget = QtWidgets.QWidget(TinyPngApp)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 501, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.apiText = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apiText.sizePolicy().hasHeightForWidth())
        self.apiText.setSizePolicy(sizePolicy)
        self.apiText.setMaximumSize(QtCore.QSize(371, 16777215))
        self.apiText.setObjectName("apiText")
        self.horizontalLayout_3.addWidget(self.apiText)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.srcText = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.srcText.sizePolicy().hasHeightForWidth())
        self.srcText.setSizePolicy(sizePolicy)
        self.srcText.setMaximumSize(QtCore.QSize(300, 16777215))
        self.srcText.setObjectName("srcText")
        self.horizontalLayout_2.addWidget(self.srcText)
        self.srcBrowseBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.srcBrowseBtn.sizePolicy().hasHeightForWidth())
        self.srcBrowseBtn.setSizePolicy(sizePolicy)
        self.srcBrowseBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.srcBrowseBtn.setFont(font)
        self.srcBrowseBtn.setAutoFillBackground(False)
        self.srcBrowseBtn.setObjectName("srcBrowseBtn")
        self.horizontalLayout_2.addWidget(self.srcBrowseBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dstText = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dstText.sizePolicy().hasHeightForWidth())
        self.dstText.setSizePolicy(sizePolicy)
        self.dstText.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dstText.setObjectName("dstText")
        self.horizontalLayout.addWidget(self.dstText)
        self.dstBrowseBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dstBrowseBtn.sizePolicy().hasHeightForWidth())
        self.dstBrowseBtn.setSizePolicy(sizePolicy)
        self.dstBrowseBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.dstBrowseBtn.setFont(font)
        self.dstBrowseBtn.setAutoFillBackground(False)
        self.dstBrowseBtn.setObjectName("dstBrowseBtn")
        self.horizontalLayout.addWidget(self.dstBrowseBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.statusLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.statusLabel.setFont(font)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.skipCB = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.skipCB.setFont(font)
        self.skipCB.setObjectName("skipCB")
        self.verticalLayout.addWidget(self.skipCB)
        self.startBtn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        self.verticalLayout.addWidget(self.startBtn)

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
        self.skipCB.setText(_translate("TinyPngApp", "跳過重複檔案"))
        self.startBtn.setText(_translate("TinyPngApp", "Start"))
