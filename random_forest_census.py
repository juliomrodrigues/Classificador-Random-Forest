# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 23:17:02 2021

Base de Dados: Dua, D. and Graff, C. (2019). UCI Machine Learning Repository 
[http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School 
of Information and Computer Science.
"""

import pandas
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
 
base = pandas.read_csv('census.csv')
 
atributos = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values

# Transformando variaveis categóricas(Strings) em números
label_encoder= LabelEncoder()
atributos[:, 1] = label_encoder.fit_transform(atributos[:, 1])
atributos[:, 3] = label_encoder.fit_transform(atributos[:, 3])
atributos[:, 5] = label_encoder.fit_transform(atributos[:, 5])
atributos[:, 6] = label_encoder.fit_transform(atributos[:, 6])
atributos[:, 7] = label_encoder.fit_transform(atributos[:, 7])
atributos[:, 8] = label_encoder.fit_transform(atributos[:, 8])
atributos[:, 9] = label_encoder.fit_transform(atributos[:, 9])
atributos[:, 13] = label_encoder.fit_transform(atributos[:, 13])
classe = label_encoder.fit_transform(classe)

# OPCIONAL : USANDO COLUMNTRANSFORMER
'''
one_hot_encoder = OneHotEncoder()
column_tranformer = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [1, 3, 5, 6, 7, 8, 9, 13])],remainder='passthrough')
atributos = column_tranformer.fit_transform(atributos).toarray()
'''

#Aplicando escalonamento nos valores
#scaler = StandardScaler()
#atributos = scaler.fit_transform(atributos)
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(atributos, classe, test_size=0.15, random_state=0)


classificador = RandomForestClassifier(n_estimators=40, criterion= 'entropy', random_state = 0)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

# Calculando a precisão e gerando matriz de confusão
taxa_precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)


print(f'A taxa de precisão alcançada foi de aproximadamente{round(taxa_precisao*100)}%')