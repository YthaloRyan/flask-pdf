from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def makeTable(tabela, valortotal):
    # Dados da tabela (6 itens por linha)
    styles = getSampleStyleSheet()
    
    
    tabela_header = ['Data de Venda', 'Produtos', 'Quantidade', 'P. Unitário', 'SubTotal']
    tabela_footer = ['','','','Total',f'R$ {valortotal}']
    
    tabela.insert(0, tabela_header)
    tabela.append(tabela_footer)


    # Obtenha a largura da página
    page_width = A4[0]

    # Define uma margem
    margin = 30

    # Largura da tabela com margens
    table_width = page_width - 2 * margin
    
    col_widths = [75,200,65,80,115]  # Largura igual para cada coluna
    


    # Cria a tabela com a largura das colunas
    table = Table(tabela, colWidths=col_widths)

    # Estilizando a tabela
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centraliza o texto
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte do cabeçalho em negrito
        ('FONTSIZE', (0, 0), (-1, 0), 10),  # Tamanho da fonte
        ('FONTSIZE', (1, 1), (-1, -1), 10),  # Tamanho da fonte
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),  # Fundo das células em bege
        ('GRID', (0, 0), (-1, -1), 0.2, colors.lightgrey),  # Adiciona linhas entre as células
        ('TOPPADDING', (0, 0), (-1, -1), 6),  # Espaço em cima do cabeçalho
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Espaço embaixo do cabeçalho
        
        # Estilo do rodapé
        ('ALIGN', (0, -1), (-1, -1), 'CENTER'),  # Alinhamento do rodapé
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),  # Fonte em negrito no rodapé
        ('FONTSIZE', (0, -1), (-1, -1), 12),  # Tamanho da fonte no rodapé
        ('TOPPADDING', (0, -1), (-1, -1), 10),  # Espaçamento superior no rodapé
        ('BOTTOMPADDING', (0, -1), (-1, -1), 10),  # Espaçamento inferior no rodapé
    ])

    table.setStyle(style)
    
    return table

