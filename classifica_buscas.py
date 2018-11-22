import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from collections import Counter

df = pd.read_csv('buscas.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

Xdummies = pd.get_dummies(x_df)
Ydummies = y_df

x = Xdummies.values;
y = Ydummies.values;

#eficacia do algoritimo que responde so um valor 0 ou 1, depende que qual aparecer mais no csv
taxa_de_acerto_base = 100.0 * max(Counter(y).itervalues()) / len(y)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)

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

diferencas = sum(resultado == teste_marcacoes)
acertos = resultado == teste_marcacoes

total_de_acertos = sum(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print("Taxa de acerto do algoritmo: %f" % taxa_de_acerto)
print(total_de_elementos)
