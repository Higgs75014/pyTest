import sys
import pyodbc
from PyQt5.QtSql import QSqlQuery, QSqlQueryModel, QSqlDatabase

from frmMain import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QWidget, QMessageBox

server = "SERVEUREXTER"
database = "ListeDesAllocataires"
user = "sa"
pwd = "Recensement55"

class clfrmMain(QWidget, Ui_frmMain):

    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.setupUi(parent)
        self.loaddatabase("")
        self.leTxtSaisie.setPlaceholderText("Nom base...")
        self.leTxtSaisie.textChanged.connect(lambda: self.searchbase(self.leTxtSaisie.text()))
        self.lstBDD.currentItemChanged.connect(lambda: self.baseselected(self.lstBDD.currentItem().text()))

    def loaddatabase(self, ssaisie):

        try:
            connex = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + pwd)
            cursor = connex.cursor()

            squery = "select distinct NomBase from LDA2 where NomBase like '%" + ssaisie + "%'"
            cursor.execute(squery)
            recs = cursor.fetchone()

            while recs:
                self.lstBDD.addItem(str(recs[0]))
                recs = cursor.fetchone()

            cursor.close()
            connex.close()

            self.loaddatatv(ssaisie)

        except pyodbc.Error as err:

            msg = QMessageBox()
            msg.setWindowTitle("LDA")
            msg.setText(err.__str__())
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            r = msg.exec_()

            if r == QMessageBox.Ok:
                msg.close()

    def loaddatatv(self, text):

        try:
            connString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + ";DATABASE=" + database + ";UID=" + user + ";PWD=" + pwd

            db = QSqlDatabase.addDatabase('QODBC')
            db.setDatabaseName(connString)
            db.open()
            qry = QSqlQuery(db)
            qry.prepare("select * from LDA2 where Nom like '%" + text + "%' or Prénom like '%" + text + "%' or NuméroDemandeurEmploi like '%" + text + "%'")
            qry.exec()

            model = QSqlQueryModel()
            model.setQuery(qry)
            self.tvDatas.setModel(model)

            self.tvDatas.resizeColumnsToContents()
            self.tvDatas.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:#5B9BD5;color:white}")
            self.tvDatas.setShowGrid(True)
            self.tvDatas.verticalHeader().setVisible(False)
            self.tvDatas.setAlternatingRowColors(True)
            self.tvDatas.setStyleSheet("alternate-background-color: #DDEBF7; background:white;border: 1px solid black;")
            self.tvDatas.show()

        except pyodbc.Error as err:

            msg = QMessageBox()
            msg.setWindowTitle("LDA")
            msg.setText(err.__str__())
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            r = msg.exec_()

            if r == QMessageBox.Ok:
                msg.close()

    def searchbase(self, text):

        self.lstBDD.blockSignals(True)
        self.lstBDD.clear()
        self.lstBDD.blockSignals(False)
        self.loaddatabase(text)

    def baseselected(self, text):

        msg = QMessageBox()
        msg.setWindowTitle("LDA")
        msg.setText("Vous avez choisi la base de : " + text)
        msg.setStandardButtons(QMessageBox.Ok)
        r = msg.exec_()

        if r == QMessageBox.Ok:
            msg.close()


def main(args):
    app = QtWidgets.QApplication(sys.argv)
    frm = QtWidgets.QWidget()
    clfrmMain(frm)
    frm.setFixedSize(frm.width(), frm.height())
    frm.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
