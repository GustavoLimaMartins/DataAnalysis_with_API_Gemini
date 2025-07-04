import sys
from dataOptions import JanelaSecundaria
from PySide6.QtWidgets import QLabel, QApplication, QDialog, QGroupBox, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

class JanelaInicial(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acesso ao interpretador IA Gemini - DIEL")
        self.setGeometry(640, 200, 300, 280)

        groupName = QGroupBox(self, title='Login', alignment=4)
        groupName.setGeometry(50, 20, 200, 200)
        self.boxName = QLineEdit(self)
        lblName = QLabel(self)
        self.boxPass = QLineEdit(self)
        self.boxPass.setEchoMode(QLineEdit.Password)
        lblPass = QLabel(self)
        btnLogin = QPushButton('Acessar')
        lblSpace = QLabel(self)

        layout = QVBoxLayout()
        lblName.setText("Usuário")
        layout.addWidget(lblName)
        layout.addWidget(self.boxName)
        lblPass.setText("Senha")
        layout.addWidget(lblPass)
        layout.addWidget(self.boxPass)
        layout.addWidget(lblSpace)
        layout.addWidget(btnLogin)
        groupName.setLayout(layout)
        btnLogin.clicked.connect(self.cliqueNoBotaoLogin)

    def cliqueNoBotaoLogin(self):
        if self.boxName.text() == 'gustavo.lima' and self.boxPass.text() == '1234':
            QMessageBox.information(self, "Sucesso!", "Login realizado!")
            janela.hide()
            # Menu de opções das bases de dados para escolha
            global janela2
            janela2 = JanelaSecundaria()
            janela2.show()
        else:
            QMessageBox.information(self, "Falha!", "Usuário/Senha incorretos!")

    def fecharJanelaSecundaria(self):
        janela2.hide()

def executarAuthenticator():
    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    # Create and show the form
    global janela
    janela = JanelaInicial()
    janela.show()
    # Run the main Qt loop
    sys.exit(app.exec())
