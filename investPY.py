# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:18:16 2020

@author: aserpa
"""

import investpy
import pandas
from datetime import date, timedelta

#Pega a lista de acoes
#stocks = investpy.get_stocks_list()



#Variaveis usadas
vAcaoLista = ['petr4','vale3', 'goll4', 'azul4']
vPais = 'brazil'
DataIni = '01/01/2020'
DataFim = date.today()-timedelta(days=1) #Data de ontem
DataFim = DataFim.strftime('%d/%m/%Y')
DataFim = str(DataFim)


#Cria o dicionario
dfs = {}

#Para cada acao na variavel, executa abaixo
for vAcao in vAcaoLista:

    #Pega o Historico das acoes
    df = investpy.get_stock_historical_data(stock=vAcao, country=vPais, from_date=DataIni, to_date=DataFim, as_json=False, order='ascending')
    
    #Reinicia o index para normalizar o Dataframe
    df = df.reset_index()
    
    
    #Funcao para trocar o ponto por virgula
    def Normaliza_Valor(nvlr_str):
        return str(nvlr_str.replace(".",","))
    
    #Cria colunas novas usando a função acima, para que o PowerBI reconheca os valores
    df['OpenA'] = df['Open'].astype(str).apply(Normaliza_Valor)
    df['HighA'] = df['High'].astype(str).apply(Normaliza_Valor)
    df['LowA'] = df['Low'].astype(str).apply(Normaliza_Valor)
    df['CloseA'] = df['Close'].astype(str).apply(Normaliza_Valor)
    
    #Cria a coluna com o nome da ação
    df['Acao'] = vAcao
    
    #Cria a entrada variavel no dicionario
    dfs['df_'+vAcao] = df
    

#Cria a lista 
vAcaoFimLista = []

#Para cada entrada dinamica criada no Dicionário, adiciona na lista
for i in dfs.keys(): 
    print(i)
    vAcaoFimLista.append(dfs[i])
    #df_acoes = pandas.DataFrame().append(dfs[i], ignore_index=False)

#Concatena os dados da lista em um unico dataframe
df_acoes = pandas.concat(vAcaoFimLista)

#PRint
print(df_acoes)












