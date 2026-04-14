# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento
# Questões:
# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 

import pandas as pd 
df = pd.read_csv("ncr_ride_bookings.csv")
resultado = df.groupby("Completed")
print(resultado)

# (0,5) 2 - Qual a proporção em relação ao total de corridas?


# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.
import pandas as pd
df = pd.read_csv("ncr_ride_bookings.csv")
resultado = df.groupby("Ride Distance")["Vehicle Type"].agg([
    "median",
    
])
print(resultado)

# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?
import pandas as pd 
df = pd.read_csv("ncr_ride_bookings.csv")
resultado = df.groupby("Payment Method")["Bike"].agg([
    "max"
])

# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?


# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?



# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;
import requests 
import pandas as pd
url ="http://www.ipeadata.gov.br/api/odata4/Metadados"
response = requests.get(url)
dados = response.json()
df = pd.DataFrame(dados)

dados = response.json()
df = pd.DataFrame(dados)
filtro = (df["FNTSIGLA"] == "serie da Fipe") & (df["SERNOME"] == "vendas - Brasil")
df_filtrado = df[filtro]

print(df_filtrado)

# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO=''
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.
import requests
import pandas as pd 


# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )

import requests
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
params = {"ticker": "VALE3", "data_ini": "2025-01-01", "data_fim": "2025-12-31"}
response = requests.get(
   f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)

dados = response.json()
df_preco = pd.DataFrame(dados)
filtro1 = df_preco["data"]=="2025-12-31"
preco_final = df_preco.loc[filtro1, 'fechamento'].iloc[0]
preco_final = float (preco_final)
filtro2 = df_preco["data"]== "2025-01-01"
precos_inicial = df_preco.loc[filtro2, 'fechamento'].iloc[0]
precos_inicial = float(precos_inicial)
preco_final/precos_inicial - 1 



# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

import requests 
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
response = requests.get(
     f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2024-04-01"},
 )
dados = response.json()
df = pd.DataFrame(dados)
maximo = df["roe"].max()
filtro1 = df["roe"]== maximo 
df[filtro1]

dados = response.json()
df_ = pd.DataFrame(dados)
setor = df["setor"]
filtro2 = df["setor"] == "tecnologia"
df[filtro2]

df = df.drop(columns=["ano_tri"]["preco"]["upside"]["upside_tri"]["roc"]["roc_tri"])

# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )
import requests
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
response = requests.get(
     f"{base_url}/bolsa/planilhao",
     headers={"Authorization": f"Bearer {token}"},
     params={"data_base": "2024-04-01"},
 )
dados = response.json()
df = pd.DataFrame(dados)
df2 = df[["ticker", "roc", "earning_yield"]]
df2['rank_roc'] = df2 ['roc'].rank(ascending=False)
df2['rank_p_ey'] = df2['earning_yield'].rank(ascending=False)
df2["rank_final"] = (df2['rank_roc'] + df2['rank_p_ey']) / 2
carteira = df2.sort_values("rank_final", ascending=False)['ticker'][:10] 

# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?
import pandas as pd
dados = response.json()
df_ = pd.DataFrame(dados)
setor = df["setor"]
filtro2 = df["setor"] 
df[filtro2]
