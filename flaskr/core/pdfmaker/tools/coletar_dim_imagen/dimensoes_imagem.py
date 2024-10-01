from PIL import Image as PILImage

def redimensionar_imagem_por_altura(altura_maxima, logo_path):
    # Abra a imagem usando Pillow para obter as dimensões
    img = PILImage.open(logo_path)
    largura_original, altura_original = img.size


    # Calcula a nova altura proporcional
    proporcao = altura_maxima / altura_original
    nova_largura = int(largura_original * proporcao)
    
    return nova_largura, altura_maxima