from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.units import cm

from reportlab.pdfgen import canvas

from .tools.tabelapdf import tabelapdf

from flask import url_for

import os

# Configurando o arquivo PDF
def make_pdf(tabela, cliente, valortotal, pdf_file):
    PAGE_WIDTH, PAGE_HEIGHT = A4
    
    base_path = os.path.dirname(os.path.abspath(__file__))  # Diretório atual (pdfmaker)
    logo_url = os.path.join(base_path, 'static', 'logo.png')
    # logo_url = url_for('static', filename='logo.png')
    
    # pdf_file = os.path.join(base_path,'..', 'static', 'tabela_exemplo_6_itens.pdf')
    # pdf_file = '../../static/tabela_exemplo_6_itens.pdf'
    document = SimpleDocTemplate(pdf_file, pagesize=A4)

    
    
    tabela = tabelapdf.makeTable(tabela, valortotal)

    imagem = Image(logo_url)  # Substitua pelo caminho da sua imagem
    imagem.width = 200  # Largura da imagem
    imagem.height = 120  # Altura da imagem

    # Criação do PDF
    from reportlab.pdfgen import canvas

    def create_pdf(canvas):
        # Posicionar a imagem em coordenadas (x, y)
        x = 23  # coordenada x
        y = 692  # coordenada y
        canvas.drawImage(logo_url, x, y, width=imagem.width, height=imagem.height)  # Desenhar a imagem
        
        
        #linha
        canvas.setStrokeColorRGB(0, 0, 0)  # Definindo a cor da linha (preto)
        canvas.setLineWidth(1)  # Definindo a espessura da linha
        canvas.line(30, 630, 565, 630)  # Linha da coordenada (100, 720) até (500, 720)
        # canvas.line(30, 0, 30, 900)  # Linha da coordenada (100, 720) até (500, 720)
        # canvas.line(565, 0, 565, 900)  # Linha da coordenada (100, 720) até (500, 720)
        # canvas.line(30, 806, 565, 805)  # Linha da coordenada (100, 720) até (500, 720)
        
        
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
    canvas = canvas.Canvas(pdf_file, pagesize=A4)
    create_pdf(canvas)
    

    print(f"PDF '{pdf_file}' criado com sucesso.")
    
    return canvas
    
    
dados = {'tabela': [['05/09/2024', 'Produto 1', '5', '15,00', '75,00'], ['09/09/2024', 'Produto 2', '3', '10,00', '15,00'], ['16/09/2024', 'Produto 3', '8', '5,50', '44,00'], ['01/09/2024', 'Produto 4', '1', '1.256,00', '1.256,00'], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], 'nomeCliente': 'Carlos Pereira Brito', 'valorTotal': '1.390,00'}

tabela = dados['tabela']
cliente = dados['nomeCliente']
valortotal = dados['valorTotal']


make_pdf(tabela=tabela, cliente=cliente, valortotal = valortotal)
