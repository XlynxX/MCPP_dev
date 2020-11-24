from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtMultimedia import QSound
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from locale import getdefaultlocale
import MCPP
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

# Главное окно
class MainScreen(QtWidgets.QMainWindow, MCPP.Ui_MainWindow):
    def __init__(self, parent = None):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле MCPP.py
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.stackedWidget.setCurrentIndex(0) # Это для того, чтобы сначала появлялось всегда главное окно
        
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
        self.ru_btn.clicked.connect(lambda: self.retranslate('ru_RU'))
        self.en_btn.clicked.connect(lambda: self.retranslate('en_US'))
        self.doneButton.clicked.connect(self.close_lang_settings)
        self.threadpool = QThreadPool() # Это нужно для создания потока
        print("Доступно потоков: %d " % self.threadpool.maxThreadCount()) # Доступное количество потоков
        # Привязка кнопок к функциям

        self.label1.setText(QApplication.translate('app', 'Открыть  ресурспак'))
        self.label2.setText(QApplication.translate('app', 'Модификации'))
        self.label3.setText(QApplication.translate('app', 'Настройки...'))
        self.label4.setText(QApplication.translate('app', 'Конвертировать'))

    # Встраивание текста с переводом
    def retranslate(self, lang):
            translator = QtCore.QTranslator(self)
            print(lang)
            if lang == 'en_US':
                translator.load(':/lang/lang/en_US')
            else:
                translator.load(':/lang/lang/ru_RU')
            QApplication.installTranslator(translator)
            
            # Окно настроек
            self.label3_2.setText(QApplication.translate('app', 'Языки'))
            self.label1_2.setText(QApplication.translate('app', 'Русский'))
            self.label2_2.setText(QApplication.translate('app', 'Английский'))
            self.labelDone.setText(QApplication.translate('app', 'Готово'))
            # Главное окно
            self.label1.setText(QApplication.translate('app', 'Открыть  ресурспак'))
            self.label2.setText(QApplication.translate('app', 'Модификации'))
            self.label3.setText(QApplication.translate('app', 'Настройки...'))
            self.label4.setText(QApplication.translate('app', 'Конвертировать'))
            if not QApplication.installTranslator(translator):
                print("Can not install translation!")
    # Встраивание текста с переводом
    
    def thread_test(self):
        print('Работает!')

    def open_lang_settings(self):
        self.stackedWidget.setCurrentIndex(1)
    # Закрытие окна настроек и открытие основного окна
    def close_lang_settings(self):
        self.stackedWidget.setCurrentIndex(0)
    # Закрытие окна настроек и открытие основного окна
    
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
    locale = getdefaultlocale()
    translator = QtCore.QTranslator(app)
    if locale[0] == 'ru_RU':
        translator.load(':/lang/lang/ru_RU')
    else:
        translator.load(':/lang/lang/en_US')
    app.installTranslator(translator)
    if not app.installTranslator(translator):
        print("Can not install translation!")
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