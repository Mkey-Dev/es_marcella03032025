# Importação das bibliotecas necessárias
import streamlit as st  # Biblioteca para criar aplicativos web interativos
import pandas as pd  # Biblioteca para manipulação de dados
import plotly.express as px  # Biblioteca para criação de gráficos interativos
from scipy.stats import chi2_contingency  # Função para realizar o teste qui-quadrado
from statsmodels.formula.api import ols  # Função para realizar regressão linear
import numpy as np  # Biblioteca para operações numéricas

# Função para carregar os dados a partir de um arquivo Excel
def load_data():
    df = pd.read_excel("df.xls")  # Lê o arquivo Excel e armazena em um DataFrame
    return df  # Retorna o DataFrame carregado

# Carrega os dados chamando a função load_data
df = load_data()    

# Título do dashboard
st.title("Análise Estatística da Transportadora")  # Define o título do aplicativo web

# Sidebar para seleção de análises
st.sidebar.title("Selecione a Análise")  # Define o título da barra lateral
analysis = st.sidebar.selectbox(
    "Escolha a análise:",  # Texto do seletor
    ["Opinião dos Clientes", "Região de Destino", "Modalidade de Transporte", 
     "Peso das Encomendas", "Tempo de Entrega", "Associações e Correlações", 
     "Verificação de Metas"]  # Opções de análises disponíveis
)

# Análise 1: Opinião dos Clientes
if analysis == "Opinião dos Clientes":
    st.header("Opinião dos Clientes")  # Título da seção
    
    # Agrupar os dados e contar as ocorrências de cada opinião
    opiniao_counts = df["Opinião"].value_counts().reset_index()  # Conta as ocorrências de cada opinião
    opiniao_counts.columns = ["Opinião", "Contagem"]  # Renomear as colunas
    
    # Criar o gráfico de barras
    fig = px.bar(opiniao_counts, x="Opinião", y="Contagem", title="Distribuição da Opinião dos Clientes")
    
# Exibir o gráfico
    st.plotly_chart(fig)  # Mostra o gráfico no aplicativo

# Análise 2: Região de Destino
elif analysis == "Região de Destino":
    st.header("Região de Destino Principal")  # Título da seção
    
    # Agrupar os dados e contar as ocorrências de cada região
    regiao_counts = df["Região"].value_counts().reset_index()  # Conta as ocorrências de cada região
    regiao_counts.columns = ["Região", "Contagem"]  # Renomear as colunas
    
    # Criar o gráfico de barras
    fig = px.bar(regiao_counts, x="Região", y="Contagem", title="Distribuição das Regiões de Destino")
    
    # Exibir o gráfico
    st.plotly_chart(fig)  # Mostra o gráfico no aplicativo

# Análise 3: Modalidade de Transporte
elif analysis == "Modalidade de Transporte":
    st.header("Modalidade de Transporte")  # Título da seção
    modalidade_freq = df["Modalidade"].value_counts()  # Conta as ocorrências de cada modalidade
    fig = px.pie(modalidade_freq, values=modalidade_freq.values, names=modalidade_freq.index, 
                 title="Distribuição da Modalidade de Transporte")  # Cria um gráfico de pizza
    st.plotly_chart(fig)  # Mostra o gráfico no aplicativo

# Análise 4: Peso das Encomendas
elif analysis == "Peso das Encomendas":
    st.header("Análise Descritiva do Peso das Encomendas")  # Título da seção
    st.write(df["Peso"].describe())  # Exibe estatísticas descritivas da coluna "Peso"
    fig = px.histogram(df, x="Peso", nbins=30, title="Distribuição do Peso das Encomendas")  # Cria um histograma
    st.plotly_chart(fig)  # Mostra o gráfico no aplicativo
    # Comentários sobre as estatísticas descritivas:
    # count: Número de valores não nulos na coluna.
    # mean: Média dos valores.
    # std: Desvio padrão dos valores (medida de dispersão).
    # min: Valor mínimo.
    # 25%: Primeiro quartil (25% dos dados estão abaixo desse valor).
    # 50%: Mediana (50% dos dados estão abaixo desse valor).
    # 75%: Terceiro quartil (75% dos dados estão abaixo desse valor).
    # max: Valor máximo.

# Análise 5: Tempo de Entrega
elif analysis == "Tempo de Entrega":
    st.header("Análise Descritiva do Tempo de Entrega")  # Título da seção
    st.write(df["Tempo"].describe())  # Exibe estatísticas descritivas da coluna "Tempo"
    fig = px.histogram(df, x="Tempo", nbins=30, title="Distribuição do Tempo de Entrega")  # Cria um histograma
    st.plotly_chart(fig)  # Mostra o gráfico no aplicativo

# Análise 6: Associações e Correlações
elif analysis == "Associações e Correlações":
    st.header("Associações e Correlações")  # Título da seção

    #6
    # Modalidade de Transporte vs. Região de Destino
    st.subheader("Modalidade de Transporte vs. Região de Destino")
    tabela_contingencia = pd.crosstab(df["Modalidade"], df["Região"])  # Cria uma tabela de contingência
    st.write("Tabela de Contingência:")
    st.write(tabela_contingencia)  # Exibe a tabela

    # Gráfico de barras agrupadas
    fig = px.bar(tabela_contingencia, barmode="group", title="Modalidade de Transporte por Região de Destino")
    st.plotly_chart(fig)

    #7  Modalidade de Transporte vs. Opinião do Cliente
    st.subheader("Modalidade de Transporte vs. Opinião do Cliente")
    tabela_opiniao_modalidade = pd.crosstab(df["Modalidade"], df["Opinião"])  # Cria uma tabela de contingência
    st.write("Tabela de Contingência:")
    st.write(tabela_opiniao_modalidade)  # Exibe a tabela

    # Gráfico de barras agrupadas
    fig = px.bar(tabela_opiniao_modalidade, barmode="group", title="Modalidade de Transporte por Opinião do Cliente")
    st.plotly_chart(fig)

    #8 Região de Destino vs. Opinião do Cliente
    st.subheader("Região de Destino vs. Opinião do Cliente")
    tabela_opiniao_regiao = pd.crosstab(df["Região"], df["Opinião"])  # Cria uma tabela de contingência
    st.write("Tabela de Contingência:")
    st.write(tabela_opiniao_regiao)  # Exibe a tabela

    # Gráfico de barras agrupadas
    fig = px.bar(tabela_opiniao_regiao, barmode="group", title="Região de Destino por Opinião do Cliente")
    st.plotly_chart(fig)

    #9 Opinião do Cliente vs. Tempo de Entrega
    st.subheader("Opinião do Cliente vs. Tempo de Entrega")
    fig = px.box(df, x="Opinião", y="Tempo", title="Distribuição do Tempo de Entrega por Opinião do Cliente")
    st.plotly_chart(fig)

    # Regressão Linear
    model = ols('Tempo ~ C(Opinião)', data=df).fit()  # Realiza uma regressão linear
    st.write("Resumo do Modelo de Regressão:")
    st.write(model.summary())  # Exibe o resumo do modelo de regressão

    
    #10 Região de Destino vs. Tempo de Entrega
    st.subheader("Região de Destino vs. Tempo de Entrega")
    fig = px.scatter(df, x="Região", y="Tempo", color="Região", title="Tempo de Entrega por Região de Destino")
    st.plotly_chart(fig)

    # Regressão Linear
    model = ols('Tempo ~ C(Região)', data=df).fit()  # Realiza uma regressão linear
    st.write("Resumo do Modelo de Regressão:")
    st.write(model.summary())  # Exibe o resumo do modelo de regressão

    # Peso da Encomenda vs. Tempo de Entrega com cores por Opinião do Cliente
    st.subheader("Peso da Encomenda vs. Tempo de Entrega")
    corr = df["Peso"].corr(df["Tempo"])  # Calcula a correlação entre Peso e Tempo
    st.write(f"Correlação: {corr:.2f}")  # Exibe o valor da correlação

    # Gráfico de dispersão com cores baseadas na coluna "Opinião"
    fig = px.scatter(df, x="Peso", y="Tempo", color="Opinião", trendline="ols", 
                 title="Relação entre Peso e Tempo de Entrega (Cores por Opinião do Cliente)")
    st.plotly_chart(fig)  # Mostra o gráfico no aplicativo




# Análise 7: Verificação de Metas
elif analysis == "Verificação de Metas":
    st.header("Verificação de Metas da Empresa")  # Título da seção

    # Porcentagem de encomendas abaixo de 800 kg
    percentagem_menos_800 = (df["Peso"] < 800).mean() * 100  # Calcula a porcentagem de encomendas abaixo de 800 kg
    st.write(f"Porcentagem de encomendas abaixo de 800 kg: {percentagem_menos_800:.2f}%")  # Exibe a porcentagem

    # Porcentagem de encomendas entregues em até 80 horas
    percentagem_80_horas = (df["Tempo"] <= 80).mean() * 100  # Calcula a porcentagem de encomendas entregues em até 80 horas
    st.write(f"Porcentagem de encomendas entregues em até 80 horas: {percentagem_80_horas:.2f}%")  # Exibe a porcentagem

    # Porcentagem de transporte rodoviário
    percentagem_rodoviario = (df["Modalidade"] == "Rodoviário").mean() * 100  # Calcula a porcentagem de transporte rodoviário
    st.write(f"Porcentagem de transporte rodoviário: {percentagem_rodoviario:.2f}%")  # Exibe a porcentagem

    # Tabela de opiniões por região
    tabela_opiniao_regiao = pd.crosstab(df["Região"], df["Opinião"], normalize='index') * 100  # Cria uma tabela de contingência normalizada
    st.write("Porcentagem de opiniões por região:")  # Exibe o título da tabela
    st.write(tabela_opiniao_regiao)  # Exibe a tabela