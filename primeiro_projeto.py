# -*- coding: utf-8 -*-
"""Primeiro projeto

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sc3Fu_GnoxAFHCeyWhwvrCHrePevuBbs

Passo a passo para a solução do **desafio**
"""

# Passo 0 - Entender o desafio que voce quer resolver

# Passo 1 - Percorrer todos os arquivos da base de dados (pasta vendas)

import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir("/content/drive/MyDrive/Curso basico Python/Vendas")
display(lista_arquivo)

tabela_total = pd.DataFrame()

# Passo 2 - Importar as bases de dados de vendas

for arquivos in lista_arquivo:
  # se tem "Vendas" no nome do arquivo, então
  if "Vendas" in arquivos:
    # importar o arquivo
    tabela = pd.read_csv(f"/content/drive/MyDrive/Curso basico Python/Vendas/{arquivos}")
    tabela_total = tabela_total.append(tabela)

# Passo 3 - Tratar / Compilar as bases de dados

display(tabela)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
display(tabela_faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
display(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()