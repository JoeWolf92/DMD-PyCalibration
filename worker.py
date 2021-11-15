from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time


class Worker(QObject):
    finished = pyqtSignal()
    statusCheckDMDTimer = pyqtSignal()


    @pyqtSlot()
    def procCounter(self): # A slot takes no params
        while True:
            time.sleep(30)
            self.statusCheckDMDTimer.emit()

        self.finished.emit()