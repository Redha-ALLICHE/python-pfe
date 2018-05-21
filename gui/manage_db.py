import sys
from PyQt5 import QtCore, QtWidgets, QtSql
import functools



def initializeModel(model):
    model.setTable('DEVICES')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    


def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    view.hideColumn(0)
    return view


def addrow():
   print (model.rowCount())
   ret = model.insertRows(model.rowCount(), 1)
   print (ret)

def delrow(i):
    model.deleteRow(i)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('../network_db/devices.db')
    model = QtSql.QSqlTableModel()
    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)

    dlg = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view1)

    btn = QtWidgets.QPushButton()
    btn.setText("add")
    btn.clicked.connect(functools.partial(model.insertRow, model.rowCount()))
    btn1 = QtWidgets.QPushButton()
    btn1.setText("remove")
    
    btn1.clicked.connect(functools.partial(model.removeRow, model.rowCount()-1))
    layout.addWidget(btn)
    layout.addWidget(btn1)
    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.show()
    sys.exit(app.exec_())
