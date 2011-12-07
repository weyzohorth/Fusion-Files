#!/usr/bin/env python
#=[site officiel]=========================
#<<<<<fusion files QT by W3YZOH0RTH>>>>>
#============[http://progject.free.fr/]===
import PyQt4.Qt as qt
import gui.gui as GUI
import sys

app = qt.QApplication(sys.argv)
gui = GUI.Gui(sys.argv)
gui.show()
sys.exit(app.exec_())
