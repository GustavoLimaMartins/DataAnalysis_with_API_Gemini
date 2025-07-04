from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGroupBox
import loginGemini
from bimestralCS import RelatorioBimestralCS

class JanelaSecundaria(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fontes de dados integradas à IA")
        self.setGeometry(640, 200, 300, 280)

        groupName = QGroupBox(self, title='Selecione uma fonte de dados', alignment=4)
        groupName.setGeometry(50, 20, 200, 200)
        btnBimestralCS = QPushButton("KPIs Bimestrais - CS")

        layout = QVBoxLayout()
        layout.addWidget(btnBimestralCS)
        groupName.setLayout(layout)
        btnBimestralCS.clicked.connect(self.cliqueNoBotaoRelatorioCS)

    def cliqueNoBotaoRelatorioCS(self):
        loginGemini.JanelaInicial().fecharJanelaSecundaria()
        self.janela3 = RelatorioBimestralCS()
        self.janela3.show()
