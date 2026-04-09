import requests
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2026-03-23"},
)
dados = resp.json()
df = pd.DataFrame(dados)
maximo = df["roe"].max()
filtro = df["roe"]== maximo 
df[filtro]



import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
params = {"ticker": "MNPR3", "data_ini": "2025-03-21", "data_fim": "2026-03-23"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params, 
)

dados = resp.json()
df_preco = pd.DataFrame(dados)
filtro1 = df_preco["data"]=="2026-03-23"
preco_final = df_preco.loc[filtro1, 'fechamento'].iloc[0]
preco_final = float (preco_final)
filtro2 = df_preco["data"]== "2025-03-21"
precos_inicial = df_preco.loc[filtro2, 'fechamento'].iloc[0]
precos_inicial = float(precos_inicial)
preco_final/precos_inicial - 1 


#API para pegar o Ibov
import yfinance as yf
#Get ticker data
ibov = yf.download("^BVSP", start="2001-01-01", end= "2026-03-26")
filtro1 = ibov.index == "2025-03-21"
ibov_ini = ibov[filtro1]["Close"].iloc[0]
filtro2 = ibov.index == "2026-03-23"
ibov_fim = ibov [filtro2]["Close"].iloc[0]
ibov_fim/ibov_ini - 1





import requests
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2021-04-01"},
)
dados = resp.json()
df = pd.DataFrame(dados)
df2 = df[["ticker", "roic", "earning_yield"]]
df2['rank_roic'] = df2 ['roic'].rank(ascending=False)
df2['rank_p_ey'] = df2['earning_yield'].rank(ascending=False)
df2["rank_final"] = (df2['rank_roic'] + df2['rank_p_ey']) / 2
carteira = df2.sort_values("rank_final", ascending=False)['ticker'][:20]  

#API para pegar os precos das acoes
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
params = {"ticker" : "BBSE3", "data_ini" : "2001-01-01", "data_fim": "2026-03-31"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params = params,
)
dados = resp.json()
df_preco = pd.DataFrame(dados)
#Preco final``
filtro1 = df_preco["data"] == "2026-03-31"
preco_final = df_preco.loc[filtro1, 'fechamento'].iloc[0]
preco_final = float(preco_final)
#Filtro inicial
filtro2 = df_preco["data"] == "2021-04-01"
precos_inicial = df_preco.loc[filtro2, 'fechamento'].iloc[0]
precos_inicial = float(precos_inicial)
preco_final/precos_inicial - 1


# 5 anos 
# preco final
filtro1 = df_preco["data"]=="2026-03-23"
preco_final = df_preco.loc[filtro1, 'fechamento'].iloc[0]
preco_final = float(preco_final)
#Filtro Inicial
filtro2 = df_preco["data"]=="2021-03-22"
precos_inicial = df_preco.loc[filtro2, 'fechamento'].iloc[0]
precos_inicial = float(precos_inicial)
preco_final/precos_inicial - 1

#API para pegar o Ibov
import yfinance as yf
#Get ticker data
ibov = yf.download("^BVSP", start="2001-01-01", end= "2026-04-01")
filtro1 = ibov.index == "2021-04-01"
ibov_ini = ibov[filtro1]["Close"].iloc[0]
filtro2 = ibov.index == "2026-03-31"
ibov_fim = ibov [filtro2]["Close"].iloc[0]
ibov_fim/ibov_ini - 1

##
data_ini = "2021-04-01"
data_fim = "2026-03-30"

carteira

retornos = []
for ticker in carteira:
    try:
        resp = requests.get(
            f"{base_url}/preco/corrigido",
            headers={"Authorization": f"Bearer {token}"},
            params={"ticker": ticker, "data_ini": data_ini, "data_fim": data_fim},
        )
        df_preco = pd.DataFrame(resp.json())
        if df_preco.empty or len(df_preco) < 2:
            print(f"  Sem dados: {ticker}")
            continue
        preco_ini = float(df_preco["fechamento"].iloc[0])
        preco_fim = float(df_preco["fechamento"].iloc[-1])
        retorno = (preco_fim / preco_ini - 1) * 100
        retornos.append({"ticker": ticker, "retorno_5Y_%": round(retorno, 2)})
    except Exception as e:
        print(f"  Erro {ticker}: {e}")

df_ret = pd.DataFrame(retornos).sort_values("retorno_5Y_%", ascending=False)

retornos

# Ibovespa no mesmo período

ibov = yf.download("^BVSP", start=data_ini, end=data_fim, auto_adjust=True, progress=False)
close = ibov["Close"].squeeze()  # resolve o MultiIndex
ret_ibov = (float(close.iloc[-1]) / float(close.iloc[0]) - 1) * 100

df_ret["peso"] = 0.05  # 20 ações × 5% = 100%
ret_carteira = (df_ret["retorno_5Y_%"] * df_ret["peso"]).sum()

print(df_ret.to_string(index=False))
print(f"\nRetorno médio carteira : {ret_carteira:.2f}%")
print(f"Retorno Ibovespa       : {ret_ibov:.2f}%")
print(f"Alpha                  : {ret_carteira - ret_ibov:.2f}%")


    

   

