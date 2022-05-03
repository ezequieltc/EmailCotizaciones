
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import sqlite3


class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 470)
        MainWindow.setFixedSize(499, 470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Data/ruhrpumpen.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RFQlabel = QtWidgets.QLabel(self.centralwidget)
        self.RFQlabel.setGeometry(QtCore.QRect(30, 10, 71, 16))
        self.RFQlabel.setObjectName("RFQlabel")
        self.Cuerpolabel = QtWidgets.QLabel(self.centralwidget)
        self.Cuerpolabel.setGeometry(QtCore.QRect(30, 130, 47, 13))
        self.Cuerpolabel.setObjectName("Cuerpolabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 0, 47, 13))
        self.label_3.setObjectName("label_3")
        self.RFQlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.RFQlineEdit.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.RFQlineEdit.setObjectName("RFQlineEdit")
        self.CuerpocomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.CuerpocomboBox.setGeometry(QtCore.QRect(30, 150, 111, 22))
        self.CuerpocomboBox.setObjectName("CuerpocomboBox")
        self.CuerpocomboBox.addItem("")
        self.CuerpocomboBox.addItem("")
        self.CuerpocomboBox.addItem("")
        # self.CuerpocomboBox.addItem("")
        # self.CuerpocomboBox.setEnabled(False)
        self.CueproPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.CueproPlainTextEdit.setEnabled(True)
        self.CueproPlainTextEdit.setGeometry(QtCore.QRect(220, 20, 241, 141))
        self.CueproPlainTextEdit.setObjectName("CueproPlainTextEdit")
        self.EnviarpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnviarpushButton.setGeometry(QtCore.QRect(40, 380, 75, 23))
        self.EnviarpushButton.setObjectName("EnviarpushButton")
        self.Destinatarioslabel = QtWidgets.QLabel(self.centralwidget)
        self.Destinatarioslabel.setGeometry(QtCore.QRect(30, 230, 71, 16))
        self.Destinatarioslabel.setObjectName("Destinatarioslabel")
        self.DestinatariocomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.DestinatariocomboBox.setGeometry(QtCore.QRect(30, 250, 111, 22))
        self.DestinatariocomboBox.setObjectName("DestinatariocomboBox")
        self.DestinatariocomboBox.addItem("")
        self.DestinatariocomboBox.addItem("")
        self.DestinatariocomboBox.addItem("")
        self.DestinatariocomboBox.addItem("")
        # self.DestinatariocomboBox.addItem("")
        self.AdjuntarArchivoscheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.AdjuntarArchivoscheckBox.setGeometry(
            QtCore.QRect(30, 290, 111, 17))
        self.AdjuntarArchivoscheckBox.setObjectName("AdjuntarArchivoscheckBox")
        self.PaisLabel = QtWidgets.QLabel(self.centralwidget)
        self.PaisLabel.setGeometry(QtCore.QRect(30, 180, 47, 13))
        self.PaisLabel.setObjectName("PaisLabel")
        self.PaisComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.PaisComboBox.setGeometry(QtCore.QRect(30, 200, 111, 22))
        self.PaisComboBox.setObjectName("PaisComboBox")
        self.PaisComboBox.addItem("")
        self.PaisComboBox.addItem("")
        self.PaisComboBox.addItem("")
        # self.PaisComboBox.addItem("")
        # self.PaisComboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setGeometry(QtCore.QRect(220, 230, 241, 71))
        self.textBrowser.setInputMethodHints(
            QtCore.Qt.ImhMultiLine | QtCore.Qt.ImhNoEditMenu | QtCore.Qt.ImhNoTextHandles)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.AdjuntarArchivosPushButton = QtWidgets.QPushButton(
            self.centralwidget)
        self.AdjuntarArchivosPushButton.setEnabled(False)
        self.AdjuntarArchivosPushButton.setGeometry(
            QtCore.QRect(30, 310, 101, 23))
        self.AdjuntarArchivosPushButton.setObjectName(
            "AdjuntarArchivosPushButton")
        self.Archivoslabel = QtWidgets.QLabel(self.centralwidget)
        self.Archivoslabel.setEnabled(False)
        self.Archivoslabel.setGeometry(QtCore.QRect(220, 200, 101, 16))
        self.Archivoslabel.setObjectName("Archivoslabel")
        self.labelAsu = QtWidgets.QLabel(self.centralwidget)
        self.labelAsu.setGeometry(QtCore.QRect(220, 320, 91, 16))
        self.labelAsu.setObjectName("labelAsu")
        self.AsuntoLabel = QtWidgets.QLabel(self.centralwidget)
        self.AsuntoLabel.setGeometry(QtCore.QRect(220, 340, 261, 16))
        self.AsuntoLabel.setText("")
        self.AsuntoLabel.setObjectName("AsuntoLabel")
        self.EliminarPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.EliminarPushButton.setEnabled(False)
        self.EliminarPushButton.setGeometry(QtCore.QRect(30, 340, 101, 23))
        self.EliminarPushButton.setObjectName("EliminarPushButton")
        self.CotComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.CotComboBox.setGeometry(QtCore.QRect(30, 100, 111, 22))
        self.CotComboBox.setObjectName("CotComboBox")
        self.CotComboBox.addItem("")
        self.CotComboBox.addItem("")
        self.CotComboBox.addItem("")
        self.ServiciolineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ServiciolineEdit.setGeometry(QtCore.QRect(30, 70, 181, 20))
        self.ServiciolineEdit.setObjectName("ServiciolineEdit")
        self.Serviciolabel = QtWidgets.QLabel(self.centralwidget)
        self.Serviciolabel.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.Serviciolabel.setObjectName("Serviciolabel")
        self.StatusLabelTexto = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabelTexto.setGeometry(QtCore.QRect(220, 390, 91, 16))
        self.StatusLabelTexto.setObjectName("StatusLabelTexto")
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setGeometry(QtCore.QRect(270, 390, 211, 16))
        self.StatusLabel.setText("")
        self.StatusLabel.setObjectName("StatusLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuConfiguracion = QtWidgets.QMenu(self.menubar)
        self.menuConfiguracion.setObjectName("menuConfiguracion")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionOpciones = QtWidgets.QAction(MainWindow)
        self.actionOpciones.setObjectName("actionOpciones")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuConfiguracion.addAction(self.actionOpciones)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuConfiguracion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Enviar Email Proveedores"))
        self.RFQlabel.setText(_translate("MainWindow", "RFQ:"))
        self.Cuerpolabel.setText(_translate("MainWindow", "Cuerpo:"))
        self.label_3.setText(_translate("MainWindow", "Cuerpo:"))
        self.CuerpocomboBox.setItemText(
            0, _translate("MainWindow", "Elija cuerpo..."))
        self.CuerpocomboBox.setItemText(
            1, _translate("MainWindow", "Estandar Español"))
        self.CuerpocomboBox.setItemText(
            2, _translate("MainWindow", "Estandar Ingles"))
        self.CuerpocomboBox.setItemText(
            3, _translate("MainWindow", "Personalizado"))
        self.EnviarpushButton.setText(_translate("MainWindow", "Enviar"))
        self.Destinatarioslabel.setText(
            _translate("MainWindow", "Destinatarios:"))
        self.DestinatariocomboBox.setCurrentText(
            _translate("MainWindow", "Elija destinatario..."))
        self.DestinatariocomboBox.setItemText(
            0, _translate("MainWindow", "Elija destinatario..."))
        self.DestinatariocomboBox.setItemText(
            1, _translate("MainWindow", "Motores"))
        self.DestinatariocomboBox.setItemText(
            2, _translate("MainWindow", "Sellos"))
        self.DestinatariocomboBox.setItemText(
            3, _translate("MainWindow", "Acoples"))
        self.DestinatariocomboBox.setItemText(
            4, _translate("MainWindow", "Otros..."))
        self.AdjuntarArchivoscheckBox.setText(
            _translate("MainWindow", "Adjuntar Archivos"))
        self.PaisLabel.setText(_translate("MainWindow", "País:"))
        self.PaisComboBox.setItemText(
            0, _translate("MainWindow", "Elija el país..."))
        self.PaisComboBox.setItemText(1, _translate("MainWindow", "Argentina"))
        self.PaisComboBox.setItemText(2, _translate("MainWindow", "Mexico"))
        # self.PaisComboBox.setItemText(3, _translate("MainWindow", "Rusia"))
        # self.PaisComboBox.setItemText(4, _translate("MainWindow", "China"))
        self.AdjuntarArchivosPushButton.setText(
            _translate("MainWindow", "Elegir Archivos..."))
        self.Archivoslabel.setText(_translate(
            "MainWindow", "Archivos Adjuntos:"))
        self.labelAsu.setText(_translate("MainWindow", "Asunto del Email:"))
        self.EliminarPushButton.setText(
            _translate("MainWindow", "Eliminar Archivos"))
        self.CotComboBox.setItemText(0, _translate(
            "MainWindow", "Tipo cotizacion..."))
        self.CotComboBox.setItemText(1, _translate("MainWindow", "Budget"))
        self.CotComboBox.setItemText(2, _translate("MainWindow", "Firme"))
        self.Serviciolabel.setText(_translate("MainWindow", "Servicio:"))
        self.StatusLabelTexto.setText(_translate("MainWindow", "Estado:"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuConfiguracion.setTitle(
            _translate("MainWindow", "Configuracion"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionOpciones.setText(_translate("MainWindow", "Opciones"))

    def checkbox(self, state):
        if QtCore.Qt.Checked == state:
            self.AdjuntarArchivosPushButton.setEnabled(True)
            self.Archivoslabel.setEnabled(True)
            self.textBrowser.setEnabled(True)
            self.EliminarPushButton.setEnabled(True)
        else:
            self.AdjuntarArchivosPushButton.setEnabled(False)
            self.Archivoslabel.setEnabled(False)
            self.textBrowser.setEnabled(False)
            self.EliminarPushButton.setEnabled(False)

    def openFileNamesDialog(self):
        global files
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(
            MainWindow, "QFileDialog.getOpenFileNames()", "", "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
            self.archivos = "\n".join(files)
        self.textBrowser.setText(self.archivos)
        print(self.archivos)

    def eliminarAjuntos(self):
        self.textBrowser.setText("")
        self.archivos = ""
        print(self.archivos)

    def enviar(self):
        conn = sqlite3.connect('database.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT * FROM proveedores WHERE destinatarios= :destinatarios AND pais=:pais",
                      {'destinatarios': self.destino, 'pais': self.paisdest})
            resultado = c.fetchall()
        print(resultado)
        # print(self.archivos)

        # print(self.cuerpo)
        print(self.destino)
        print(self.paisdest)

    def texto(self, text):
        if text == 'Estandar Español':
            self.cuerpo = "Este es el texto en español papa"
        elif text == "Estandar Ingles":
            self.cuerpo = "This is a texto en ingles"
        # print(text)

    def destinos(self, text):
        self.destino = text
        # print(text)

    def pais(self, text):
        self.paisdest = text


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.AdjuntarArchivoscheckBox.stateChanged.connect(ui.checkbox)
    ui.AdjuntarArchivosPushButton.clicked.connect(ui.openFileNamesDialog)
    ui.EliminarPushButton.clicked.connect(ui.eliminarAjuntos)
    ui.EnviarpushButton.clicked.connect(ui.enviar)
    ui.CuerpocomboBox.activated[str].connect(ui.texto)
    ui.PaisComboBox.activated[str].connect(ui.pais)
    ui.DestinatariocomboBox.activated[str].connect(ui.destinos)
    sys.exit(app.exec_())
