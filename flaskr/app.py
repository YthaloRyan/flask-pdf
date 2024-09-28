from flask import Flask, render_template, request, redirect, url_for, jsonify
from core import organizar_infos
from core.pdfmaker import pdf

import time

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('pdf/a4.html')
        
    
@app.route('/submit_form', methods=['POST'])
def submit_form():
    dados = request.get_json()
    
    infos = organizar_infos.start(dados)
    
    tabela = infos['tabela']
    cliente = infos['nomeCliente']
    valortotal = infos['valorTotal']
    
    pdf_path = './static/nota.pdf'
    
    canvas = pdf.make_pdf(tabela=tabela, cliente=cliente, valortotal=valortotal, pdf_file=pdf_path)
    
    canvas.save()
    
    
    
    return jsonify(message='Pdf Gerado')


@app.route('/teste')
def teste():
    return render_template('teste.html')



if __name__ == '__main__':
    app.run(debug=True)
