# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName("frmMain")
        frmMain.resize(1508, 797)
        self.leTxtSaisie = QtWidgets.QLineEdit(frmMain)
        self.leTxtSaisie.setGeometry(QtCore.QRect(30, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.leTxtSaisie.setFont(font)
        self.leTxtSaisie.setObjectName("leTxtSaisie")
        self.lstBDD = QtWidgets.QListWidget(frmMain)
        self.lstBDD.setGeometry(QtCore.QRect(30, 80, 281, 561))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lstBDD.setFont(font)
        self.lstBDD.setObjectName("lstBDD")
        self.tvDatas = QtWidgets.QTableView(frmMain)
        self.tvDatas.setGeometry(QtCore.QRect(330, 80, 1161, 681))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tvDatas.setFont(font)
        self.tvDatas.setStyleSheet("alternate-background-color: rgb(221, 221, 110);")
        self.tvDatas.setObjectName("tvDatas")
        self.gbAllocataire = QtWidgets.QGroupBox(frmMain)
        self.gbAllocataire.setGeometry(QtCore.QRect(30, 660, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.gbAllocataire.setFont(font)
        self.gbAllocataire.setTitle("")
        self.gbAllocataire.setObjectName("gbAllocataire")
        self.gbDetailDossier = QtWidgets.QGroupBox(frmMain)
        self.gbDetailDossier.setGeometry(QtCore.QRect(340, 10, 511, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gbDetailDossier.setFont(font)
        self.gbDetailDossier.setObjectName("gbDetailDossier")
        self.lblDetail = QtWidgets.QLabel(self.gbDetailDossier)
        self.lblDetail.setGeometry(QtCore.QRect(10, 30, 411, 20))
        self.lblDetail.setObjectName("lblDetail")
        self.pbWWW = QtWidgets.QPushButton(frmMain)
        self.pbWWW.setGeometry(QtCore.QRect(870, 20, 75, 41))
        self.pbWWW.setStyleSheet("background:transparent")
        self.pbWWW.setObjectName("pbWWW")

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        frmMain.setWindowTitle(_translate("frmMain", "Liste des allocataires"))
        self.gbDetailDossier.setTitle(_translate("frmMain", "Détail du dossier"))
        self.lblDetail.setText(_translate("frmMain", "Etat: indemnisation - Reliquat: 91 - ARR (mois précédent): Non"))
        self.pbWWW.setText(_translate("frmMain", "PushButton"))
