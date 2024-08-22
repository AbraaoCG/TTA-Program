#from iexfinance.stocks import Stock,get_historical_data
# from iexfinance.refdata import get_symbols
# from iexfinance.utils.exceptions import IEXQueryError

import requests
import pandas as pd
import yfinance as yf

keyBrAPI = '5BEDTGPVVSgTJvPYMQ4FCy'
keyIEX = 'sk_3aa29dbc1b574efe9c4aa9cb2b81a011'


# -------------------BrAPI-------------------
# url = "https://brapi.dev/api/available"
# params = {
#     'search': 'TR',
#     'token': keyBrAPI,
# }

# response = requests.get(url, params=params)
 
# if response.status_code == 200:
#     data = response.json()
#     print(len(data))
# else:
#     print(f"Request failed with status code {response.status_code}")


#-------------------IEXFinance-------------------
# try:
#     # Obtendo a lista de símbolos disponíveis
#     symbols = get_symbols(token=keyIEX)

#     # Exibindo os primeiros 5 tokens como exemplo
#     for symbol in symbols[:5]:
#         print(f"Símbolo: {symbol['symbol']}, Nome: {symbol['name']}, Tipo: {symbol['type']}")
# except IEXQueryError as e:
#     print(f"Erro ao acessar a API: {e}")

# -------------------Yahoo Finance-------------------

# # Obtendo informações sobre os componentes do S&P 500
# sp500 = yf.Ticker("^GSPC")
# sp500_constituents = sp500.history(period="1d").index.tolist()

# # Para fins de exemplo, vamos buscar informações sobre alguns símbolos
# symbols = ["AAPL", "MSFT", "AMZN", "GOOG", "FB"]

# # Exibindo informações básicas dos símbolos
# for symbol in symbols:
#     ticker = yf.Ticker(symbol)
#     info = ticker.info
#     print(f"Símbolo: {symbol}, Nome: {info['longName']}, Setor: {info.get('sector', 'N/A')}")

tokens_list = [
    "AMER3", "CVCB3", "COGN3", "B3SA3", "HAPV3", "PETR4", "PETZ3", "BBDC4", "RAIZ4", "USIM5",
    "ABEV3", "VALE3", "LREN3", "BBAS3", "MGLU3", "ITSA4", "CMIN3", "CMIG4", "AZUL4", "CIEL3",
    "ASAI3", "PCAR3", "GGBR4", "ITUB4", "RADL3", "CPLE6", "IFCM3", "NTCO3", "RAIL3", "CRFB3",
    "RDOR3", "POMO4", "CSAN3", "BEEF3", "CSNA3", "PETR3", "MRVE3", "GOAU4", "JBSS3", "VAMO3",
    "FLRY3", "VBBR3", "PRIO3", "EQTL3", "ELET3", "CCRO3", "RENT3", "UGPA3", "CYRE3", "BRFS3",
    "LWSA3", "BBDC3", "MRFG3", "GOLL4", "ENEV3", "GFSA3", "MOVI3", "SUZB3", "ANIM3", "WEGE3",
    "TIMS3", "AURE3", "QUAL3", "EMBR3", "ALOS3", "CPLE3", "CBAV3", "RRRP3", "BBSE3", "DXCO3",
    "BHIA3", "MLAS3", "MELK3", "STBP3", "BRAP4", "CEAB3", "VIVA3", "MULT3", "TRPL4", "HBSA3",
    "SIMH3", "SMFT3", "YDUQ3", "LJQQ3", "JHSF3", "TOTS3", "ECOR3", "RAPT4", "CXSE3", "GGPS3",
    "ONCO3", "BPAN4", "HYPE3", "BRKM5", "AESB3", "SBSP3", "LIGT3", "VIVT3", "AZEV4", "SEQL3",
    "KLBN4", "ALPA4", "FRAS3", "IRBR3", "SRNA3", "SYNE3", "VVEO3", "NGRD3", "CURY3", "SLCE3",
    "SBFG3", "PRNR3", "MBLY3", "GMAT3", "JFEN3", "ODPV3", "CSED3", "TEND3", "TTEN3", "ELET6",
    "RCSL3", "EGIE3", "EZTC3", "KRSA3", "CPFE3", "NEOE3", "SMTO3", "RECV3", "PSSA3", "SAPR4",
    "POSI3", "CLSA3", "RANI3", "CASH3", "AZZA3", "PGMN3", "PLPL3", "BRIT3", "PTBL3", "CSMG3",
    "TASA4", "DIRR3", "WIZC3", "DASA3", "MEAL3", "GUAR3", "EVEN3", "GRND3", "OIBR3", "LOGG3",
    "KEPL3", "MDIA3", "FIQE3", "MTRE3", "BRSR6", "OPCT3", "ENJU3", "SOJA3", "MATD3", "AMAR3",
    "BMGB4", "PDGR3", "MILS3", "ESPA3", "MYPK3", "FESA4", "TECN3", "SEER3", "LEVE3", "VULC3",
    "RCSL4", "SHOW3", "ORVR3", "TRIS3", "HBOR3", "AMBP3", "USIM3", "INTB3", "TUPY3", "CAML3",
    "JALL3", "EALT3", "ZAMP3", "AZEV3", "LUPA3", "VITT3", "VLID3", "ABCB4", "ETER3", "LAVV3",
    "ITUB3", "PNVL3", "PFRM3", "BLAU3", "TRAD3", "KLBN3", "ALPK3", "DESK3", "INEP3", "RNEW4",
    "JSLG3", "MDNE3", "ARML3", "UNIP6", "BMOB3", "AGXY3", "SHUL4", "PMAM3", "BRAP3", "PINE4",
    "AERI3", "ROMI3", "AGRO3", "INEP4", "HBRE3", "DMVF3", "ITSA3", "DEXP3", "BIOM3", "TGMA3",
    "LPSB3", "PORT3", "SAPR3", "RNEW3", "TAEE4", "TCSA3", "ELMD3", "CMIG3", "SANB4", "GGBR3",
    "AALR3", "POMO3", "RAPT3", "SANB3", "ALPA3", "TFCO4", "ATMP3", "TAEE3", "TPIS3", "RSID3",
    "ALLD3", "CSUD3", "EALT4", "GOAU3", "TASA3", "VIVR3", "EUCA4", "CTSA4", "UCAS3", "LAND3",
    "VTRU3", "BOBR4", "HAGA4", "PINE11", "CSRN3", "DOTZ3", "CEBR5"
]

# # Teste de validade de tokens na Yahoo Finance
# codes = tokens_list.copy()
# valid_symbols = []

# for code in codes:
#     symbol = f"{code}.SA"
#     ticker = yf.Ticker(symbol)
#     try:
#         if 'shortName' in ticker.info:
#             valid_symbols.append(symbol)
#             print(f"Válido: {symbol}")
#     except:
#         print(f"Inválido: {symbol}")

# print("Símbolos válidos:", valid_symbols)

yf_symbols = ['AMER3.SA', 'CVCB3.SA', 'COGN3.SA', 'B3SA3.SA', 'HAPV3.SA', 'PETR4.SA', 'PETZ3.SA', 'BBDC4.SA', 'RAIZ4.SA', 'USIM5.SA', 'ABEV3.SA', 'VALE3.SA', 'LREN3.SA', 'BBAS3.SA', 'MGLU3.SA', 'ITSA4.SA', 'CMIN3.SA', 'CMIG4.SA', 'AZUL4.SA', 'CIEL3.SA', 'ASAI3.SA', 'PCAR3.SA', 'GGBR4.SA', 'ITUB4.SA', 'RADL3.SA', 'CPLE6.SA', 'IFCM3.SA', 'NTCO3.SA', 'RAIL3.SA', 'CRFB3.SA', 'RDOR3.SA', 'POMO4.SA', 'CSAN3.SA', 'BEEF3.SA', 'CSNA3.SA', 'PETR3.SA', 'MRVE3.SA', 'GOAU4.SA', 'JBSS3.SA', 'VAMO3.SA', 'FLRY3.SA', 'VBBR3.SA', 'PRIO3.SA', 'EQTL3.SA', 'ELET3.SA', 'CCRO3.SA', 'RENT3.SA', 'UGPA3.SA', 'CYRE3.SA', 'BRFS3.SA', 'LWSA3.SA', 'BBDC3.SA', 'MRFG3.SA', 'GOLL4.SA', 'ENEV3.SA', 'GFSA3.SA', 'MOVI3.SA', 'SUZB3.SA', 'ANIM3.SA', 'WEGE3.SA', 'TIMS3.SA', 'AURE3.SA', 'QUAL3.SA', 'EMBR3.SA', 'ALOS3.SA', 'CPLE3.SA', 'CBAV3.SA', 'RRRP3.SA', 'BBSE3.SA', 'DXCO3.SA', 'BHIA3.SA', 'MLAS3.SA', 'MELK3.SA', 'STBP3.SA', 'BRAP4.SA', 'CEAB3.SA', 'VIVA3.SA', 'MULT3.SA', 'TRPL4.SA', 'HBSA3.SA', 'SIMH3.SA', 'SMFT3.SA', 'YDUQ3.SA', 'LJQQ3.SA', 'JHSF3.SA', 'TOTS3.SA', 'ECOR3.SA', 'RAPT4.SA', 'CXSE3.SA', 'GGPS3.SA', 'ONCO3.SA', 'BPAN4.SA', 'HYPE3.SA', 'BRKM5.SA', 'AESB3.SA', 'SBSP3.SA', 'LIGT3.SA', 'VIVT3.SA', 'AZEV4.SA', 'SEQL3.SA', 'KLBN4.SA', 'ALPA4.SA', 'FRAS3.SA', 'IRBR3.SA', 'SRNA3.SA', 'SYNE3.SA', 'VVEO3.SA', 'NGRD3.SA', 'CURY3.SA', 'SLCE3.SA', 'SBFG3.SA', 'PRNR3.SA', 'MBLY3.SA', 'GMAT3.SA', 'JFEN3.SA', 'ODPV3.SA', 'CSED3.SA', 'TEND3.SA', 'TTEN3.SA', 'ELET6.SA', 'RCSL3.SA', 'EGIE3.SA', 'EZTC3.SA', 'KRSA3.SA', 'CPFE3.SA', 'NEOE3.SA', 'SMTO3.SA', 'RECV3.SA', 'PSSA3.SA', 'SAPR4.SA', 'POSI3.SA', 'CLSA3.SA', 'RANI3.SA', 'CASH3.SA', 'AZZA3.SA', 'PGMN3.SA', 'PLPL3.SA', 'BRIT3.SA', 'PTBL3.SA', 'CSMG3.SA', 'TASA4.SA', 'DIRR3.SA', 'WIZC3.SA', 'DASA3.SA', 'MEAL3.SA', 'GUAR3.SA', 'EVEN3.SA', 'GRND3.SA', 'OIBR3.SA', 'LOGG3.SA', 'KEPL3.SA', 'MDIA3.SA', 'FIQE3.SA', 'MTRE3.SA', 'BRSR6.SA', 'OPCT3.SA', 'ENJU3.SA', 'SOJA3.SA', 'MATD3.SA', 'AMAR3.SA', 'BMGB4.SA', 'PDGR3.SA', 'MILS3.SA', 'ESPA3.SA', 'MYPK3.SA', 'FESA4.SA', 'TECN3.SA', 'SEER3.SA', 'LEVE3.SA', 'VULC3.SA', 'RCSL4.SA', 'SHOW3.SA', 'ORVR3.SA', 'TRIS3.SA', 'HBOR3.SA', 'AMBP3.SA', 'USIM3.SA', 'INTB3.SA', 'TUPY3.SA', 'CAML3.SA', 'JALL3.SA', 'EALT3.SA', 'ZAMP3.SA', 'AZEV3.SA', 'LUPA3.SA', 'VITT3.SA', 'VLID3.SA', 'ABCB4.SA', 'ETER3.SA', 'LAVV3.SA', 'ITUB3.SA', 'PNVL3.SA', 'PFRM3.SA', 'BLAU3.SA', 'TRAD3.SA', 'KLBN3.SA', 'ALPK3.SA', 'DESK3.SA', 'INEP3.SA', 'RNEW4.SA', 'JSLG3.SA', 'MDNE3.SA', 'ARML3.SA', 'UNIP6.SA', 'BMOB3.SA', 'AGXY3.SA', 'SHUL4.SA', 'PMAM3.SA', 'BRAP3.SA', 'PINE4.SA', 'AERI3.SA', 'ROMI3.SA', 'AGRO3.SA', 'INEP4.SA', 'HBRE3.SA', 'DMVF3.SA', 'ITSA3.SA', 'DEXP3.SA', 'BIOM3.SA', 'TGMA3.SA', 'LPSB3.SA', 'PORT3.SA', 'SAPR3.SA', 'RNEW3.SA', 'TAEE4.SA', 'TCSA3.SA', 'ELMD3.SA', 'CMIG3.SA', 'SANB4.SA', 'GGBR3.SA', 'AALR3.SA', 'POMO3.SA', 'RAPT3.SA', 'SANB3.SA', 'ALPA3.SA', 'TFCO4.SA', 'ATMP3.SA', 'TAEE3.SA', 'TPIS3.SA', 'RSID3.SA', 'ALLD3.SA', 'CSUD3.SA', 'EALT4.SA', 'GOAU3.SA', 'TASA3.SA', 'VIVR3.SA', 'EUCA4.SA', 'CTSA4.SA', 'UCAS3.SA', 'LAND3.SA', 'VTRU3.SA', 'BOBR4.SA', 'HAGA4.SA', 'CSRN3.SA', 'DOTZ3.SA', 'CEBR5.SA']

# Lista de tickers (tokens) das ações que você deseja consultar
test_tickers = ['B3SA3.SA','PETR4.SA']

# Função para obter o preço atual de uma lista de tickers
def get_current_prices(tickers):
    # Cria um dicionário para armazenar os preços
    prices = {}
    
    # Obtém os dados de cada ticker
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d')  # Obtém os dados do último dia
        if not data.empty:
            prices[ticker] = data['Close'].iloc[-1]  # Obtém o preço de fechamento mais recente
    
    return prices

# Obtém os preços atuais
current_prices = get_current_prices(test_tickers)

# Exibe os preços atuais
for ticker, price in current_prices.items():
    print(f'{ticker}: {price:.2f}')