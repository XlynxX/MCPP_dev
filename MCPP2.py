# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import mainrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(402, 242)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/res/MCPP.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-image: url(:/background/res/background.png);")
        MainWindow.setIconSize(QSize(512, 512))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label1 = QLabel(self.centralwidget)
        self.label1.setObjectName(u"label1")
        self.label1.setEnabled(False)
        self.label1.setGeometry(QRect(50, 10, 301, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Minecraft Rus")
        font.setPointSize(12)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.NoAntialias)
        self.label1.setFont(font)
        self.label1.setLayoutDirection(Qt.LeftToRight)
        self.label1.setAutoFillBackground(False)
        self.label1.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.label1.setInputMethodHints(Qt.ImhNone)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")
        self.label2.setEnabled(False)
        self.label2.setGeometry(QRect(50, 50, 301, 21))
        sizePolicy1.setHeightForWidth(self.label2.sizePolicy().hasHeightForWidth())
        self.label2.setSizePolicy(sizePolicy1)
        self.label2.setFont(font)
        self.label2.setLayoutDirection(Qt.LeftToRight)
        self.label2.setAutoFillBackground(False)
        self.label2.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.label2.setInputMethodHints(Qt.ImhNone)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton1 = QPushButton(self.centralwidget)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setEnabled(True)
        self.pushButton1.setGeometry(QRect(50, 41, 300, 40))
        sizePolicy1.setHeightForWidth(self.pushButton1.sizePolicy().hasHeightForWidth())
        self.pushButton1.setSizePolicy(sizePolicy1)
        self.pushButton1.setFont(font)
        self.pushButton1.setMouseTracking(False)
        self.pushButton1.setFocusPolicy(Qt.NoFocus)
        self.pushButton1.setLayoutDirection(Qt.LeftToRight)
        self.pushButton1.setAutoFillBackground(False)
        self.pushButton1.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	\n"
"	border-image: url(:/buttons/res/btn_default.png);\n"
"	padding: 0;\n"
"	border: none;\n"
"	text-decoration: none;\n"
"	text-align: center;\n"
"	color: white;\n"
"	padding-top: 0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	\n"
"	border-image: url(:/buttons/res/btn_hover.png);\n"
"}")
        self.pushButton1.setFlat(False)
        self.label3 = QLabel(self.centralwidget)
        self.label3.setObjectName(u"label3")
        self.label3.setEnabled(False)
        self.label3.setGeometry(QRect(50, 98, 301, 21))
        sizePolicy1.setHeightForWidth(self.label3.sizePolicy().hasHeightForWidth())
        self.label3.setSizePolicy(sizePolicy1)
        self.label3.setFont(font)
        self.label3.setLayoutDirection(Qt.LeftToRight)
        self.label3.setAutoFillBackground(False)
        self.label3.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.label3.setInputMethodHints(Qt.ImhNone)
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setEnabled(True)
        self.pushButton2.setGeometry(QRect(50, 89, 300, 40))
        sizePolicy1.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy1)
        self.pushButton2.setFont(font)
        self.pushButton2.setMouseTracking(False)
        self.pushButton2.setFocusPolicy(Qt.NoFocus)
        self.pushButton2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton2.setAutoFillBackground(False)
        self.pushButton2.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	\n"
"	border-image: url(:/buttons/res/btn_default.png);\n"
"	padding: 0;\n"
"	border: none;\n"
"	text-decoration: none;\n"
"	text-align: center;\n"
"	color: white;\n"
"	padding-top: 0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	\n"
"	border-image: url(:/buttons/res/btn_hover.png);\n"
"}")
        self.pushButton2.setFlat(False)
        self.labelDone = QLabel(self.centralwidget)
        self.labelDone.setObjectName(u"labelDone")
        self.labelDone.setEnabled(False)
        self.labelDone.setGeometry(QRect(50, 189, 301, 21))
        sizePolicy1.setHeightForWidth(self.labelDone.sizePolicy().hasHeightForWidth())
        self.labelDone.setSizePolicy(sizePolicy1)
        self.labelDone.setFont(font)
        self.labelDone.setLayoutDirection(Qt.LeftToRight)
        self.labelDone.setAutoFillBackground(False)
        self.labelDone.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.labelDone.setInputMethodHints(Qt.ImhNone)
        self.labelDone.setAlignment(Qt.AlignCenter)
        self.labelDone.setTextInteractionFlags(Qt.NoTextInteraction)
        self.doneButton = QPushButton(self.centralwidget)
        self.doneButton.setObjectName(u"doneButton")
        self.doneButton.setEnabled(True)
        self.doneButton.setGeometry(QRect(50, 180, 300, 40))
        sizePolicy1.setHeightForWidth(self.doneButton.sizePolicy().hasHeightForWidth())
        self.doneButton.setSizePolicy(sizePolicy1)
        self.doneButton.setFont(font)
        self.doneButton.setMouseTracking(False)
        self.doneButton.setFocusPolicy(Qt.NoFocus)
        self.doneButton.setLayoutDirection(Qt.LeftToRight)
        self.doneButton.setAutoFillBackground(False)
        self.doneButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	\n"
"	border-image: url(:/buttons/res/btn_default.png);\n"
"	padding: 0;\n"
"	border: none;\n"
"	text-decoration: none;\n"
"	text-align: center;\n"
"	color: white;\n"
"	padding-top: 0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	\n"
"	border-image: url(:/buttons/res/btn_hover.png);\n"
"}")
        self.doneButton.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.doneButton.raise_()
        self.labelDone.raise_()
        self.pushButton2.raise_()
        self.label3.raise_()
        self.pushButton1.raise_()
        self.label2.raise_()
        self.label1.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MCPP", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a\u0438", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
#if QT_CONFIG(tooltip)
        self.pushButton1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton1.setText("")
        self.label3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
#if QT_CONFIG(tooltip)
        self.pushButton2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton2.setText("")
        self.labelDone.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
#if QT_CONFIG(tooltip)
        self.doneButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.doneButton.setText("")
    # retranslateUi

