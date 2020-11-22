from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtMultimedia import QSound
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import MCPP
import sys
import time

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

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


class MainScreen(QtWidgets.QMainWindow, MCPP.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле MCPP.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #message = self.tr('Apple')
        #print(message)
        
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
        
        self.pushButton1.clicked.connect(self.test)  # Выполнить функцию test при нажатии
        self.threadpool = QThreadPool() # Это нужно для создания потока
        print("Доступно потоков %d " % self.threadpool.maxThreadCount()) # Доступное количество потоков
        self.label1.setText(QApplication.translate('app', 'Открыть ресурспак'))
    
    def thread_test(self):
        print('Работает!')
        #self.pushButton1.setEnabled(False)
    
    
    def test(self):
        worker = Worker(self.thread_test) # Запуск функции потоком
        self.threadpool.start(worker)
    
    # Проигрывание щелчка при нажатии
    def Play(self):
        QSound.play(":/sounds/res/click.wav")

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    
    translator = QtCore.QTranslator(app)
    translator.load(':/lang/test')
    app.installTranslator(translator)
    if not app.installTranslator(translator):
        print("Can not install translation!")
    
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