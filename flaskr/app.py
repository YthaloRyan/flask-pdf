from flask import Flask, render_template, request, jsonify
from core import organizar_infos
from core.pdfmaker import pdf

contatos = ['Fones: (88) 99711-6000', '(88) 99837-4888 / (88) 99720-1388',
                    'End: Rua G, nº 40 Bairro Cidade Nova / Tauá - CE']

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('pdf/a4.html', contatos=contatos)
        
    
@app.route('/submit_form', methods=['POST'])
def submit_form():
    dados = request.get_json()
    
    infos = organizar_infos.start(dados)
    
    tabela = infos['tabela']
    cliente = infos['nomeCliente']
    valortotal = infos['valorTotal']
    
    pdf.makePdf(tabela=tabela, cliente=cliente, valortotal=valortotal, contatos=contatos).start()
    
    
    return jsonify(message='Pdf Gerado')

if __name__ == '__main__':
    app.run(debug=True)
