import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

palette = app.palette()
palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor("black"))
app.setPalette(palette)

pbar = QtGui.QProgressDialog("Hatching Norggling...","Algebraic",0,100)
pbar.show()
pbar.setValue(50)

sys.exit(app.exec_())
