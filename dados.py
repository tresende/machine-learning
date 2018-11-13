import csv

def carregar_acessos():
    X = []
    Y = []
    arquivo = open('acesso.csv', 'rb')
    leitor = csv.reader(arquivo)
    leitor.next()
    for home,como_funciona,contato, comprou in leitor:
        dado = [int(home), int(como_funciona) ,int(contato)]
        X.append(dado)
        Y.append(int(comprou))
    return X, Y