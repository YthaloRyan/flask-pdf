from flask import Flask, render_template, request, redirect, url_for, jsonify
from core import organizar_infos
from core.pdfmaker import pdf

import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form_():
    if request.method == 'POST':
        dados = request.form.to_dict()
        
        print(dados)
        
        
        infos = organizar_infos.start(dados)
        
        tabela = infos['tabela']
        cliente = infos['nomeCliente']
        valortotal = infos['valorTotal']
        
        pdf_path = './static/nota.pdf'
        
        print(pdf_path)
        
        
        canvas = pdf.make_pdf(tabela=tabela, cliente=cliente, valortotal=valortotal, pdf_file=pdf_path)
        
        canvas.save()
        
    
    else:
    
        return render_template('base.html')
        
    
@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        dados = request.form.to_dict()
        
        print(dados)
        
        
        infos = organizar_infos.start(dados)
        
        tabela = infos['tabela']
        cliente = infos['nomeCliente']
        valortotal = infos['valorTotal']
        
        pdf_path = './static/nota.pdf'
        
        print(pdf_path)
        
        
        canvas = pdf.make_pdf(tabela=tabela, cliente=cliente, valortotal=valortotal, pdf_file=pdf_path)
        
        canvas.save()
        

    return None
        

    

@app.route('/success')
def success():
    return "Formulário enviado com sucesso!"

@app.route('/teste')
def teste():
    return render_template('teste.html')




# testes ajax
@app.route('/ajax')
def form():
    return render_template('form_ajax.html')

@app.route('/submit_ajax', methods=['POST'])
def submit_ajax():
    data = request.get_json()  # Recebe os dados enviados como JSON
    name = data.get('name')
    email = data.get('email')
    
    # Processa os dados (aqui só estamos retornando uma mensagem)
    response_message = f"Received: Name = {name}, Email = {email}"
    
    print(data)
    
    # Retorna uma resposta em JSON
    return jsonify(message='opa')


if __name__ == '__main__':
    app.run(debug=True)
