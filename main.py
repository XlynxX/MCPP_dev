from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtMultimedia import QSound
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from locale import getdefaultlocale
import MCPP, MCPP2
import sys
import time

# THREAD
class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)
# THREAD


# Окно настроек
class SettingsScreen(QtWidgets.QMainWindow, MCPP2.Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            # Повторяющиеся для QLabel функции
            for child in self.findChildren(QLabel):
                # Тени
                self.shadow = QGraphicsDropShadowEffect(self)
                self.shadow.setXOffset(2)
                self.shadow.setYOffset(2)
                self.shadow.setColor(QColor(63, 63, 63, 255))
                self.shadow.setBlurRadius(0)
                child.setGraphicsEffect(self.shadow)
                # Атрибут игнорирования QLabel мышкой
                child.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
            
            # Повторяющиеся для QPushButton функции
            for child in self.findChildren(QPushButton):
                # Вызов функции проигрывания звука при нажатии
                child.clicked.connect(MainScreen.Play)

            # Привязка кнопок к функциям
            self.pushButton1.clicked.connect(self.retranslate)
            self.pushButton2.clicked.connect(self.retranslate)
            self.doneButton.clicked.connect(self.close_lang_settings)
            # Привязка кнопок к функциям

            self.label1.setText(QApplication.translate('app', 'Языки'))
            self.label2.setText(QApplication.translate('app', 'Русский'))
            self.label3.setText(QApplication.translate('app', 'Английский'))
            self.labelDone.setText(QApplication.translate('app', 'Готово'))

        # Закрытие окна настроек и открытие основного окна
        def close_lang_settings(self):
            self.close()
            self.window = MainScreen()
            self.window.show()
        # Закрытие окна настроек и открытие основного окна


        # Встраивание текста с переводом
        def retranslate(self):
            translator = QtCore.QTranslator(self)
            #print(lang)
            #if word == 'en_US':
                #translator.load(':/lang/lang/en_US')
            #else:
                #translator.load(':/lang/lang/ru_RU')
            translator.load(':/lang/lang/en_US')
            QApplication.installTranslator(translator)
            
            self.label1.setText(QApplication.translate('app', 'Языки'))
            self.label2.setText(QApplication.translate('app', 'Русский'))
            self.label3.setText(QApplication.translate('app', 'Английский'))
            self.labelDone.setText(QApplication.translate('app', 'Готово'))
            if not QApplication.installTranslator(translator):
                print("Can not install translation!")

            #MainScreen.retranslate
        # Встраивание текста с переводом

    

#Главное окно
class MainScreen(QtWidgets.QMainWindow, MCPP.Ui_MainWindow):
    def __init__(self, parent = None):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле MCPP.py
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        # Повторяющиеся для QLabel функции
        for child in self.findChildren(QLabel):
            # Тени
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setXOffset(2)
            self.shadow.setYOffset(2)
            self.shadow.setColor(QColor(63, 63, 63, 255))
            self.shadow.setBlurRadius(0)
            child.setGraphicsEffect(self.shadow)
            # Атрибут игнорирования QLabel мышкой
            child.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
            
        # Повторяющиеся для QPushButton функции
        for child in self.findChildren(QPushButton):
            # Вызов функции проигрывания звука при нажатии
            child.clicked.connect(self.Play)


        # Привязка кнопок к функциям
        self.langButton.clicked.connect(self.open_lang_settings)  # Выполнить функцию test при нажатии
        self.pushButton1.clicked.connect(self.test)
        self.threadpool = QThreadPool() # Это нужно для создания потока
        print("Доступно потоков: %d " % self.threadpool.maxThreadCount()) # Доступное количество потоков
        # Привязка кнопок к функциям

        self.label1.setText(QApplication.translate('app', 'Открыть  ресурспак'))
        self.label2.setText(QApplication.translate('app', 'Модификации'))
        self.label3.setText(QApplication.translate('app', 'Настройки...'))
        self.label4.setText(QApplication.translate('app', 'Конвертировать'))

    # Встраивание текста с переводом
    #def retranslate(self):
        #translator = QtCore.QTranslator(self)
        #translator.load(':/lang/lang/en_US')
        #QApplication.installTranslator(translator)

        #self.label1.setText(QApplication.translate('app', 'Открыть  ресурспак'))
        #self.label2.setText(QApplication.translate('app', 'Модификации'))
        #self.label3.setText(QApplication.translate('app', 'Настройки...'))
        #self.label4.setText(QApplication.translate('app', 'Конвертировать'))
        #if not QApplication.installTranslator(translator):
            #print("Can not install translation!")
    # Встраивание текста с переводом
    
    def thread_test(self):
        print('Работает!')

    def open_lang_settings(self):
        #self.hide()
        self.settings = SettingsScreen()
        self.settings.show()
    
    
    def test(self):
        worker = Worker(self.thread_test) # Запуск функции потоком
        self.threadpool.start(worker)
    
    # Проигрывание звука при нажатии
    def Play(self):
        QSound.play(":/sounds/res/click.wav")
    # Проигрывание звука при нажатии

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    
    # Загрузка перевода
    #locale = getdefaultlocale()
    #translator = QtCore.QTranslator(app)
    #translator.load(':/lang/lang/%s' % locale[0])
    #app.installTranslator(translator)
    #if not app.installTranslator(translator):
        #print("Can not install translation!")
    # Загрузка перевода
    
    window = MainScreen()  # Создаём объект класса MainScreen

    # Загружаем кастомные шрифты
    MCPP = QtWidgets.QMainWindow()
    MCPP.addfont = QtGui.QFontDatabase()
    MCPP.addfont.addApplicationFont(":/fonts/res/Minecraft.ttf")
    MCPP.setFont(QtGui.QFont("Minecraft Rus", 12))
    # Загружаем кастомные шрифты

    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()