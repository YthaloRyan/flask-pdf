//Qs
const QsId = (el) => document.getElementById(el);

const coletarSubTo = (Id) => {
    var preco_nao_formatado = QsId(`subTo${Id}`).value;
    
    
    if (QsId(`subTo${Id}`).type == 'number') {
        preco_nao_formatado = Number(preco_nao_formatado).toLocaleString('pt-br', {minimumFractionDigits: 2});
    } 
    
    
    preco_nao_formatado = preco_nao_formatado.replace(/\D/g, ''); // remove tudo que não é dígito, fica então 2000099
    var preco =  parseFloat(preco_nao_formatado)/100; // 20000.99
    
    
    return preco;
}


function formatarParaNumero(valor) {
    // Remove os pontos e substitui a vírgula por ponto
    var string_valor = valor.replace(/\./g, '').replace(',', '.');

    var valor_formatado = Number(string_valor);

    return valor_formatado;
}


//Liga/Desliga somador automatico
const checarCheckbox = (Id) =>  {
    const checkbox = document.getElementById(`checkbox${Id}`);
    const isChecked = checkbox.checked;

    return isChecked;
}

const resetarCheckbox = (Id) => {
    const isChecked = checarCheckbox(Id);

    var subTo = QsId(`subTo${Id}`)

    if (isChecked) {
        subTo.readOnly = true;
        
        calcularSubTotal(Id);
    } else {
        subTo.readOnly = false;
        subTo.value = '';
        
    }
}


//Receber onclick Inputs [qtd, preco, subtotal]
const teclaAcionada = (Id) => {
    const isChecked = checarCheckbox(Id);
    
    if (!isChecked) {
        calcularTotal();
        return;
    }

    calcularSubTotal(Id);
}


//CalcularSubTotal
const calcularSubTotal = (Id) => {
    const quantidade = (QsId(`qtd${Id}`).value) || 0;
    var preco = (QsId(`preco${Id}`).value || '0');

    preco = formatarParaNumero(preco);

    var total = quantidade * preco;

    total = total.toLocaleString('pt-br', {minimumFractionDigits: 2});


    QsId(`subTo${Id}`).value = total;

    
    calcularTotal();
}


//Somar todos os subtotais
const calcularTotal = () => {
    const lista_subTo = document.querySelectorAll('#subToDiv');
    var range_subTo = lista_subTo.length;

    var total = 0;
    for (let i = 0; i < range_subTo; i++) {
        var preco = (QsId(`subTo${i}`).value || '0');
        preco = formatarParaNumero(preco);
        
        
        total = total + preco;
    }

    

    total = total.toLocaleString('pt-br', {minimumFractionDigits: 2});
    
    QsId('valorTotaltd').innerHTML = total;
    QsId('valorTotal').value = total;
}


//Coleta um value e transforma em dinheiro
function coletarNumero(Id) {
    var preco = (QsId(Id).value || '0');

    if (preco == '0') {
        return ''
    }
        
    preco = formatarParaNumero(preco);
    preco = preco.toLocaleString('pt-br', {minimumFractionDigits: 2});

    return preco
}

//formata todos os valores do input para dinheiro
function finalizarNumeros() {
    const lista_subTo = document.querySelectorAll('#subToDiv');
    var range_subTo = lista_subTo.length;
    

    for (let i = 0; i < range_subTo; i++) {
        QsId(`preco${i}`).value = coletarNumero(`preco${i}`);

        QsId(`subTo${i}`).value = coletarNumero(`subTo${i}`);
    }

    var iframe = document.getElementById('notaPdf');
    iframe.src = iframe.src;
}