# Classificador Random Forest 
Utilizando RandomForestClassifier() numa base de dados real para classificar registros(Censo de 1994 - EUA).
Objetivo: Prever se um americano possui renda anual <= ou > 50 mil dólares por ano.

Base Line Classifier = 0.7559 (ZeroR)

### Resultados - Validação Cruzada - StratifiedKFold
**Precisão** | **Pré-Processamentos** | **Desvio Padrão**
| :------: | :------: | :------: |
**0.8549** | **LabelEncoder** | **0.0047**
0.8532 | OneHotEncoder | 0.0059
0.8547 | LabelEncoder + StandardScaler | 0.0047
0.8535 | OneHotEncoder + StandardScaler | 0.0058
0.8535 | LabelEnconder + OneHotEncoder + StandardScaler | 0.0058

### Matriz de Confusão (Média):
x | **0** | **1**
| :------: | :------: | :------: |
0 | **2299.1** | 172.9
1 | 299.5 | **484.6**

A Matriz na tabela acima é formada pela média de todas as matrizes geradas ao longo de 10 execuções usando pré-processamentos LabelEncoder.

A diagonal principal (em negrito) destaca os registros classificados corretamente.

### Bibliotecas usadas:
- Pandas
- Sklearn
- Numpy

### Técnicas de Pré-Processamento e Tratamento dos dados usada:
- LabelEnconder;
- OneHotEncoder;
- StandardScaler;

### Ferramentas Usadas:
- Anaconda
- Spyder

### Linguagem:
- Python

### Fonte da Base de Dados: 
- Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

### Como usar:
- Basta fazer o download do código fonte e da base de dados. Para executar o código por partes(células) e testar diferentes possibilidades de pré-processamento, recomendo uma IDE como Spyder ou o Jupyter. (Támbem é necessário ter o Python instalado no seu computador)

#### Outros Classificadores:
- [Naive Bayes](https://github.com/juliomrodrigues/Classificador-Naive-Bayes)
- [Árvore de Decisão](https://github.com/juliomrodrigues/Arvore-de-Decisao)
- [Aprendizagem por Regras](https://github.com/juliomrodrigues/Classificador-Regras)
- [Aprendizagem por Instâncias(KNN)](https://github.com/juliomrodrigues/Classificador-KNN)
- [Regressão Logística](https://github.com/juliomrodrigues/Regressao-Logistica-Classificador)
- [SVM](https://github.com/juliomrodrigues/Classificador-SVM)
- [Rede Neural](https://github.com/juliomrodrigues/Classificador-Rede-Neural)
