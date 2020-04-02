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

import ShapeRecognition as sr
import cv2
import numpy as np
import os.path

class appMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(appMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sceneCamera = QtWidgets.QGraphicsScene()
        self.sceneMask = QtWidgets.QGraphicsScene()
        self.show()
        self.fileNameCameraImage = ""
        self.ui.btn_CamImageImport.clicked.connect(self.onClick_CamImageImport)
        self.ui.btn_Calibrate.clicked.connect(self.onClick_Calibrate)
        self.ui.btn_SaveCalibration.clicked.connect(self.onClick_SaveCalibration)
        self.ui.cbox_LockCalibration.clicked.connect(self.onClick_LockCalibration)
        self.showImageInView("./TestImages/Vialux_DMD.png", self.ui.view_CameraImage)
        self.showImageInView("./TestImages/UoL_logo.jpeg", self.ui.view_DMDMaskImage)
        self.CalibrationValuesFile = 'CalibrationValues.txt'
        self.CalibrationImageFile = 'CalibrationImageFile.txt'
        if os.path.isfile(self.CalibrationValuesFile) and os.path.isfile(self.CalibrationImageFile):
            self.calibrationValuesStorage = np.loadtxt(self.CalibrationValuesFile, dtype=float)
            self.ui.txt_DMDSizeX.setPlainText(str(self.calibrationValuesStorage[0]))
            self.ui.txt_DMDSizeY.setPlainText(str(self.calibrationValuesStorage[1]))
            self.ui.txt_DMDCalibrationImageRatio.setPlainText(str(self.calibrationValuesStorage[2]))
            if self.calibrationValuesStorage[3] == 1:
                self.ui.radioButton_BlackMask.setChecked(True)
            else:
                self.ui.radioButton_WhiteMask.setChecked(True)
            self.ui.txt_CentreAdjustX.setPlainText(str(self.calibrationValuesStorage[4]))
            self.ui.txt_CentreAdjustY.setPlainText(str(self.calibrationValuesStorage[5]))
            self.ui.txt_RotationAdjust.setPlainText(str(self.calibrationValuesStorage[6]))
            self.ui.txt_WidthAdjust.setPlainText(str(self.calibrationValuesStorage[7]))
            self.ui.txt_HeightAdjust.setPlainText(str(self.calibrationValuesStorage[8]))
            imageFile = open(self.CalibrationImageFile,'r')
            self.fileNameCameraImage = imageFile.read()
            self.calibrationImageStorage = self.fileNameCameraImage
            imageFile.close()
            self.onClick_Calibrate()
            

    def showImageInView(self, image, view):
        if isinstance(image, str):
            imagePixMap = QtGui.QPixmap(image).scaled(300,300, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        else:
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            imagePixMap = QtGui.QImage(image, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).scaled(300,300, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        view.setPixmap(QtGui.QPixmap(imagePixMap))
        view.repaint()
    
    def generateBox(self, calibration):
        # Initialise local input values
        centreX = calibration.positionX
        centreY = calibration.positionY
        theta = calibration.rotation
        phi = 90 - theta
        thetaRad = theta * np.pi / 180
        phiRad = phi * np.pi / 180
        semiW = calibration.width / 2
        semiH = calibration.height / 2
        # A is point to the right of centre half way up the right side of the rectangle
        Ax = int(round(centreX + semiW * np.cos(thetaRad)))
        Ay = int(round(centreY + semiW * np.sin(thetaRad)))
        # B is the bottom right corner of the rectangle
        Bx = int(round(Ax + semiH * np.sin(thetaRad)))
        By = int(round(Ay - semiH * np.cos(thetaRad)))
        # C is the top right corner of the rectangle
        Cx = int(round(Ax - semiH * np.cos(phiRad)))
        Cy = int(round(Ay + semiH * np.sin(phiRad)))
        # D is point to the left of centre half way up the left side of the rectangle
        Dx = int(round(centreX - semiW * np.cos(thetaRad)))
        Dy = int(round(centreY - semiW * np.sin(thetaRad)))
        # E is the bottom left corner of the rectangle
        Ex = int(round(Dx + semiH * np.cos(phiRad)))
        Ey = int(round(Dy - semiH * np.sin(phiRad)))
        # F is the top left corner of the rectangle
        Fx = int(round(Dx - semiH * np.sin(thetaRad)))
        Fy = int(round(Dy + semiH * np.cos(thetaRad)))
        box = np.array([[Fx, Fy], [Ex, Ey], [Bx, By], [Cx, Cy]])
        return box

    @pyqtSlot()
    def onClick_CamImageImport(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileNameCameraImage, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;tiff (*.tiff);;tif (*.tif);;png (*.png)", options=options)
        if self.fileNameCameraImage:
            self.showImageInView(self.fileNameCameraImage, self.ui.view_CameraImage)

    @pyqtSlot()
    def onClick_Calibrate(self):
        if not self.fileNameCameraImage:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Calibration image must be loaded before calibration can be performed.')
            error_dialog.exec_()
            return
        if not(self.ui.txt_DMDSizeX.toPlainText().replace(".", "", 1).isdigit()) or not(self.ui.txt_DMDSizeY.toPlainText().replace(".", "", 1).isdigit()) or not(self.ui.txt_DMDCalibrationImageRatio.toPlainText().replace(".", "", 1).isdigit()):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('DMD calibration ratio and DMD X & Y size must be numeric.')
            error_dialog.exec_()
            return
        self.calibration = sr.ShapeDetector(self.fileNameCameraImage, self.ui.radioButton_BlackMask.isChecked())
        self.calibration.detectCalibration()
        self.calibration.positionX = self.calibration.positionX + float(self.ui.txt_CentreAdjustX.toPlainText())
        self.calibration.positionY = self.calibration.positionY + float(self.ui.txt_CentreAdjustY.toPlainText())
        self.calibration.rotation = self.calibration.rotation + float(self.ui.txt_RotationAdjust.toPlainText())
        self.calibration.width = self.calibration.width * float(self.ui.txt_WidthAdjust.toPlainText())
        self.calibration.height = self.calibration.height * float(self.ui.txt_HeightAdjust.toPlainText())
        box = self.generateBox(self.calibration)
        cv2.drawContours(self.calibration.colourImage, [box], 0, (0, 255, 0), 3)
        cv2.circle(self.calibration.colourImage,(round(self.calibration.positionX),round(self.calibration.positionY)), 10, (0,0,255), -1)
        self.showImageInView(self.calibration.colourImage, self.ui.view_CameraImage)
        if self.ui.radioButton_BlackMask.isChecked():
            checkState = 1
        else:
            checkState = 0
        self.calibrationValuesStorage = np.array([
            float(self.ui.txt_DMDSizeX.toPlainText()),
            float(self.ui.txt_DMDSizeY.toPlainText()), 
            float(self.ui.txt_DMDCalibrationImageRatio.toPlainText()), 
            float(checkState), 
            float(self.ui.txt_CentreAdjustX.toPlainText()), 
            float(self.ui.txt_CentreAdjustY.toPlainText()),
            float(self.ui.txt_RotationAdjust.toPlainText()),
            float(self.ui.txt_WidthAdjust.toPlainText()),
            float(self.ui.txt_HeightAdjust.toPlainText()),
            float(self.calibration.positionX),
            float(self.calibration.positionY),
            float(self.calibration.rotation),
            float(self.calibration.width),
            float(self.calibration.height)
            ], dtype=float)
        self.calibrationImageStorage = self.fileNameCameraImage

    @pyqtSlot()
    def onClick_SaveCalibration(self):
        np.savetxt(self.CalibrationValuesFile, self.calibrationValuesStorage, fmt='%1.2f')
        imageFile = open(self.CalibrationImageFile, 'w+')
        imageFile.write(self.calibrationImageStorage)
        imageFile.close()

    @pyqtSlot()
    def onClick_LockCalibration(self):
        if self.ui.cbox_LockCalibration.isChecked():
            self.ui.txt_DMDSizeX.setEnabled(False)
            self.ui.txt_DMDSizeY.setEnabled(False)
            self.ui.txt_DMDCalibrationImageRatio.setEnabled(False)
            self.ui.txt_CentreAdjustX.setEnabled(False)
            self.ui.txt_CentreAdjustY.setEnabled(False)
            self.ui.radioButton_BlackMask.setEnabled(False)
            self.ui.radioButton_WhiteMask.setEnabled(False)
            self.ui.txt_RotationAdjust.setEnabled(False)
            self.ui.txt_WidthAdjust.setEnabled(False)
            self.ui.txt_HeightAdjust.setEnabled(False)
            self.ui.btn_SaveCalibration.setEnabled(False)
            self.ui.btn_Calibrate.setEnabled(False)
        elif not(self.ui.cbox_LockCalibration.isChecked()):
            self.ui.txt_DMDSizeX.setEnabled(True)
            self.ui.txt_DMDSizeY.setEnabled(True)
            self.ui.txt_DMDCalibrationImageRatio.setEnabled(True)
            self.ui.txt_CentreAdjustX.setEnabled(True)
            self.ui.txt_CentreAdjustY.setEnabled(True)
            self.ui.radioButton_BlackMask.setEnabled(True)
            self.ui.radioButton_WhiteMask.setEnabled(True)
            self.ui.txt_RotationAdjust.setEnabled(True)
            self.ui.txt_WidthAdjust.setEnabled(True)
            self.ui.txt_HeightAdjust.setEnabled(True)
            self.ui.btn_SaveCalibration.setEnabled(True)
            self.ui.btn_Calibrate.setEnabled(True)
        else:
            self.ui.txt_DMDSizeX.setEnabled(True)
            self.ui.txt_DMDSizeY.setEnabled(True)
            self.ui.txt_DMDCalibrationImageRatio.setEnabled(True)
            self.ui.txt_CentreAdjustX.setEnabled(True)
            self.ui.txt_CentreAdjustY.setEnabled(True)
            self.ui.radioButton_BlackMask.setEnabled(True)
            self.ui.radioButton_WhiteMask.setEnabled(True)
            self.ui.txt_RotationAdjust.setEnabled(True)
            self.ui.txt_WidthAdjust.setEnabled(True)
            self.ui.txt_HeightAdjust.setEnabled(True)
            self.ui.btn_SaveCalibration.setEnabled(True)
            self.ui.btn_Calibrate.setEnabled(True)
        self.repaint()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = appMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
