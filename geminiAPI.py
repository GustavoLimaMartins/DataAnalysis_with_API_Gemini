from enum import verify

import requests
from dateutil.utils import today
from google import genai
from google.genai import types
import sys, os

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyAfVo2x1BWotQktd7Cpt2LbsT4H1H0VUGo")

def recurso(path_relativo):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # PyInstaller: caminho temporário
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))  # execução .py
    return os.path.join(base_path, path_relativo)

file_path = recurso('Pasta1.txt')
file_path2 = recurso('exe_dashboardRelatorioCS.html')

def queryGeminiRelatorioCS(prompt):

    myfile = client.files.upload(file=file_path)
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite-preview-06-17",
        contents=[f"Responda estritamente a seguinte questão (sem ser prolixo): {prompt};\n"
                  "Sabendo que o anexo é um arquivo no formato .csv (separado por ponto e vírgula) e os dados pertencem à empresa Diel Energia, sob a tutela de Lais Chaves, então oriente-se a partir da descrição dos dados abaixo para responder:\n"
                  "A coluna de 'Segmento' representa a categoria de mercado onde situa-se o cliente,\n"
                  "A coluna de 'Cliente' possui a lista completa de clientes ativos da Diel Energia LTDA,\n"
                  f"A coluna de 'Saving - Mês 1' é a taxa de saving energético no formato percentual (onde 100% é o melhor indicador), relativo ao mês/ano: {today().month-2}/2025,\n"
                  f"A coluna de 'Saving - Mês 2' é a taxa de saving energético no formato percentual (onde 100% é o melhor indicador), relativo ao mês/ano: {today().month-1}/2025,\n"
                  f"A coluna de 'Unidade com Programação - Mês 1' é a taxa de unidades contratadas do respectivo cliente com programação ativa no formato percentual, relativo ao mês/ano: {today().month-2}/2025,\n"
                  f"A coluna de 'Unidade com Programação - Mês 2' é a taxa de unidades contratadas do respectivo cliente com programação ativa no formato percentual, relativo ao mês/ano: {today().month-1}/2025,\n"
                  f"A coluna de 'Funcionamento Correto ON/OFF - Mês 1' é a taxa de obediência das máquinas de ar-condicionado à programação (liga/desliga e setpoint) acordada com o cliente, no formato percentual, relativo ao mês/ano: {today().month-2}/2025,\n"
                  f"A coluna de 'Funcionamento Correto ON/OFF - Mês 2' é a taxa de obediência das máquinas de ar-condicionado à programação (liga/desliga e setpoint) acordada com o cliente, no formato percentual, relativo ao mês/ano: {today().month-1}/2025,\n"
                  f"A coluna de 'Saúde das Máquinas - Mês 1' é a taxa que avalia o estado de saúde do parque de refrigeração (incluindo evaporadoras e condensadoras) conforme alertas de: risco, falha, offline ou operação normal, no formato percentual (onde 100% representa a melhor saúde), relativo ao mês/ano: {today().month-2}/2025,\n"
                  f"A coluna de 'Saúde das Máquinas - Mês 2' é a taxa que avalia o estado de saúde do parque de refrigeração (incluindo evaporadoras e condensadoras) conforme alertas de: risco, falha, offline ou operação normal, no formato percentual (onde 100% representa a melhor saúde), relativo ao mês/ano: {today().month-1}/2025,\n"
                  f"A coluna de 'Tx de disponibilidade (ajustado) - Mês 1' é a taxa de disponibilidade de rede de internet para os dispositivos de monitoramento (incluindo evaporadoras e condensadoras), conforme status de: online, offline e temporariamente offline, no formato percentual (onde 100% representa o melhor sinal de rede), relativo ao mês/ano: {today().month-2}/2025,\n"
                  f"A coluna de 'Tx de disponibilidade (ajustado) - Mês 2' é a taxa de disponibilidade de rede de internet para os dispositivos de monitoramento (incluindo evaporadoras e condensadoras), conforme status de: online, offline e temporariamente offline, no formato percentual (onde 100% representa o melhor sinal de rede), relativo ao mês/ano: {today().month-1}/2025",
                  myfile],
        config=types.GenerateContentConfig(
            thinking_config = types.ThinkingConfig(thinking_budget=-1)
        )
    )

    return response.text

def queryGeminiAnalyzerRelatorioCS():

    myfile = client.files.upload(file=file_path)
    html_example = client.files.upload(file=file_path2)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=["De acordo com o arquivo .html em anexo, gere um script em html (página web) funcional como um especialista em visualização de dados e desenvolvimento frontend, prepare um infográfico de página única (SPA) totalmente interativo, analisando os dados que foram fornecidos e integrando eles no arquivo (.html). Valide os dados e garanta que são fiéis ao arquivo de origem, conforme a descrição abaixo para plotar os visuais e garanta que todos estão funcionando adequadamente. Traga apenas o novo script, sem comentários inline!\n"
                  "Sabendo que o anexo é um arquivo no formato .csv (separado por ponto e vírgula) e os dados pertencem à empresa Diel Energia, sob a tutela de Lais Chaves, então oriente-se a partir da descrição dos dados abaixo para responder:\n"
                  "A coluna de 'Segmento' representa a categoria de mercado onde situa-se o cliente,\n"
                  "A coluna de 'Cliente' possui a lista completa de clientes ativos da Diel Energia LTDA,\n"
                  f"A coluna de 'Saving - Mês 1' é a taxa de saving energético no formato percentual (onde 100% é o melhor indicador), relativo ao mês/ano: {today().month - 2}/2025,\n"
                  f"A coluna de 'Saving - Mês 2' é a taxa de saving energético no formato percentual (onde 100% é o melhor indicador), relativo ao mês/ano: {today().month - 1}/2025,\n"
                  f"A coluna de 'Unidade com Programação - Mês 1' é a taxa de unidades contratadas do respectivo cliente com programação ativa no formato percentual, relativo ao mês/ano: {today().month - 2}/2025,\n"
                  f"A coluna de 'Unidade com Programação - Mês 2' é a taxa de unidades contratadas do respectivo cliente com programação ativa no formato percentual, relativo ao mês/ano: {today().month - 1}/2025,\n"
                  f"A coluna de 'Funcionamento Correto ON/OFF - Mês 1' é a taxa de obediência das máquinas de ar-condicionado à programação (liga/desliga e setpoint) acordada com o cliente, no formato percentual, relativo ao mês/ano: {today().month - 2}/2025,\n"
                  f"A coluna de 'Funcionamento Correto ON/OFF - Mês 2' é a taxa de obediência das máquinas de ar-condicionado à programação (liga/desliga e setpoint) acordada com o cliente, no formato percentual, relativo ao mês/ano: {today().month - 1}/2025,\n"
                  f"A coluna de 'Saúde das Máquinas - Mês 1' é a taxa que avalia o estado de saúde do parque de refrigeração (incluindo evaporadoras e condensadoras) conforme alertas de: risco, falha, offline ou operação normal, no formato percentual (onde 100% representa a melhor saúde), relativo ao mês/ano: {today().month - 2}/2025,\n"
                  f"A coluna de 'Saúde das Máquinas - Mês 2' é a taxa que avalia o estado de saúde do parque de refrigeração (incluindo evaporadoras e condensadoras) conforme alertas de: risco, falha, offline ou operação normal, no formato percentual (onde 100% representa a melhor saúde), relativo ao mês/ano: {today().month - 1}/2025,\n"
                  f"A coluna de 'Tx de disponibilidade (ajustado) - Mês 1' é a taxa de disponibilidade de rede de internet para os dispositivos de monitoramento (incluindo evaporadoras e condensadoras), conforme status de: online, offline e temporariamente offline, no formato percentual (onde 100% representa o melhor sinal de rede), relativo ao mês/ano: {today().month - 2}/2025,\n"
                  f"A coluna de 'Tx de disponibilidade (ajustado) - Mês 2' é a taxa de disponibilidade de rede de internet para os dispositivos de monitoramento (incluindo evaporadoras e condensadoras), conforme status de: online, offline e temporariamente offline, no formato percentual (onde 100% representa o melhor sinal de rede), relativo ao mês/ano: {today().month - 1}/2025",
                  myfile,
                  html_example]
    )

    return response.text