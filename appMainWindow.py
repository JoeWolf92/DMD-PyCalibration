# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

from UI_appMainWindow import Ui_MainWindow

class appMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(appMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sceneCamera = QtWidgets.QGraphicsScene()
        self.sceneMask = QtWidgets.QGraphicsScene()
        self.show()
        self.ui.btn_CamImageImport.clicked.connect(self.onClick_CamImageImport)

    @pyqtSlot()
    def onClick_CamImageImport(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileNameCameraImage, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;tiff (*.tiff);;tif (*.tif);;png (*.png)", options=options)
        if self.fileNameCameraImage:
            print(self.fileNameCameraImage)
            # self.showImageInFrame(self.fileNameCameraImage, self.ui.view_CameraImage)
            self.cameraImagePixMap = QtGui.QPixmap(self.fileNameCameraImage)
            # self.cameraImagePixMap.scaled(250,250,aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.cameraImagePixMap = self.cameraImagePixMap.scaled(300,300, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.ui.view_CameraImage.setPixmap(QtGui.QPixmap(self.cameraImagePixMap))
            # self.sceneCamera.addItem(QtWidgets.QGraphicsPixmapItem(self.cameraImagePixMap))
            # self.ui.view_CameraImage.setScene(self.sceneCamera)
            # self.ui.view_CameraImage.show()

    def showImageInFrame(self, image_path, label_image):
        # frame = QtGui.QWidget()
        # label_image = QtGui.QLabel(self.ui.view_CameraImage)
        image_profile = QtGui.QImage(image_path)
        image_profile = image_profile.scaled(250,250, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        label_image.setPixmap(QtGui.QPixmap.fromImage(image_profile))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = appMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
