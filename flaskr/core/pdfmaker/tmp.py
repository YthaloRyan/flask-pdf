from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.units import cm

from reportlab.pdfgen import canvas

from tools.tabelapdf import tabelapdf
from tools.coletar_dim_imagen import dimensoes_imagem as di

from flask import url_for

import os

from PIL import Image as PILImage


class makePdf():
    def __init__(self, tabela, cliente, valortotal):
        self.tabela = tabela
        self.cliente = cliente
        self.valortotal = valortotal
        
        self.base_path = os.path.join(os.getcwd(), 'static')
        self.logo_path = os.path.join(self.base_path, 'logo.png')
        
        self.pdf_path = os.path.join(self.base_path, 'testes.pdf')
        
        self.logo_altura_maxima = 120
        
        self.espacamento = 30
        
        self.contatos = ['Fones: (88) 99711-6000', '(88) 99837-4888 / (88) 99720-1388',
                    'End: Rua G, nº 40 Bairro Cidade Nova / Tauá - CE']
        
    
    def draw_image(self, x, y):
        nova_largura, nova_altura = di.redimensionar_imagem_por_altura(self.logo_altura_maxima, self.logo_path)
        
        self.pdf.drawImage(self.logo_path, x, y, width=nova_largura, height=nova_altura)
    
    
    def draw_string(self, font, size, text, y):
        self.pdf.setFont(font, size)
        self.pdf.drawString(self.espacamento, y, text)
        
    def draw_string_list(self, font, size, string_list, y):
        text = self.pdf.beginText()
        text.setFont(font, size)
        text.setFillColor(colors.black)

        
        maior_string = max(string_list, key=len)
        maior_string_size = self.pdf.stringWidth(maior_string, font, size)
        
        
        y_position = y
        
        max_position = 1160 - self.espacamento - maior_string_size

        
        for linha in string_list:
            text_width = self.pdf.stringWidth(linha, font, size)
            
            # Calcular a posição X para centralizar em relação à página
            x_position = (max_position - text_width) / 2
            text.setTextOrigin(x_position, y_position)
            
            
            text.textLine(linha)
            
    
            y_position -= 20
            
        self.pdf.drawText(text)
        
        
    
    def draw_demarcador(self):
        self.pdf.setStrokeColorRGB(0, 0, 0)  # Definindo a cor da linha (preto)
        self.pdf.setLineWidth(1)  # Definindo a espessura da linha
        self.pdf.line(self.espacamento, 630, 565, 630)  # Linha da coordenada (100, 720) até (500, 720)
        self.pdf.line(self.espacamento, 0, 30, 900)  # Linha da coordenada (100, 720) até (500, 720)
        self.pdf.line(565, 0, 565, 900)  # Linha da coordenada (100, 720) até (500, 720)
        self.pdf.line(self.espacamento, 806, 565, 805)  # Linha da coordenada (100, 720) até (500, 720)

    def draw_divisoria(self, y):
        self.pdf.setStrokeColorRGB(0, 0, 0)  # Definindo a cor da linha (preto)
        self.pdf.setLineWidth(1)  # Definindo a espessura da linha
        self.pdf.line(self.espacamento, y, 595 - self.espacamento, y)  # Linha da coordenada (100, 720) até (500, 720)
        
        
        
        
        
    
    
    
    
    def start(self):
        print(A4)
        pdf_path = os.path.join(self.base_path, 'nota.pdf')
        
        self.pdf = canvas.Canvas(self.pdf_path, pagesize=A4)
        
        # imagem
        self.draw_image(x=23, y=692)
        
        
        # linhas
        self.draw_demarcador()
        self.draw_divisoria(y=630)
        
        
        # nome do cliente
        self.draw_string(font="Helvetica", size=20, text=f"Nome: {self.cliente}", y=650)
        
        # lista de contatos
        
        
        self.draw_string_list(font="Helvetica-Bold", size=10, string_list=self.contatos, y=797)
        
        
        # tabela
        pdf_tabela = tabelapdf.makeTable(self.tabela, self.valortotal)
        pdf_tabela.wrapOn(self.pdf, 0, 0)
        pdf_tabela.drawOn(self.pdf, self.espacamento, 75)  # Posicionar a tabela
        
        
        
        
        
        
        
        self.pdf.save()
        
        

tabela = [['11/09/2024', 'produto1', '12', '456,00', '5.472,00'], ['09/09/2024', 'produto 2', '54', '4,25', '229,50'], ['14/09/2024', 'prduto com o nome bastante grande', '2', '467.890,00', '935.780,00'], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
makePdf(tabela=tabela, cliente='Carlin', valortotal='124135').start()
        
        
        