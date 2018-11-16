import pandas as pd

df = pd.read_csv('buscas.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

Xdummies = pd.get_dummies(x_df)
Ydummies = y_df

x = Xdummies.values;
y = Ydummies.values;

print(y)
