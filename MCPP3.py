# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MCPP3(object):
    def setupUi(self, MCPP3):
        MCPP3.setObjectName("MCPP3")
        MCPP3.resize(491, 333)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/MCPP.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MCPP3.setWindowIcon(icon)
        MCPP3.setStyleSheet("background-image: url(:/background/bg32.png);")
        self.centralwidget = QtWidgets.QWidget(MCPP3)
        self.centralwidget.setObjectName("centralwidget")
        self.DoneB = QtWidgets.QPushButton(self.centralwidget)
        self.DoneB.setGeometry(QtCore.QRect(130, 260, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Minecraft Rus")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.DoneB.setFont(font)
        self.DoneB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DoneB.setAutoFillBackground(False)
        self.DoneB.setStyleSheet("QPushButton{\n"
"    height: 61px;\n"
"    width: 231px;\n"
"    text-decoration: none;\n"
"    text-align: center;\n"
"    color: white;\n"
"    background: url(:/buttons/btn.png) no-repeat;\n"
"    line-height: 26px;\n"
"    border: 2px solid black;\n"
"    padding-top: 6px;}\n"
"QPushButton:Hover{\n"
"   border: 2px solid white;}\n"
"QPushButton:Focus{\n"
"   outline: none;\n"
"   border: none;}\n"
"\n"
"")
        icon = QtGui.QIcon.fromTheme(",")
        self.DoneB.setIcon(icon)
        self.DoneB.setIconSize(QtCore.QSize(16, 16))
        self.DoneB.setDefault(False)
        self.DoneB.setFlat(True)
        self.DoneB.setObjectName("DoneB")
        self.SkyB = QtWidgets.QPushButton(self.centralwidget)
        self.SkyB.setGeometry(QtCore.QRect(10, 10, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Minecraft Rus")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.SkyB.setFont(font)
        self.SkyB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SkyB.setAutoFillBackground(False)
        self.SkyB.setStyleSheet("QPushButton{\n"
"    height: 61px;\n"
"    width: 231px;\n"
"    text-decoration: none;\n"
"    text-align: center;\n"
"    color: white;\n"
"    background: url(:/buttons/btn.png) no-repeat;\n"
"    line-height: 26px;\n"
"    border: 2px solid black;\n"
"    padding-top: 6px;}\n"
"QPushButton:Hover{\n"
"   border: 2px solid white;}\n"
"QPushButton:Focus{\n"
"   outline: none;\n"
"   border: none;}\n"
"\n"
"")
        icon = QtGui.QIcon.fromTheme(",")
        self.SkyB.setIcon(icon)
        self.SkyB.setIconSize(QtCore.QSize(16, 16))
        self.SkyB.setDefault(False)
        self.SkyB.setFlat(True)
        self.SkyB.setObjectName("SkyB")
        self.FontB = QtWidgets.QPushButton(self.centralwidget)
        self.FontB.setGeometry(QtCore.QRect(10, 80, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Minecraft Rus")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.FontB.setFont(font)
        self.FontB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.FontB.setAutoFillBackground(False)
        self.FontB.setStyleSheet("QPushButton{\n"
"    height: 61px;\n"
"    width: 231px;\n"
"    text-decoration: none;\n"
"    text-align: center;\n"
"    color: white;\n"
"    background: url(:/buttons/btn.png) no-repeat;\n"
"    line-height: 26px;\n"
"    border: 2px solid black;\n"
"    padding-top: 6px;}\n"
"QPushButton:Hover{\n"
"   border: 2px solid white;}\n"
"QPushButton:Focus{\n"
"   outline: none;\n"
"   border: none;}\n"
"\n"
"")
        icon = QtGui.QIcon.fromTheme(",")
        self.FontB.setIcon(icon)
        self.FontB.setIconSize(QtCore.QSize(16, 16))
        self.FontB.setDefault(False)
        self.FontB.setFlat(True)
        self.FontB.setObjectName("FontB")
        self.EntityB = QtWidgets.QPushButton(self.centralwidget)
        self.EntityB.setGeometry(QtCore.QRect(10, 150, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Minecraft Rus")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.EntityB.setFont(font)
        self.EntityB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.EntityB.setAutoFillBackground(False)
        self.EntityB.setStyleSheet("QPushButton{\n"
"    height: 61px;\n"
"    width: 231px;\n"
"    text-decoration: none;\n"
"    text-align: center;\n"
"    color: white;\n"
"    background: url(:/buttons/btn.png) no-repeat;\n"
"    line-height: 26px;\n"
"    border: 2px solid black;\n"
"    padding-top: 6px;}\n"
"QPushButton:Hover{\n"
"   border: 2px solid white;}\n"
"QPushButton:Focus{\n"
"   outline: none;\n"
"   border: none;}\n"
"\n"
"")
        icon = QtGui.QIcon.fromTheme(",")
        self.EntityB.setIcon(icon)
        self.EntityB.setIconSize(QtCore.QSize(16, 16))
        self.EntityB.setDefault(False)
        self.EntityB.setFlat(True)
        self.EntityB.setObjectName("EntityB")
        self.TexturesB = QtWidgets.QPushButton(self.centralwidget)
        self.TexturesB.setGeometry(QtCore.QRect(250, 10, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Minecraft Rus")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.TexturesB.setFont(font)
        self.TexturesB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TexturesB.setAutoFillBackground(False)
        self.TexturesB.setStyleSheet("QPushButton{\n"
"    height: 61px;\n"
"    width: 231px;\n"
"    text-decoration: none;\n"
"    text-align: center;\n"
"    color: white;\n"
"    background: url(:/buttons/btn.png) no-repeat;\n"
"    line-height: 26px;\n"
"    border: 2px solid black;\n"
"    padding-top: 6px;}\n"
"QPushButton:Hover{\n"
"   border: 2px solid white;}\n"
"QPushButton:Focus{\n"
"   outline: none;\n"
"   border: none;}\n"
"\n"
"")
        icon = QtGui.QIcon.fromTheme(",")
        self.TexturesB.setIcon(icon)
        self.TexturesB.setIconSize(QtCore.QSize(16, 16))
        self.TexturesB.setDefault(False)
        self.TexturesB.setFlat(True)
        self.TexturesB.setObjectName("TexturesB")
        self.OncloseB = QtWidgets.QPushButton(self.centralwidget)
        self.OncloseB.setGeometry(QtCore.QRect(250, 80, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Minecraft Rus")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.OncloseB.setFont(font)
        self.OncloseB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OncloseB.setAutoFillBackground(False)
        self.OncloseB.setStyleSheet("QPushButton{\n"
"    height: 61px;\n"
"    width: 231px;\n"
"    text-decoration: none;\n"
"    text-align: center;\n"
"    color: white;\n"
"    background: url(:/buttons/btn.png) no-repeat;\n"
"    line-height: 26px;\n"
"    border: 2px solid black;\n"
"    padding-top: 6px;}\n"
"QPushButton:Hover{\n"
"   border: 2px solid white;}\n"
"QPushButton:Focus{\n"
"   outline: none;\n"
"   border: none;}\n"
"\n"
"")
        icon = QtGui.QIcon.fromTheme(",")
        self.OncloseB.setIcon(icon)
        self.OncloseB.setIconSize(QtCore.QSize(16, 16))
        self.OncloseB.setDefault(False)
        self.OncloseB.setFlat(True)
        self.OncloseB.setObjectName("OncloseB")
        self.SupportB = QtWidgets.QPushButton(self.centralwidget)
        self.SupportB.setGeometry(QtCore.QRect(250, 150, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Minecraft Rus")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.SupportB.setFont(font)
        self.SupportB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SupportB.setAutoFillBackground(False)
        self.SupportB.setStyleSheet("QPushButton{\n"
"    height: 61px;\n"
"    width: 231px;\n"
"    text-decoration: none;\n"
"    text-align: center;\n"
"    color: white;\n"
"    background: url(:/buttons/btn.png) no-repeat;\n"
"    line-height: 26px;\n"
"    border: 2px solid black;\n"
"    padding-top: 6px;}\n"
"QPushButton:Hover{\n"
"   border: 2px solid white;}\n"
"QPushButton:Focus{\n"
"   outline: none;\n"
"   border: none;}\n"
"\n"
"")
        icon = QtGui.QIcon.fromTheme(",")
        self.SupportB.setIcon(icon)
        self.SupportB.setIconSize(QtCore.QSize(16, 16))
        self.SupportB.setDefault(False)
        self.SupportB.setFlat(True)
        self.SupportB.setObjectName("SupportB")
        MCPP3.setCentralWidget(self.centralwidget)

        self.retranslateUi(MCPP3)
        QtCore.QMetaObject.connectSlotsByName(MCPP3)

    def retranslateUi(self, MCPP3):
        _translate = QtCore.QCoreApplication.translate
        MCPP3.setWindowTitle(_translate("MCPP3", "MCPP"))
        self.DoneB.setText(_translate("MCPP3", "Done"))
        self.SkyB.setText(_translate("MCPP3", "Sky"))
        self.FontB.setText(_translate("MCPP3", "Fonts"))
        self.EntityB.setText(_translate("MCPP3", "Entity"))
        self.TexturesB.setText(_translate("MCPP3", "Textures"))
        self.OncloseB.setText(_translate("MCPP3", "On close"))
        self.SupportB.setText(_translate("MCPP3", "Support creator"))
import minecraft_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MCPP3 = QtWidgets.QMainWindow()
    ui = Ui_MCPP3()
    ui.setupUi(MCPP3)
    MCPP3.show()
    sys.exit(app.exec_())
