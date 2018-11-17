import pandas as pd
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('buscas.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

Xdummies = pd.get_dummies(x_df)
Ydummies = y_df

x = Xdummies.values;
y = Ydummies.values;

portcentagem_de_treino = 0.9
tamanho_de_treino = int(portcentagem_de_treino * len(y))
tamanho_de_teste = int(len(y) - tamanho_de_treino)

treino_dados = x[:tamanho_de_treino]
treino_marcacoes = y[:tamanho_de_treino]

teste_dados = x[-tamanho_de_teste:]
teste_marcacoes = y[-tamanho_de_teste:]

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
print resultado

diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

# quantas vezes eu acertei ?
print taxa_de_acerto

# print(y)
