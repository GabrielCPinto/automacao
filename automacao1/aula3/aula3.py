import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


table = pd.read_csv('aula3\\clientes.csv')
col = ['id_cliente','score_credito']

encoder = LabelEncoder()

table['profissao'] = encoder.fit_transform(table['profissao'])
table['mix_credito'] = encoder.fit_transform(table['mix_credito'])
table['comportamento_pagamento'] = encoder.fit_transform(table['comportamento_pagamento'])
y = table['score_credito']
x = table.drop(columns = col)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()
modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste.to_numpy())

print(accuracy_score(y_teste, previsao_arvoredecisao))
print(accuracy_score(y_teste, previsao_knn))