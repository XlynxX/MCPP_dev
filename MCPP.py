# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QSize, QRect, QCoreApplication, QMetaObject
from PySide2.QtGui import QIcon, QFont, Qt
from PySide2.QtWidgets import QSizePolicy, QWidget, QStackedWidget, QLabel, QPushButton, QScrollArea, QFrame

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
        MainWindow.setMinimumSize(QSize(402, 242))
        MainWindow.setMaximumSize(QSize(402, 242))
        MainWindow.setWindowTitle(u"MCPP")
        icon = QIcon()
        icon.addFile(u":/icons/res/MCPP.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-image: url(:/background/res/background.png);")
        MainWindow.setIconSize(QSize(512, 512))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 402, 242))
        self.stackedWidget.setMinimumSize(QSize(402, 242))
        self.stackedWidget.setMaximumSize(QSize(402, 242))
        font = QFont()
        font.setKerning(False)
        font.setStyleStrategy(QFont.NoAntialias)
        self.stackedWidget.setFont(font)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label3 = QLabel(self.page)
        self.label3.setObjectName(u"label3")
        self.label3.setEnabled(False)
        self.label3.setGeometry(QRect(40, 126, 301, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label3.sizePolicy().hasHeightForWidth())
        self.label3.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Minecraft Rus")
        font1.setPointSize(12)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        font1.setStyleStrategy(QFont.NoAntialias)
        self.label3.setFont(font1)
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
        self.label4 = QLabel(self.page)
        self.label4.setObjectName(u"label4")
        self.label4.setEnabled(False)
        self.label4.setGeometry(QRect(40, 174, 301, 21))
        sizePolicy1.setHeightForWidth(self.label4.sizePolicy().hasHeightForWidth())
        self.label4.setSizePolicy(sizePolicy1)
        self.label4.setFont(font1)
        self.label4.setLayoutDirection(Qt.LeftToRight)
        self.label4.setAutoFillBackground(False)
        self.label4.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.label4.setInputMethodHints(Qt.ImhNone)
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton1 = QPushButton(self.page)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setEnabled(True)
        self.pushButton1.setGeometry(QRect(40, 21, 300, 40))
        sizePolicy1.setHeightForWidth(self.pushButton1.sizePolicy().hasHeightForWidth())
        self.pushButton1.setSizePolicy(sizePolicy1)
        self.pushButton1.setFont(font1)
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
        self.pushButton3 = QPushButton(self.page)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setEnabled(True)
        self.pushButton3.setGeometry(QRect(40, 117, 300, 40))
        sizePolicy1.setHeightForWidth(self.pushButton3.sizePolicy().hasHeightForWidth())
        self.pushButton3.setSizePolicy(sizePolicy1)
        self.pushButton3.setFont(font1)
        self.pushButton3.setMouseTracking(False)
        self.pushButton3.setFocusPolicy(Qt.NoFocus)
        self.pushButton3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton3.setAutoFillBackground(False)
        self.pushButton3.setStyleSheet(u"QPushButton\n"
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
        self.pushButton3.setFlat(False)
        self.label2 = QLabel(self.page)
        self.label2.setObjectName(u"label2")
        self.label2.setEnabled(False)
        self.label2.setGeometry(QRect(40, 78, 301, 21))
        sizePolicy1.setHeightForWidth(self.label2.sizePolicy().hasHeightForWidth())
        self.label2.setSizePolicy(sizePolicy1)
        self.label2.setFont(font1)
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
        self.pushButton4 = QPushButton(self.page)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setEnabled(True)
        self.pushButton4.setGeometry(QRect(40, 165, 300, 40))
        sizePolicy1.setHeightForWidth(self.pushButton4.sizePolicy().hasHeightForWidth())
        self.pushButton4.setSizePolicy(sizePolicy1)
        self.pushButton4.setFont(font1)
        self.pushButton4.setMouseTracking(False)
        self.pushButton4.setFocusPolicy(Qt.NoFocus)
        self.pushButton4.setLayoutDirection(Qt.LeftToRight)
        self.pushButton4.setAutoFillBackground(False)
        self.pushButton4.setStyleSheet(u"QPushButton\n"
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
        self.pushButton4.setFlat(False)
        self.label1 = QLabel(self.page)
        self.label1.setObjectName(u"label1")
        self.label1.setEnabled(False)
        self.label1.setGeometry(QRect(40, 30, 301, 21))
        sizePolicy1.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy1)
        self.label1.setFont(font1)
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
        self.pushButton2 = QPushButton(self.page)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setEnabled(True)
        self.pushButton2.setGeometry(QRect(40, 69, 300, 40))
        sizePolicy1.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy1)
        self.pushButton2.setFont(font1)
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
        self.langButton = QPushButton(self.page)
        self.langButton.setObjectName(u"langButton")
        self.langButton.setEnabled(True)
        self.langButton.setGeometry(QRect(350, 20, 40, 40))
        sizePolicy1.setHeightForWidth(self.langButton.sizePolicy().hasHeightForWidth())
        self.langButton.setSizePolicy(sizePolicy1)
        self.langButton.setFont(font1)
        self.langButton.setMouseTracking(False)
        self.langButton.setFocusPolicy(Qt.NoFocus)
        self.langButton.setLayoutDirection(Qt.LeftToRight)
        self.langButton.setAutoFillBackground(False)
        self.langButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/buttons/res/btn_lang.png);\n"
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
"	\n"
"	border-image: url(:/buttons/res/btn_lang_hover.png);\n"
"}")
        self.langButton.setFlat(False)
        self.VersionLabel = QLabel(self.page)
        self.VersionLabel.setObjectName(u"VersionLabel")
        self.VersionLabel.setEnabled(False)
        self.VersionLabel.setGeometry(QRect(5, 222, 181, 21))
        sizePolicy1.setHeightForWidth(self.VersionLabel.sizePolicy().hasHeightForWidth())
        self.VersionLabel.setSizePolicy(sizePolicy1)
        self.VersionLabel.setFont(font1)
        self.VersionLabel.setLayoutDirection(Qt.LeftToRight)
        self.VersionLabel.setAutoFillBackground(False)
        self.VersionLabel.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.VersionLabel.setInputMethodHints(Qt.ImhNone)
        self.VersionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.VersionLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.CopytightLabel = QLabel(self.page)
        self.CopytightLabel.setObjectName(u"CopytightLabel")
        self.CopytightLabel.setEnabled(False)
        self.CopytightLabel.setGeometry(QRect(220, 222, 181, 21))
        sizePolicy1.setHeightForWidth(self.CopytightLabel.sizePolicy().hasHeightForWidth())
        self.CopytightLabel.setSizePolicy(sizePolicy1)
        self.CopytightLabel.setFont(font1)
        self.CopytightLabel.setLayoutDirection(Qt.LeftToRight)
        self.CopytightLabel.setAutoFillBackground(False)
        self.CopytightLabel.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.CopytightLabel.setInputMethodHints(Qt.ImhNone)
        self.CopytightLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.CopytightLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.stackedWidget.addWidget(self.page)
        self.pushButton4.raise_()
        self.pushButton3.raise_()
        self.pushButton2.raise_()
        self.label3.raise_()
        self.label4.raise_()
        self.pushButton1.raise_()
        self.label2.raise_()
        self.label1.raise_()
        self.langButton.raise_()
        self.VersionLabel.raise_()
        self.CopytightLabel.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-image: url(:/background/res/background_label.png);")
        self.labelDone = QLabel(self.page_2)
        self.labelDone.setObjectName(u"labelDone")
        self.labelDone.setEnabled(False)
        self.labelDone.setGeometry(QRect(50, 199, 301, 21))
        sizePolicy1.setHeightForWidth(self.labelDone.sizePolicy().hasHeightForWidth())
        self.labelDone.setSizePolicy(sizePolicy1)
        self.labelDone.setFont(font1)
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
        self.doneButton = QPushButton(self.page_2)
        self.doneButton.setObjectName(u"doneButton")
        self.doneButton.setEnabled(True)
        self.doneButton.setGeometry(QRect(50, 190, 300, 40))
        sizePolicy1.setHeightForWidth(self.doneButton.sizePolicy().hasHeightForWidth())
        self.doneButton.setSizePolicy(sizePolicy1)
        self.doneButton.setFont(font1)
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
        self.label3_2 = QLabel(self.page_2)
        self.label3_2.setObjectName(u"label3_2")
        self.label3_2.setEnabled(False)
        self.label3_2.setGeometry(QRect(50, 10, 301, 21))
        sizePolicy1.setHeightForWidth(self.label3_2.sizePolicy().hasHeightForWidth())
        self.label3_2.setSizePolicy(sizePolicy1)
        self.label3_2.setFont(font1)
        self.label3_2.setLayoutDirection(Qt.LeftToRight)
        self.label3_2.setAutoFillBackground(False)
        self.label3_2.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.label3_2.setInputMethodHints(Qt.ImhNone)
        self.label3_2.setAlignment(Qt.AlignCenter)
        self.label3_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(20, 34, 371, 145))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(100)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setMaximumSize(QSize(371, 151))
        self.scrollArea.setFont(font)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"QScrollArea\n"
"{\n"
"	background-color:transparent;\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"QScrollBar:vertical\n"
" {\n"
"	border: none;\n"
"    background:none;\n"
"    width:13px;\n"
"	margin: 0px 0px 0px 0px;\n"
" }\n"
" QScrollBar::handle:vertical\n"
" {\n"
"	\n"
"	border-image: url(:/buttons/res/scrollbar.png);\n"
"	background-color: rgb(0, 0, 0);\n"
"	background: rgb(0, 0, 0);\n"
"	border: none;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical\n"
" {\n"
"	background-color: rgb(0, 0, 0);\n"
"	background: rgb(0, 0, 0);\n"
"	border: none;\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical\n"
" {\n"
"	background-color: rgb(0, 0, 0);\n"
"	background: rgb(0, 0, 0);\n"
"	border: none;\n"
" }\n"
" QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
" {\n"
"	background-color: rgb(0, 0, 0);\n"
"	background: rgb(0, 0, 0);\n"
"	border: none;\n"
" }\n"
" QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
" {\n"
"	background-color: rgb(0, 0, 0);\n"
"	background:"
                        " rgb(0, 0, 0);\n"
"	border: none;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
" {\n"
"	background-color: rgb(0, 0, 0);\n"
"	background: rgb(0, 0, 0);\n"
"	border: none;\n"
" }\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
" {\n"
"	background-color: rgb(0, 0, 0);\n"
"	background: rgb(0, 0, 0);\n"
"	border: none;\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 402, 200))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color:transparent;\n"
"background: transparent;\n"
"border: none;")
        self.label2_2 = QLabel(self.scrollAreaWidgetContents)
        self.label2_2.setObjectName(u"label2_2")
        self.label2_2.setEnabled(False)
        self.label2_2.setGeometry(QRect(30, 63, 301, 21))
        sizePolicy1.setHeightForWidth(self.label2_2.sizePolicy().hasHeightForWidth())
        self.label2_2.setSizePolicy(sizePolicy1)
        self.label2_2.setFont(font1)
        self.label2_2.setLayoutDirection(Qt.LeftToRight)
        self.label2_2.setAutoFillBackground(False)
        self.label2_2.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.label2_2.setInputMethodHints(Qt.ImhNone)
        self.label2_2.setAlignment(Qt.AlignCenter)
        self.label2_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.en_btn = QPushButton(self.scrollAreaWidgetContents)
        self.en_btn.setObjectName(u"en_btn")
        self.en_btn.setEnabled(True)
        self.en_btn.setGeometry(QRect(10, 60, 331, 36))
        sizePolicy1.setHeightForWidth(self.en_btn.sizePolicy().hasHeightForWidth())
        self.en_btn.setSizePolicy(sizePolicy1)
        self.en_btn.setFont(font1)
        self.en_btn.setMouseTracking(False)
        self.en_btn.setFocusPolicy(Qt.StrongFocus)
        self.en_btn.setLayoutDirection(Qt.LeftToRight)
        self.en_btn.setAutoFillBackground(False)
        self.en_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"QPushButton:focus\n"
"{\n"
"	border-image: url(:/buttons/res/lang_btn.png);\n"
"}")
        self.en_btn.setFlat(False)
        self.ru_btn = QPushButton(self.scrollAreaWidgetContents)
        self.ru_btn.setObjectName(u"ru_btn")
        self.ru_btn.setEnabled(True)
        self.ru_btn.setGeometry(QRect(10, 12, 331, 36))
        sizePolicy1.setHeightForWidth(self.ru_btn.sizePolicy().hasHeightForWidth())
        self.ru_btn.setSizePolicy(sizePolicy1)
        self.ru_btn.setFont(font1)
        self.ru_btn.setMouseTracking(False)
        self.ru_btn.setFocusPolicy(Qt.StrongFocus)
        self.ru_btn.setLayoutDirection(Qt.LeftToRight)
        self.ru_btn.setAutoFillBackground(False)
        self.ru_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"QPushButton:focus\n"
"{\n"
"	border-image: url(:/buttons/res/lang_btn.png);\n"
"}")
        self.ru_btn.setFlat(False)
        self.label1_2 = QLabel(self.scrollAreaWidgetContents)
        self.label1_2.setObjectName(u"label1_2")
        self.label1_2.setEnabled(False)
        self.label1_2.setGeometry(QRect(30, 15, 301, 21))
        sizePolicy1.setHeightForWidth(self.label1_2.sizePolicy().hasHeightForWidth())
        self.label1_2.setSizePolicy(sizePolicy1)
        self.label1_2.setFont(font1)
        self.label1_2.setLayoutDirection(Qt.LeftToRight)
        self.label1_2.setAutoFillBackground(False)
        self.label1_2.setStyleSheet(u"background: none;\n"
"color: #FFFFFF;\n"
"padding: 0;\n"
"border: none;\n"
"text-decoration: none;\n"
"text-align: center;\n"
"padding-top: 0px;\n"
"")
        self.label1_2.setInputMethodHints(Qt.ImhNone)
        self.label1_2.setAlignment(Qt.AlignCenter)
        self.label1_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.en_btn.raise_()
        self.label2_2.raise_()
        self.ru_btn.raise_()
        self.label1_2.raise_()
        self.labelback1 = QLabel(self.page_2)
        self.labelback1.setObjectName(u"labelback1")
        self.labelback1.setEnabled(False)
        self.labelback1.setGeometry(QRect(0, 0, 402, 34))
        sizePolicy1.setHeightForWidth(self.labelback1.sizePolicy().hasHeightForWidth())
        self.labelback1.setSizePolicy(sizePolicy1)
        self.labelback1.setFont(font1)
        self.labelback1.setLayoutDirection(Qt.LeftToRight)
        self.labelback1.setAutoFillBackground(False)
        self.labelback1.setStyleSheet(u"background-image: url(:/background/res/background.png);\n"
"border: none;\n"
"text-decoration: none;\n"
"")
        self.labelback1.setInputMethodHints(Qt.ImhNone)
        self.labelback1.setAlignment(Qt.AlignCenter)
        self.labelback1.setTextInteractionFlags(Qt.NoTextInteraction)
        self.labelback2 = QLabel(self.page_2)
        self.labelback2.setObjectName(u"labelback2")
        self.labelback2.setEnabled(False)
        self.labelback2.setGeometry(QRect(0, 180, 402, 61))
        sizePolicy1.setHeightForWidth(self.labelback2.sizePolicy().hasHeightForWidth())
        self.labelback2.setSizePolicy(sizePolicy1)
        self.labelback2.setFont(font1)
        self.labelback2.setLayoutDirection(Qt.LeftToRight)
        self.labelback2.setAutoFillBackground(False)
        self.labelback2.setStyleSheet(u"background-image: url(:/background/res/background.png);\n"
"border: none;\n"
"text-decoration: none;\n"
"")
        self.labelback2.setInputMethodHints(Qt.ImhNone)
        self.labelback2.setAlignment(Qt.AlignCenter)
        self.labelback2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.stackedWidget.addWidget(self.page_2)
        self.scrollArea.raise_()
        self.labelback1.raise_()
        self.label3_2.raise_()
        self.labelback2.raise_()
        self.doneButton.raise_()
        self.labelDone.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438...", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.pushButton1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton1.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton3.setText("")
        self.label2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438", None))
#if QT_CONFIG(tooltip)
        self.pushButton4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton4.setText("")
        self.label1.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c  \u0440\u0435\u0441\u0443\u0440\u0441\u043f\u0430\u043a", None))
#if QT_CONFIG(tooltip)
        self.pushButton2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton2.setText("")
#if QT_CONFIG(tooltip)
        self.langButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.langButton.setText("")
        self.VersionLabel.setText(QCoreApplication.translate("MainWindow", u"MCPP 0.0.2", None))
        self.CopytightLabel.setText(QCoreApplication.translate("MainWindow", u"Do not distribute!", None))
        self.labelDone.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
#if QT_CONFIG(tooltip)
        self.doneButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.doneButton.setText("")
        self.label3_2.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a...", None))
        self.label2_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
#if QT_CONFIG(tooltip)
        self.en_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.en_btn.setText("")
#if QT_CONFIG(tooltip)
        self.ru_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.ru_btn.setText("")
        self.label1_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.labelback1.setText("")
        self.labelback2.setText("")
        pass
    # retranslateUi

