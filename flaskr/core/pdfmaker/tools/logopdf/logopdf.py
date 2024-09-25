from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Table

from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def makeLogo(image_path):
     # Cria o objeto de imagem
    img = Image(image_path)
    
    # Redimensiona a imagem automaticamente sem deformar
    img._restrictSize(300, 300)

    # Cria uma tabela com uma célula vazia à esquerda para mover a imagem para a direita
    table_data = [[img, '']]  # A célula vazia à esquerda move a imagem para a direita
    

    # Define as larguras das colunas da tabela (primeira coluna vazia)
    img_table = Table(table_data, colWidths=[200, 300])  # Ajuste a largura da coluna vazia para mover a imagem
    
    style = TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.2, colors.lightgrey),  # Adiciona linhas entre as células
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alinhamento à esquerda
    ])

    img_table.setStyle(style)
    
    return img_table