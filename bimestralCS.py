import sys
import time

from dateutil.utils import today
import webbrowser
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QTextEdit, QMessageBox
from geminiAPI import queryGeminiRelatorioCS, queryGeminiAnalyzerRelatorioCS

global exe
exe = 0

class RelatorioBimestralCS(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prompt de conversa com a IA Gemini")
        self.setGeometry(500, 120, 600, 625)

        groupName = QGroupBox(self, title='Faça perguntas pertinentes ao relatório bimestral de CS', alignment=4)
        groupName.setGeometry(25, 10, 550, 180)
        self.groupName2 = QGroupBox(self, title='Resposta do Gemini', alignment=4)
        self.groupName2.setGeometry(25, 300, 550, 250)
        groupName3 = QGroupBox(self)
        groupName3.setGeometry(25, 550, 550, 50)
        self.boxPrompt = QTextEdit(self)
        self.boxPrompt.setMaximumWidth(550)
        self.boxPrompt.setMaximumHeight(125)
        self.btnEnviar = QPushButton('Enviar para o Gemini')
        self.btnApagar = QPushButton('Reiniciar chat com IA')
        self.btnApagar.setEnabled(False)
        self.btnEnviar.clicked.connect(self.enviarParaGemini)
        self.btnApagar.clicked.connect(self.apagarChatGemini)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.boxPrompt)
        self.layout.addWidget(self.btnEnviar)
        self.layout.addWidget(self.btnApagar)
        groupName.setLayout(self.layout)
        self.layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()

        self.btnGerarRelatorio = QPushButton("Gerar dashboard com IA")
        self.btnGerarRelatorio.setMaximumWidth(225)
        self.btnGerarRelatorio.clicked.connect(self.gerarDashboardGemini)

        self.btnAbrirRelatorio = QPushButton("Abrir dashboard da IA")
        self.btnAbrirRelatorio.setMaximumWidth(225)
        self.btnAbrirRelatorio.setEnabled(False)
        self.btnAbrirRelatorio.clicked.connect(self.abrirDashboardGemini)

        self.btnCopiarGemini = QPushButton("Copiar resposta da IA")
        self.btnCopiarGemini.setEnabled(False)
        self.btnCopiarGemini.clicked.connect(self.copiarRespostaGemini)

        layout3.addWidget(self.btnCopiarGemini)
        layout3.addWidget(self.btnGerarRelatorio)
        layout3.addWidget(self.btnAbrirRelatorio)
        groupName3.setLayout(layout3)

        lblData = QLabel(self)
        lblData.setGeometry(25, 170, 550, 100)
        lblData.setText("Dados:\nTaxa de Saving; Taxa de Unidade com Programação; Taxa de Funcionamento Correto ON/OFF;\nTaxa de Saúde das Máquinas e Taxa de Disponibilidade (ajustada)")
        lblFilter = QLabel(self)
        lblFilter.setGeometry(25, 220, 550, 100)
        lblFilter.setText(f"Filtros:\nSegmento; Cliente; Mês ({today().month - 2}/2025 e {today().month - 1}/2025)")

    def enviarParaGemini(self):
        self.prompt = self.boxPrompt.toPlainText()
        responseGemini = queryGeminiRelatorioCS(self.prompt)

        global exe
        if exe == 0:
            self.boxGemini = QTextEdit(self)
            self.boxGemini.setReadOnly(True)
            self.layout2.addWidget(self.boxGemini)

        self.boxGemini.setText(responseGemini)
        self.groupName2.setLayout(self.layout2)
        self.btnCopiarGemini.setEnabled(True)
        self.btnApagar.setEnabled(True)
        exe =+ 1

    def apagarChatGemini(self):
        self.boxPrompt.setText('')
        self.boxGemini.setText('')
        self.btnCopiarGemini.setEnabled(False)
        self.btnApagar.setEnabled(False)
        QMessageBox.information(self, "Chat reiniciado!", "Faça outra pergunta...")

    def gerarDashboardGemini(self):
        QMessageBox.information(self, "Em andamento!", "O dashboard será construído, aperte 'OK' para continuar...")
        conteudo_html = queryGeminiAnalyzerRelatorioCS()
        with open("dashboardRelatorioCS.html", "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo_html)

        QMessageBox.information(self, "Sucesso!", "Dashboard gerado, você já pode abri-lo")
        self.btnAbrirRelatorio.setEnabled(True)
        self.btnGerarRelatorio.setEnabled(False)

    def abrirDashboardGemini(self):
        webbrowser.open_new_tab("dashboardRelatorioCS.html")

    def copiarRespostaGemini(self):
        texto = self.boxGemini.toPlainText()
        QApplication.clipboard().setText(texto)
        QMessageBox.information(self, "Sucesso", "Texto copiado!\nUse Ctrl+V para colar.")

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    # Create and show the form
    global janela
    janela = RelatorioBimestralCS()
    janela.show()
    # Run the main Qt loop
    sys.exit(app.exec())