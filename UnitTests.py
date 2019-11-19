import sys
import unittest
from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtTest

import appMainWindow

app = QtWidgets.QApplication(sys.argv)

class appMainWindowTests(unittest.TestCase):
    # Unit tests for the GUI
    def setUp(self):
        # Create the GUI
        self.form = appMainWindow.appMainWindow()

    def test_defaults(self):
        # Test default values of GUI contents
        self.assertEqual(self.form.ui.btn_CamImageImport.text(), "Import Camera Image")
        self.assertEqual(self.form.ui.btn_DMDMaskGen.text(),"Generate DMD Mask")
        self.assertEqual(self.form.ui.btn_DMDMaskSave.text(),"Save DMD Mask")
        self.assertEqual(self.form.ui.btn_Calibrate,"Calibrate")
        
        
if __name__ == '__main__':
    unittest.main()