from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.units import cm

from reportlab.pdfgen import canvas

from .tools.tabelapdf import tabelapdf

from flask import url_for

import os

# Configurando o arquivo PDF
def make_pdf(tabela):
    base_path = os.path.dirname(os.path.abspath(__file__))  # Diretório atual (pdfmaker)
    logo_url = os.path.join(base_path, 'static', 'logo.png')
    # logo_url = url_for('static', filename='logo.png')
    
    pdf_file = os.path.join(base_path, 'static', 'tabela_exemplo_6_itens.pdf')
    document = SimpleDocTemplate(pdf_file, pagesize=A4)

    
    
    tabela = tabelapdf.makeTable(tabela)

    imagem = Image(logo_url)  # Substitua pelo caminho da sua imagem
    imagem.width = 250  # Largura da imagem
    imagem.height = 150  # Altura da imagem

    # Criação do PDF
    from reportlab.pdfgen import canvas

    def create_pdf(canvas):
        # Posicionar a imagem em coordenadas (x, y)
        x = 20  # coordenada x
        y = 680  # coordenada y
        canvas.drawImage(logo_url, x, y, width=imagem.width, height=imagem.height)  # Desenhar a imagem

        # Adicionar a tabela
        tabela.wrapOn(canvas, 0, 0)
        tabela.drawOn(canvas, 20, 200)  # Posicionar a tabela

    # Gerar o PDF
    canvas = canvas.Canvas(pdf_file, pagesize=A4)
    create_pdf(canvas)
    canvas.save()

    print(f"PDF '{pdf_file}' criado com sucesso.")
