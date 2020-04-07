# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 722)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolTipDuration(2)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_MaskFunctionality = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_MaskFunctionality.setGeometry(QtCore.QRect(530, 330, 391, 311))
        self.tab_MaskFunctionality.setObjectName("tab_MaskFunctionality")
        self.tab_Calibration = QtWidgets.QWidget()
        self.tab_Calibration.setObjectName("tab_Calibration")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_Calibration)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(70, 10, 243, 101))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txt_DMDCalibrationMaskRatio = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
        self.txt_DMDCalibrationMaskRatio.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_DMDCalibrationMaskRatio.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_DMDCalibrationMaskRatio.setTabChangesFocus(True)
        self.txt_DMDCalibrationMaskRatio.setObjectName("txt_DMDCalibrationMaskRatio")
        self.gridLayout_3.addWidget(self.txt_DMDCalibrationMaskRatio, 0, 0, 1, 1)
        self.txt_CentreCircleSize = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
        self.txt_CentreCircleSize.setMinimumSize(QtCore.QSize(0, 25))
        self.txt_CentreCircleSize.setMaximumSize(QtCore.QSize(16777215, 25))
        self.txt_CentreCircleSize.setTabChangesFocus(True)
        self.txt_CentreCircleSize.setObjectName("txt_CentreCircleSize")
        self.gridLayout_3.addWidget(self.txt_CentreCircleSize, 1, 0, 1, 1)
        self.label_CalibrationCentreCircle = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_CalibrationCentreCircle.setObjectName("label_CalibrationCentreCircle")
        self.gridLayout_3.addWidget(self.label_CalibrationCentreCircle, 1, 1, 1, 1)
        self.label_DMDCalibrationMaskRatio = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_DMDCalibrationMaskRatio.setObjectName("label_DMDCalibrationMaskRatio")
        self.gridLayout_3.addWidget(self.label_DMDCalibrationMaskRatio, 0, 1, 1, 1)
        self.tab_MaskFunctionality.addTab(self.tab_Calibration, "")
        self.tab_Threshold = QtWidgets.QWidget()
        self.tab_Threshold.setObjectName("tab_Threshold")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_Threshold)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 10, 391, 261))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.txt_maskAdjustUD = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.txt_maskAdjustUD.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_maskAdjustUD.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_maskAdjustUD.setTabChangesFocus(True)
        self.txt_maskAdjustUD.setObjectName("txt_maskAdjustUD")
        self.gridLayout_4.addWidget(self.txt_maskAdjustUD, 3, 2, 1, 1)
        self.btn_MaskToAdd = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.btn_MaskToAdd.setObjectName("btn_MaskToAdd")
        self.gridLayout_4.addWidget(self.btn_MaskToAdd, 2, 2, 1, 2)
        self.btn_getThresholdValues = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.btn_getThresholdValues.setObjectName("btn_getThresholdValues")
        self.gridLayout_4.addWidget(self.btn_getThresholdValues, 0, 0, 1, 2)
        self.label_maskAdjustLR = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_maskAdjustLR.setObjectName("label_maskAdjustLR")
        self.gridLayout_4.addWidget(self.label_maskAdjustLR, 3, 1, 1, 1)
        self.txt_maskAdjustLR = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.txt_maskAdjustLR.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_maskAdjustLR.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_maskAdjustLR.setTabChangesFocus(True)
        self.txt_maskAdjustLR.setObjectName("txt_maskAdjustLR")
        self.gridLayout_4.addWidget(self.txt_maskAdjustLR, 3, 0, 1, 1)
        self.label_maskAdjustUD = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_maskAdjustUD.setObjectName("label_maskAdjustUD")
        self.gridLayout_4.addWidget(self.label_maskAdjustUD, 3, 3, 1, 1)
        self.label_highValueThreshold = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_highValueThreshold.setObjectName("label_highValueThreshold")
        self.gridLayout_4.addWidget(self.label_highValueThreshold, 1, 2, 1, 1)
        self.slider_thresholdValue = QtWidgets.QSlider(self.gridLayoutWidget_4)
        self.slider_thresholdValue.setOrientation(QtCore.Qt.Horizontal)
        self.slider_thresholdValue.setObjectName("slider_thresholdValue")
        self.gridLayout_4.addWidget(self.slider_thresholdValue, 1, 1, 1, 1)
        self.label_ThresholdLevel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_ThresholdLevel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ThresholdLevel.setWordWrap(True)
        self.label_ThresholdLevel.setObjectName("label_ThresholdLevel")
        self.gridLayout_4.addWidget(self.label_ThresholdLevel, 0, 2, 1, 2)
        self.txt_MaskToAdd = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.txt_MaskToAdd.setMinimumSize(QtCore.QSize(170, 75))
        self.txt_MaskToAdd.setMaximumSize(QtCore.QSize(170, 75))
        self.txt_MaskToAdd.setTabChangesFocus(True)
        self.txt_MaskToAdd.setReadOnly(False)
        self.txt_MaskToAdd.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.txt_MaskToAdd.setObjectName("txt_MaskToAdd")
        self.gridLayout_4.addWidget(self.txt_MaskToAdd, 2, 0, 1, 2)
        self.txt_currentThreshold = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.txt_currentThreshold.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_currentThreshold.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_currentThreshold.setTabChangesFocus(True)
        self.txt_currentThreshold.setObjectName("txt_currentThreshold")
        self.gridLayout_4.addWidget(self.txt_currentThreshold, 1, 3, 1, 1)
        self.label_maskAdjustRot = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_maskAdjustRot.setObjectName("label_maskAdjustRot")
        self.gridLayout_4.addWidget(self.label_maskAdjustRot, 4, 1, 1, 1)
        self.txt_maskAdjustRot = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.txt_maskAdjustRot.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_maskAdjustRot.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_maskAdjustRot.setTabChangesFocus(True)
        self.txt_maskAdjustRot.setObjectName("txt_maskAdjustRot")
        self.gridLayout_4.addWidget(self.txt_maskAdjustRot, 4, 0, 1, 1)
        self.label_lowValueThreshold = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_lowValueThreshold.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_lowValueThreshold.setObjectName("label_lowValueThreshold")
        self.gridLayout_4.addWidget(self.label_lowValueThreshold, 1, 0, 1, 1)
        self.cBox_FlipLR = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.cBox_FlipLR.setObjectName("cBox_FlipLR")
        self.gridLayout_4.addWidget(self.cBox_FlipLR, 4, 2, 1, 1)
        self.cBox_FlipUD = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.cBox_FlipUD.setObjectName("cBox_FlipUD")
        self.gridLayout_4.addWidget(self.cBox_FlipUD, 4, 3, 1, 1)
        self.tab_MaskFunctionality.addTab(self.tab_Threshold, "")
        self.tab_Slit = QtWidgets.QWidget()
        self.tab_Slit.setObjectName("tab_Slit")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_Slit)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(80, 0, 223, 171))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.txt_SlitWidth = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.txt_SlitWidth.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_SlitWidth.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_SlitWidth.setTabChangesFocus(True)
        self.txt_SlitWidth.setObjectName("txt_SlitWidth")
        self.gridLayout_5.addWidget(self.txt_SlitWidth, 1, 0, 1, 1)
        self.label_NumberOfSlits = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_NumberOfSlits.setObjectName("label_NumberOfSlits")
        self.gridLayout_5.addWidget(self.label_NumberOfSlits, 0, 1, 1, 1)
        self.spinBox_NumberOfSlits = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_NumberOfSlits.setMinimumSize(QtCore.QSize(90, 25))
        self.spinBox_NumberOfSlits.setMaximumSize(QtCore.QSize(90, 25))
        self.spinBox_NumberOfSlits.setMinimum(1)
        self.spinBox_NumberOfSlits.setMaximum(4)
        self.spinBox_NumberOfSlits.setObjectName("spinBox_NumberOfSlits")
        self.gridLayout_5.addWidget(self.spinBox_NumberOfSlits, 0, 0, 1, 1)
        self.txt_SlitSeparation = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.txt_SlitSeparation.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_SlitSeparation.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_SlitSeparation.setTabChangesFocus(True)
        self.txt_SlitSeparation.setObjectName("txt_SlitSeparation")
        self.gridLayout_5.addWidget(self.txt_SlitSeparation, 2, 0, 1, 1)
        self.label_SlitSeparation = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_SlitSeparation.setObjectName("label_SlitSeparation")
        self.gridLayout_5.addWidget(self.label_SlitSeparation, 2, 1, 1, 1)
        self.label_SlitWidth = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_SlitWidth.setObjectName("label_SlitWidth")
        self.gridLayout_5.addWidget(self.label_SlitWidth, 1, 1, 1, 1)
        self.txt_SlitRotation = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.txt_SlitRotation.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_SlitRotation.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_SlitRotation.setTabChangesFocus(True)
        self.txt_SlitRotation.setObjectName("txt_SlitRotation")
        self.gridLayout_5.addWidget(self.txt_SlitRotation, 3, 0, 1, 1)
        self.label_SlitRotation = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_SlitRotation.setObjectName("label_SlitRotation")
        self.gridLayout_5.addWidget(self.label_SlitRotation, 3, 1, 1, 1)
        self.tab_MaskFunctionality.addTab(self.tab_Slit, "")
        self.tab_Pinhole = QtWidgets.QWidget()
        self.tab_Pinhole.setObjectName("tab_Pinhole")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.tab_Pinhole)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(80, 0, 238, 171))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_PinholeRadius = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_PinholeRadius.setObjectName("label_PinholeRadius")
        self.gridLayout_6.addWidget(self.label_PinholeRadius, 1, 1, 1, 1)
        self.label_NumberOfPinholes = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_NumberOfPinholes.setObjectName("label_NumberOfPinholes")
        self.gridLayout_6.addWidget(self.label_NumberOfPinholes, 0, 1, 1, 1)
        self.label_PinholePitch = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_PinholePitch.setObjectName("label_PinholePitch")
        self.gridLayout_6.addWidget(self.label_PinholePitch, 2, 1, 1, 1)
        self.spinBox_NumberOfPinholes = QtWidgets.QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_NumberOfPinholes.setMinimumSize(QtCore.QSize(90, 25))
        self.spinBox_NumberOfPinholes.setMaximumSize(QtCore.QSize(90, 25))
        self.spinBox_NumberOfPinholes.setMinimum(1)
        self.spinBox_NumberOfPinholes.setMaximum(4)
        self.spinBox_NumberOfPinholes.setObjectName("spinBox_NumberOfPinholes")
        self.gridLayout_6.addWidget(self.spinBox_NumberOfPinholes, 0, 0, 1, 1)
        self.txt_PinholeRadius = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_6)
        self.txt_PinholeRadius.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_PinholeRadius.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_PinholeRadius.setTabChangesFocus(True)
        self.txt_PinholeRadius.setObjectName("txt_PinholeRadius")
        self.gridLayout_6.addWidget(self.txt_PinholeRadius, 1, 0, 1, 1)
        self.txt_PinholePitch = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_6)
        self.txt_PinholePitch.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_PinholePitch.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_PinholePitch.setTabChangesFocus(True)
        self.txt_PinholePitch.setObjectName("txt_PinholePitch")
        self.gridLayout_6.addWidget(self.txt_PinholePitch, 2, 0, 1, 1)
        self.label_PinholeRotation = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_PinholeRotation.setObjectName("label_PinholeRotation")
        self.gridLayout_6.addWidget(self.label_PinholeRotation, 3, 1, 1, 1)
        self.txt_PinholeRotation = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_6)
        self.txt_PinholeRotation.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_PinholeRotation.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_PinholeRotation.setTabChangesFocus(True)
        self.txt_PinholeRotation.setObjectName("txt_PinholeRotation")
        self.gridLayout_6.addWidget(self.txt_PinholeRotation, 3, 0, 1, 1)
        self.tab_MaskFunctionality.addTab(self.tab_Pinhole, "")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 290, 901, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.view_CameraImage = QtWidgets.QLabel(self.centralwidget)
        self.view_CameraImage.setGeometry(QtCore.QRect(10, 10, 480, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_CameraImage.sizePolicy().hasHeightForWidth())
        self.view_CameraImage.setSizePolicy(sizePolicy)
        self.view_CameraImage.setText("")
        self.view_CameraImage.setPixmap(QtGui.QPixmap("./TestImages/Vialux_DMD.png"))
        self.view_CameraImage.setScaledContents(True)
        self.view_CameraImage.setObjectName("view_CameraImage")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(500, 0, 425, 294))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_CamImageImport = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_CamImageImport.setObjectName("btn_CamImageImport")
        self.gridLayout.addWidget(self.btn_CamImageImport, 7, 0, 1, 2)
        self.cbox_LockCalibration = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.cbox_LockCalibration.setObjectName("cbox_LockCalibration")
        self.gridLayout.addWidget(self.cbox_LockCalibration, 7, 2, 1, 2)
        self.btn_SaveCalibration = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_SaveCalibration.setObjectName("btn_SaveCalibration")
        self.gridLayout.addWidget(self.btn_SaveCalibration, 6, 1, 1, 1)
        self.btn_Calibrate = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_Calibrate.setObjectName("btn_Calibrate")
        self.gridLayout.addWidget(self.btn_Calibrate, 6, 0, 1, 1)
        self.txt_HeightAdjust = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_HeightAdjust.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_HeightAdjust.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_HeightAdjust.setTabChangesFocus(True)
        self.txt_HeightAdjust.setObjectName("txt_HeightAdjust")
        self.gridLayout.addWidget(self.txt_HeightAdjust, 5, 2, 1, 1)
        self.label_CalibrationThreshold = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_CalibrationThreshold.setWordWrap(True)
        self.label_CalibrationThreshold.setObjectName("label_CalibrationThreshold")
        self.gridLayout.addWidget(self.label_CalibrationThreshold, 6, 3, 1, 1)
        self.label_CalibrationParameters = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_CalibrationParameters.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CalibrationParameters.setObjectName("label_CalibrationParameters")
        self.gridLayout.addWidget(self.label_CalibrationParameters, 0, 2, 1, 2)
        self.txt_CalibrationThreshold = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_CalibrationThreshold.sizePolicy().hasHeightForWidth())
        self.txt_CalibrationThreshold.setSizePolicy(sizePolicy)
        self.txt_CalibrationThreshold.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_CalibrationThreshold.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_CalibrationThreshold.setTabChangesFocus(True)
        self.txt_CalibrationThreshold.setObjectName("txt_CalibrationThreshold")
        self.gridLayout.addWidget(self.txt_CalibrationThreshold, 6, 2, 1, 1)
        self.radioButton_BlackImageMask = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_BlackImageMask.setChecked(True)
        self.radioButton_BlackImageMask.setAutoExclusive(True)
        self.radioButton_BlackImageMask.setObjectName("radioButton_BlackImageMask")
        self.gridLayout.addWidget(self.radioButton_BlackImageMask, 4, 0, 1, 1)
        self.radioButton_WhiteImageMask = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_WhiteImageMask.setAutoExclusive(True)
        self.radioButton_WhiteImageMask.setObjectName("radioButton_WhiteImageMask")
        self.gridLayout.addWidget(self.radioButton_WhiteImageMask, 4, 1, 1, 1)
        self.txt_DMDCalibrationImageRatio = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_DMDCalibrationImageRatio.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_DMDCalibrationImageRatio.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_DMDCalibrationImageRatio.setTabChangesFocus(True)
        self.txt_DMDCalibrationImageRatio.setPlaceholderText("")
        self.txt_DMDCalibrationImageRatio.setObjectName("txt_DMDCalibrationImageRatio")
        self.gridLayout.addWidget(self.txt_DMDCalibrationImageRatio, 3, 0, 1, 1)
        self.txt_RotationAdjust = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_RotationAdjust.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_RotationAdjust.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_RotationAdjust.setTabChangesFocus(True)
        self.txt_RotationAdjust.setObjectName("txt_RotationAdjust")
        self.gridLayout.addWidget(self.txt_RotationAdjust, 3, 2, 1, 1)
        self.label_CentreAdjustX = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_CentreAdjustX.setObjectName("label_CentreAdjustX")
        self.gridLayout.addWidget(self.label_CentreAdjustX, 1, 3, 1, 1)
        self.label_DMDSizeX = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_DMDSizeX.setObjectName("label_DMDSizeX")
        self.gridLayout.addWidget(self.label_DMDSizeX, 1, 1, 1, 1)
        self.label_WidthAdjust = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_WidthAdjust.setObjectName("label_WidthAdjust")
        self.gridLayout.addWidget(self.label_WidthAdjust, 4, 3, 1, 1)
        self.txt_DMDSizeY = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_DMDSizeY.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_DMDSizeY.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_DMDSizeY.setTabChangesFocus(True)
        self.txt_DMDSizeY.setPlaceholderText("")
        self.txt_DMDSizeY.setObjectName("txt_DMDSizeY")
        self.gridLayout.addWidget(self.txt_DMDSizeY, 2, 0, 1, 1)
        self.label_DMDParameters = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_DMDParameters.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DMDParameters.setObjectName("label_DMDParameters")
        self.gridLayout.addWidget(self.label_DMDParameters, 0, 0, 1, 2)
        self.txt_DMDSizeX = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_DMDSizeX.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_DMDSizeX.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_DMDSizeX.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.txt_DMDSizeX.setTabChangesFocus(True)
        self.txt_DMDSizeX.setPlaceholderText("")
        self.txt_DMDSizeX.setObjectName("txt_DMDSizeX")
        self.gridLayout.addWidget(self.txt_DMDSizeX, 1, 0, 1, 1)
        self.txt_WidthAdjust = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_WidthAdjust.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_WidthAdjust.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_WidthAdjust.setTabChangesFocus(True)
        self.txt_WidthAdjust.setObjectName("txt_WidthAdjust")
        self.gridLayout.addWidget(self.txt_WidthAdjust, 4, 2, 1, 1)
        self.label_CentreAdjustY = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_CentreAdjustY.setObjectName("label_CentreAdjustY")
        self.gridLayout.addWidget(self.label_CentreAdjustY, 2, 3, 1, 1)
        self.label_RotationAdjust = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_RotationAdjust.setWordWrap(True)
        self.label_RotationAdjust.setObjectName("label_RotationAdjust")
        self.gridLayout.addWidget(self.label_RotationAdjust, 3, 3, 1, 1)
        self.txt_CentreAdjustX = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_CentreAdjustX.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_CentreAdjustX.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_CentreAdjustX.setTabChangesFocus(True)
        self.txt_CentreAdjustX.setObjectName("txt_CentreAdjustX")
        self.gridLayout.addWidget(self.txt_CentreAdjustX, 1, 2, 1, 1)
        self.label_HeightAdjust = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_HeightAdjust.setObjectName("label_HeightAdjust")
        self.gridLayout.addWidget(self.label_HeightAdjust, 5, 3, 1, 1)
        self.label_DMDCalibrationImageRatio = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_DMDCalibrationImageRatio.setWordWrap(True)
        self.label_DMDCalibrationImageRatio.setObjectName("label_DMDCalibrationImageRatio")
        self.gridLayout.addWidget(self.label_DMDCalibrationImageRatio, 3, 1, 1, 1)
        self.txt_CentreAdjustY = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_CentreAdjustY.setMinimumSize(QtCore.QSize(90, 25))
        self.txt_CentreAdjustY.setMaximumSize(QtCore.QSize(90, 25))
        self.txt_CentreAdjustY.setTabChangesFocus(True)
        self.txt_CentreAdjustY.setObjectName("txt_CentreAdjustY")
        self.gridLayout.addWidget(self.txt_CentreAdjustY, 2, 2, 1, 1)
        self.label_DMDSizeY = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_DMDSizeY.setObjectName("label_DMDSizeY")
        self.gridLayout.addWidget(self.label_DMDSizeY, 2, 1, 1, 1)
        self.view_DMDMaskImage = QtWidgets.QLabel(self.centralwidget)
        self.view_DMDMaskImage.setGeometry(QtCore.QRect(20, 320, 480, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_DMDMaskImage.sizePolicy().hasHeightForWidth())
        self.view_DMDMaskImage.setSizePolicy(sizePolicy)
        self.view_DMDMaskImage.setText("")
        self.view_DMDMaskImage.setPixmap(QtGui.QPixmap("./TestImages/UoL_logo.jpeg"))
        self.view_DMDMaskImage.setScaledContents(True)
        self.view_DMDMaskImage.setObjectName("view_DMDMaskImage")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(531, 640, 391, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_BlackDMDMask = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_BlackDMDMask.setChecked(True)
        self.radioButton_BlackDMDMask.setAutoExclusive(True)
        self.radioButton_BlackDMDMask.setObjectName("radioButton_BlackDMDMask")
        self.gridLayout_2.addWidget(self.radioButton_BlackDMDMask, 0, 0, 1, 2)
        self.btn_DMDMaskSave = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_DMDMaskSave.setObjectName("btn_DMDMaskSave")
        self.gridLayout_2.addWidget(self.btn_DMDMaskSave, 1, 2, 1, 2)
        self.btn_DMDMaskGen = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_DMDMaskGen.setObjectName("btn_DMDMaskGen")
        self.gridLayout_2.addWidget(self.btn_DMDMaskGen, 1, 0, 1, 2)
        self.radioButton_WhiteDMDMask = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_WhiteDMDMask.setAutoExclusive(True)
        self.radioButton_WhiteDMDMask.setObjectName("radioButton_WhiteDMDMask")
        self.gridLayout_2.addWidget(self.radioButton_WhiteDMDMask, 0, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad_Calibration = QtWidgets.QAction(MainWindow)
        self.actionLoad_Calibration.setObjectName("actionLoad_Calibration")
        self.actionSave_Calibration = QtWidgets.QAction(MainWindow)
        self.actionSave_Calibration.setObjectName("actionSave_Calibration")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad_Calibration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_MaskFunctionality.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DMD Mask App"))
        self.txt_DMDCalibrationMaskRatio.setPlainText(_translate("MainWindow", "1"))
        self.txt_CentreCircleSize.setPlainText(_translate("MainWindow", "0"))
        self.label_CalibrationCentreCircle.setText(_translate("MainWindow", "Centre Circle Radius"))
        self.label_DMDCalibrationMaskRatio.setText(_translate("MainWindow", "Calibration Mask Ratio"))
        self.tab_MaskFunctionality.setTabText(self.tab_MaskFunctionality.indexOf(self.tab_Calibration), _translate("MainWindow", "Calibration"))
        self.txt_maskAdjustUD.setPlainText(_translate("MainWindow", "0"))
        self.btn_MaskToAdd.setText(_translate("MainWindow", "Mask Addition"))
        self.btn_getThresholdValues.setText(_translate("MainWindow", "Get Threshold Values"))
        self.label_maskAdjustLR.setText(_translate("MainWindow", "L/R Adjust"))
        self.txt_maskAdjustLR.setPlainText(_translate("MainWindow", "0"))
        self.label_maskAdjustUD.setText(_translate("MainWindow", "U/D Adjust"))
        self.label_highValueThreshold.setText(_translate("MainWindow", "1000"))
        self.label_ThresholdLevel.setText(_translate("MainWindow", "Curent Threshold"))
        self.txt_currentThreshold.setPlainText(_translate("MainWindow", "0"))
        self.label_maskAdjustRot.setText(_translate("MainWindow", "Rot Adjust"))
        self.txt_maskAdjustRot.setPlainText(_translate("MainWindow", "0"))
        self.label_lowValueThreshold.setText(_translate("MainWindow", "0"))
        self.cBox_FlipLR.setText(_translate("MainWindow", "Flip L/R"))
        self.cBox_FlipUD.setText(_translate("MainWindow", "Flip U/D"))
        self.tab_MaskFunctionality.setTabText(self.tab_MaskFunctionality.indexOf(self.tab_Threshold), _translate("MainWindow", "Threshold"))
        self.txt_SlitWidth.setPlainText(_translate("MainWindow", "0"))
        self.label_NumberOfSlits.setText(_translate("MainWindow", "Number of Slits"))
        self.txt_SlitSeparation.setPlainText(_translate("MainWindow", "0"))
        self.label_SlitSeparation.setText(_translate("MainWindow", "Slit Separation (um)"))
        self.label_SlitWidth.setText(_translate("MainWindow", "Slit Width (um)"))
        self.txt_SlitRotation.setPlainText(_translate("MainWindow", "0"))
        self.label_SlitRotation.setText(_translate("MainWindow", "Slit Rotation (deg)"))
        self.tab_MaskFunctionality.setTabText(self.tab_MaskFunctionality.indexOf(self.tab_Slit), _translate("MainWindow", "Slit"))
        self.label_PinholeRadius.setText(_translate("MainWindow", "Pinhole Radius (um)"))
        self.label_NumberOfPinholes.setText(_translate("MainWindow", "Number of Pinholes"))
        self.label_PinholePitch.setText(_translate("MainWindow", "Pinhole Pitch (um)"))
        self.txt_PinholeRadius.setPlainText(_translate("MainWindow", "0"))
        self.txt_PinholePitch.setPlainText(_translate("MainWindow", "0"))
        self.label_PinholeRotation.setText(_translate("MainWindow", "Pinhole Rotation (deg)"))
        self.txt_PinholeRotation.setPlainText(_translate("MainWindow", "0"))
        self.tab_MaskFunctionality.setTabText(self.tab_MaskFunctionality.indexOf(self.tab_Pinhole), _translate("MainWindow", "Pinhole"))
        self.btn_CamImageImport.setText(_translate("MainWindow", "Import Camera Image"))
        self.cbox_LockCalibration.setText(_translate("MainWindow", "Lock Calibration?"))
        self.btn_SaveCalibration.setText(_translate("MainWindow", "Save"))
        self.btn_Calibrate.setText(_translate("MainWindow", "Calibrate"))
        self.txt_HeightAdjust.setPlainText(_translate("MainWindow", "1"))
        self.label_CalibrationThreshold.setText(_translate("MainWindow", "Calibration Threshold"))
        self.label_CalibrationParameters.setText(_translate("MainWindow", "Calibration Adjustment"))
        self.txt_CalibrationThreshold.setPlainText(_translate("MainWindow", "200"))
        self.radioButton_BlackImageMask.setText(_translate("MainWindow", "Black Mask"))
        self.radioButton_WhiteImageMask.setText(_translate("MainWindow", "White Mask"))
        self.txt_DMDCalibrationImageRatio.setPlainText(_translate("MainWindow", "1"))
        self.txt_RotationAdjust.setPlainText(_translate("MainWindow", "0"))
        self.label_CentreAdjustX.setText(_translate("MainWindow", "Centre Adjust X"))
        self.label_DMDSizeX.setText(_translate("MainWindow", "DMD Size X"))
        self.label_WidthAdjust.setText(_translate("MainWindow", "Width Scaling"))
        self.txt_DMDSizeY.setPlainText(_translate("MainWindow", "1080"))
        self.label_DMDParameters.setText(_translate("MainWindow", "DMD Parameters"))
        self.txt_DMDSizeX.setPlainText(_translate("MainWindow", "1920"))
        self.txt_WidthAdjust.setPlainText(_translate("MainWindow", "1"))
        self.label_CentreAdjustY.setText(_translate("MainWindow", "Centre Adjust Y"))
        self.label_RotationAdjust.setText(_translate("MainWindow", "Rotation Adjust (clockwise)"))
        self.txt_CentreAdjustX.setPlainText(_translate("MainWindow", "0"))
        self.label_HeightAdjust.setText(_translate("MainWindow", "Height Scaling"))
        self.label_DMDCalibrationImageRatio.setText(_translate("MainWindow", "Calibration Image Ratio"))
        self.txt_CentreAdjustY.setPlainText(_translate("MainWindow", "0"))
        self.label_DMDSizeY.setText(_translate("MainWindow", "DMD Size Y"))
        self.radioButton_BlackDMDMask.setText(_translate("MainWindow", "Black Mask"))
        self.btn_DMDMaskSave.setText(_translate("MainWindow", "Save Current Mask"))
        self.btn_DMDMaskGen.setText(_translate("MainWindow", "Generate DMD Mask"))
        self.radioButton_WhiteDMDMask.setText(_translate("MainWindow", "White Mask"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Calibration.setText(_translate("MainWindow", "Load Calibration"))
        self.actionSave_Calibration.setText(_translate("MainWindow", "Save Calibration"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
