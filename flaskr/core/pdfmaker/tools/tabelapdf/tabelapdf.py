from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def makeTable(tabela):
    # Dados da tabela (6 itens por linha)
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    
    large_font_style = ParagraphStyle(name='LargeFont', fontSize=14)
    
    tabela_header = ['Data de Venda', 'Produtos', 'Quantidade', 'P. Unitário', 'SubTotal']
    tabela_footer = ['','','','Total','R$ 100,000,00']
    
    tabela.insert(0, tabela_header)
    tabela.append(tabela_footer)


    # Obtenha a largura da página
    page_width = A4[0]

    # Define uma margem
    margin = 20  # Margem de 20 pontos em cada lado

    # Largura da tabela com margens
    table_width = page_width - 2 * margin
    print(table_width)
    col_widths = [65,220,55,85,130]  # Largura igual para cada coluna
    print(sum(col_widths))


    

    
    # Cria a tabela com a largura das colunas
    table = Table(tabela, colWidths=col_widths)

    # Estilizando a tabela
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centraliza o texto
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte do cabeçalho em negrito
        ('FONTSIZE', (0, 0), (-1, -1), 9),  # Tamanho da fonte no rodapé
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),  # Fundo das células em bege
        ('GRID', (0, 0), (-1, -1), 0.2, colors.lightgrey),  # Adiciona linhas entre as células
        
        # Estilo do rodapé
        
        
        ('ALIGN', (0, -1), (-1, -1), 'CENTER'),  # Alinhamento do rodapé
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),  # Fonte em negrito no rodapé
        ('FONTSIZE', (0, -1), (-1, -1), 12),  # Tamanho da fonte no rodapé
        ('TOPPADDING', (0, -1), (-1, -1), 10),  # Espaçamento superior no rodapé
        ('BOTTOMPADDING', (0, -1), (-1, -1), 10),  # Espaçamento inferior no rodapé
    ])

    table.setStyle(style)
    
    return table

