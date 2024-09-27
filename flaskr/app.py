from flask import Flask, render_template, request, redirect, url_for
from core import organizar_infos
from core.pdfmaker import pdf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        dados = request.form.to_dict()
        
        print(dados)
        
        
        infos = organizar_infos.start(dados)
        
        tabela = infos['tabela']
        cliente = infos['nomeCliente']
        valortotal = infos['valorTotal']
        
        pdf_path = url_for('static', 'nota.pdf')
        
        print(pdf_path)
        
        
        canvas = pdf.make_pdf(tabela, cliente, valortotal, pdf_file=pdf_path)
        
        canvas.save()
        
        
        

    return render_template('base.html')

@app.route('/success')
def success():
    return "Formulário enviado com sucesso!"

@app.route('/teste')
def teste():
    return render_template('teste.html')


if __name__ == '__main__':
    app.run(debug=True)
