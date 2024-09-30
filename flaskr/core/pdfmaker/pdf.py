from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.units import cm

from reportlab.pdfgen import canvas as cv

from .tools.tabelapdf import tabelapdf

from flask import url_for

import os

from PIL import Image as PILImage

def redimensionar_imagem(caminho_imagem, altura_maxima):
    # Abra a imagem usando Pillow para obter as dimensões
    img = PILImage.open(caminho_imagem)
    largura_original, altura_original = img.size
    
    
    
    # Calcula a nova altura proporcional
    proporcao = altura_maxima / altura_original
    nova_largura = int(largura_original * proporcao)
    
    return nova_largura, altura_maxima

# Configurando o arquivo PDF
def make_pdf(tabela, cliente, valortotal):
    
    
    current_directory = os.getcwd()
    logo_url = os.path.join(current_directory, 'static', 'logo.png')
    pdf_url = os.path.join(current_directory, 'static', 'nota.pdf')
    
    
    
    print("Current Directory:", current_directory)
    
    
    
    
    
    canvas = cv.Canvas(pdf_url, pagesize=A4)

    
    
    tabela = tabelapdf.makeTable(tabela, valortotal)

    # imagem = Image(logo_url)  # Substitua pelo caminho da sua imagem
    # print(imagem.imageWidth)
    # print(imagem.imageHeight)
    # imagem.imageWidth = int(imagem.imageWidth * 0.3)  # Largura da imagem
    # imagem.imageHeight = int(imagem.imageHeight * 0.3)  # Altura da imagem
    # print(imagem.imageWidth)
    # print(imagem.imageHeight)
    nova_altura = 120

    nova_largura, nova_altura = redimensionar_imagem(logo_url, nova_altura)
    
    print(nova_largura)
    print(nova_altura)

    
    # Posicionar a imagem em coordenadas (x, y)
    x = 23  # coordenada x
    y = 692  # coordenada y
    canvas.drawImage(logo_url, x, y, width=nova_largura, height=nova_altura)  # Desenhar a imagem
    
    
    #linha
    canvas.setStrokeColorRGB(0, 0, 0)  # Definindo a cor da linha (preto)
    canvas.setLineWidth(1)  # Definindo a espessura da linha
    canvas.line(30, 630, 565, 630)  # Linha da coordenada (100, 720) até (500, 720)
    canvas.line(30, 0, 30, 900)  # Linha da coordenada (100, 720) até (500, 720)
    canvas.line(565, 0, 565, 900)  # Linha da coordenada (100, 720) até (500, 720)
    canvas.line(30, 806, 565, 805)  # Linha da coordenada (100, 720) até (500, 720)
    
    
    #nomecliente
    canvas.setFont("Helvetica", 20)
    canvas.drawString(30, 650, f"Nome: {cliente}")
    
    
    # Criando um objeto de texto
    text = canvas.beginText()
    text.setFont("Helvetica-Bold", 10)
    text.setFillColor(colors.black)

    # Adicionando várias linhas de texto
    contatos = ['Fones: (88) 99711-6000', '(88) 99837-4888 / (88) 99720-1388',
                'End: Rua G, nº 40 Bairro Cidade Nova / Tauá - CE']
    # Definir a posição Y inicial (vertical)
    
    y_position = 797

    # Para cada linha de texto, calcular a largura e centralizar
    for linha in contatos:
        # Calcular a largura da linha
        text_width = canvas.stringWidth(linha, "Helvetica-Bold", 10)
        
        # Calcular a posição X para centralizar em relação à página
        x_position = (898 - text_width) / 2
        
        # Definir a origem do texto com base no cálculo acima
        text.setTextOrigin(x_position, y_position)
        
        # Adicionar a linha de texto
        text.textLine(linha)
        
        # Ajustar a posição Y para a próxima linha (diminuir para mover para baixo)
        y_position -= 20  # Ajuste a altura da linha conforme necessário
        
    canvas.drawText(text)
    
    

    # Adicionar a tabela
    tabela.wrapOn(canvas, 0, 0)
    tabela.drawOn(canvas, 30, 75)  # Posicionar a tabela

    # Gerar o PDF
    
    
    

    print(f"PDF criado com sucesso.")
    
    canvas.save()
    
