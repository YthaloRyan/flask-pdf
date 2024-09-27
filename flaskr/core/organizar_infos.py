import locale

def formatar_preco(preco):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    if not preco:
        return ''
    
    
    
    
    
    preco = float(preco.replace(',', '.'))
    print(preco)
    
    valor_formatado = locale.currency(preco, grouping=True).replace('R$ ', '')
    
    return valor_formatado

def formatar_data(data):
    data = data.split('-')
    
    return '/'.join(data[::-1])

def start(infos):
    infos_organizadas = {'tabela': []}
    tabela_temporaria = {}
    
    
    infos_organizadas['nomeCliente'] = infos['nomeCliente']
    infos_organizadas['valorTotal'] = infos['valorTotal']
    del infos['nomeCliente']
    del infos['valorTotal']
    
    
    for info in infos:
        id = ''.join((i for i in info if i.isdigit() ))
        
        if infos[info] == '0,00':
            infos[info] = ''  
        
        
            
        if 'data' in info:
            infos[info] = formatar_data(infos[info])
        
          
            
        if id in tabela_temporaria:
            tabela_temporaria[id].append(infos[info])
    
        else:
            tabela_temporaria[id] = [infos[info]]
        
    for id in tabela_temporaria:
        infos_organizadas['tabela'].append(tabela_temporaria[id])
    
    
    return infos_organizadas