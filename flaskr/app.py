from flask import Flask, render_template, request, redirect, url_for
from core import organizar_infos
from core.pdfmaker import pdf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        dados = request.form.to_dict()
        
        infos = organizar_infos.start(dados)
        
        tabela = infos['tabela']
        cliente = infos['nomeCliente']
        valortotal = infos['valorTotal']
        print(infos)
        
        pdf.make_pdf(tabela, cliente, valortotal)
        
        
        return redirect(url_for('success'))

    return render_template('base.html')

@app.route('/success')
def success():
    return "Formulário enviado com sucesso!"

@app.route('/teste')
def teste():
    return render_template('teste.html')


if __name__ == '__main__':
    app.run(debug=True)
