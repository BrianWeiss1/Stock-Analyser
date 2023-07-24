import requests
def getStockPrediction(symbol):
	stock = symbol
	url = "https://stock-analysis.p.rapidapi.com/api/v1/resources/growth-estimate"

	querystring = {"ticker":stock}

	headers = {
		"X-RapidAPI-Key": "d3234f9b98msh636f82f9af5f491p15d26ejsn2b89beb2bdc9",
		"X-RapidAPI-Host": "stock-analysis.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	dict = response.json()

	print(dict[stock]["Current year"])
	
	return dict[stock]["Current year"]

stockList = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'TSLA', 'META', 'GOOG', 'UNH', 'JPM', 'JNJ', 'XOM', 'AVGO', 'LLY', 'MRK', 'CVX', 'PEP', 'ABBV', 'COST', 'ADBE', 'CRM', 'WMT', 'BAC', 'MCD', 'CSCO', 'TMO', 'PFE', 'ACN', 'ABT', 'NFLX', 'LIN', 'ORCL', 'AMD', 'WFC', 'TXN', 'DHR', 'DIS', 'NEE', 'RTX', 'SPGI', 'INTC', 'HON', 'INTU', 'LOW', 'UPS', 'COP', 'CAT', 'QCOM', 'BMY', 'NKE', 'UNP', 'IBM', 'AMGN', 'ISRG', 'MDT', 'NOW', 'SBUX', 'PLD', 'AMAT', 'ELV', 'BLK', 'BKNG', 'AXP', 'LMT', 'SCHW', 'MDLZ', 'SYK', 'GILD', 'TJX', 'ADP', 'CVS', 'ADI', 'MMC', 'VRTX', 'AMT', 'ETN', 'LRCX', 'PYPL', 'SLB', 'TMUS', 'ZTS', 'REGN', 'BSX', 'EQIX', 'BDX', 'PANW', 'EOG', 'PGR', 'DUK', 'ITW', 'AON', 'SNPS', 'CSX', 'CME', 'APD', 'ATVI', 'CDNS', 'NOC', 'ICE', 'SHW', 'KLAC', 'TGT', 'FDX', 'FCX', 'HCA', 'ORLY', 'CMG', 'MMM', 'MCK', 'MCO', 'HUM', 'NXPI', 'USB', 'NSC', 'PNC', 'MPC', 'EMR', 'ROP', 'DXCM', 'FTNT', 'APH', 'PXD', 'MAR', 'MSI', 'MCHP', 'PSX', 'JCI', 'SRE', 'AJG', 'ECL', 'CCI', 'PCAR', 'TDG', 'CARR', 'PSA', 'ADSK', 'KMB', 'AZO', 'ADM', 'TEL', 'GIS', 'IDXX', 'AEP', 'COF', 'OXY', 'CTAS', 'TFC', 'MNST', 'VLO', 'AIG', 'STZ', 'ANET', 'NUE', 'IQV', 'EXC', 'CHTR', 'MRNA', 'WELL', 'WMB', 'MSCI', 'SPG', 'CTVA', 'TRV', 'AFL', 'HLT', 'PAYX', 'BIIB', 'MET', 'DHI', 'ROK', 'CPRT', 'HES', 'CNC', 'ROST', 'YUM', 'SYY', 'LHX', 'AMP', 'DOW', 'CMI', 'CSGP', 'AME', 'OTIS', 'FIS', 'HSY', 'ODFL', 'XEL', 'PPG', 'PRU', 'KMI', 'BKR', 'DLR', 'GWW', 'CTSH', 'NEM', 'DVN', 'VRSK', 'HAL', 'FAST', 'VICI', 'PEG', 'RMD', 'GEHC', 'LEN', 'URI', 'CEG', 'RSG', 'DLTR', 'ABC', 'DAL', 'ACGL', 'MTD', 'KEYS', 'ZBH', 'ANSS', 'ALL', 'GPN', 'OKE', 'VMC', 'APTV', 'WBD', 'ILMN', 'KHC', 'WEC', 'PWR', 'PCG', 'MLM', 'AWK', 'HPQ', 'WST', 'CBRE', 'EIX', 'AVB', 'KDP', 'XYL', 'TROW', 'EBAY', 'EFX', 'FTV', 'ALB', 'DFS', 'FANG', 'CDW', 'GLW', 'BAX', 'WTW', 'CAH', 'SBAC', 'TTWO', 'ALGN', 'ENPH', 'CHD', 'HIG', 'MPWR', 'TSCO', 'ULTA', 'STT', 'MTB', 'EQR', 'DTE', 'LYB', 'STE', 'AEE', 'HPE', 'RCL', 'LUV', 'ETR', 'MKC', 'GPC', 'WBA', 'FICO', 'RJF', 'IFF', 'DOV', 'DRI', 'INVH', 'WAB', 'CTRA', 'FITB', 'PPL', 'VTR', 'HOLX', 'EXR', 'FSLR', 'VRSN', 'PODD', 'COO', 'TDY', 'CNP', 'CLX', 'ARE', 'EXPD', 'PFG', 'NVR', 'FLT', 'HWM', 'UAL', 'LVS', 'MOH', 'IRM', 'CMS', 'BALL', 'OMC', 'TRGP', 'SWKS', 'MAA', 'CCL', 'TER', 'ATO', 'PHM', 'NTAP', 'PAYC', 'EXPE', 'HBAN', 'STLD', 'TYL', 'NDAQ', 'BRO', 'WAT', 'NTRS', 'BBY', 'FDS', 'GRMN', 'SJM', 'CINF', 'RVTY', 'MRO', 'DGX', 'JBHT', 'IEX', 'ZBRA', 'CAG', 'ESS', 'PTC', 'CFG', 'SYF', 'MGM', 'TSN', 'SWK', 'CBOE', 'AMCR', 'EQT', 'IPG', 'SEDG', 'AES', 'AKAM', 'SNA', 'LKQ', 'AVY', 'TXT', 'POOL', 'EVRG', 'DPZ', 'LNT', 'LYV', 'TECH', 'EPAM', 'KMX', 'MAS', 'UDR', 'MOS', 'NDSN', 'TAP', 'TRMB', 'AXON', 'MTCH', 'KIM', 'PKG', 'VTRS', 'WRB', 'JKHY', 'HST', 'LDOS', 'CPT', 'APA', 'WDC', 'TFX', 'FMC', 'CZR', 'INCY', 'PEAK', 'ETSY', 'HRL', 'CHRW', 'STX', 'AAL', 'KEY', 'WYNN', 'ALLE', 'BWA', 'GEN', 'PNR', 'HSIC', 'CDAY', 'EMN', 'QRVO', 'CRL', 'ROL', 'REG', 'TPR', 'MKTX', 'AOS', 'UHS', 'JNPR', 'PNW', 'CPB', 'HII', 'GNRC', 'FOXA', 'NRG', 'RHI', 'BXP', 'FFIV', 'XRAY', 'CTLT', 'NCLH', 'BEN', 'BIO', 'WHR', 'BBWI', 'IVZ', 'HAS', 'PARA', 'NWSA', 'WRK', 'FRT', 'CMA', 'AIZ', 'SEE', 'ALK', 'VFC', 'DXC', 'DVA', 'ZION', 'MHK', 'OGN', 'FOX', 'LNC', 'AAP', 'NWL', 'NWS', 'FTRE']
correspondinglst = []
correspondingdict = {}
try:
    for symbol in stockList:
        stockPrediction = getStockPrediction(symbol)
        print("a")
        print("a")
        correspondinglst.append(stockPrediction)
        correspondingdict[symbol] = stockPrediction
except:
    print(correspondinglst)
    print(correspondingdict) 
correspondingdict = {'AAPL': '-2.10', 'MSFT': '5.00', 'AMZN': '688.90', 'NVDA': '137.10', 'TSLA': '-15.20', 'META': '37.50', 'GOOG': '16.70', 'UNH': '11.90', 'JPM': '32.20', 'JNJ': '5.30', 'XOM': '-33.40', 'AVGO': '11.40', 'LLY': '9.40', 'MRK': '-56.70', 'CVX': '-30.50', 'PEP': '10.50', 'ABBV': '-21.10', 'COST': '6.80', 'ADBE': '14.70', 'CRM': '42.20', 'WMT': '-0.80', 'BAC': '5.30', 'MCD': '10.40', 'CSCO': '13.40'}
print("a")
# # Replace 'YOUR_API_KEY' with the API key you received in the email
# API_KEY = '32ewfeasf43fewgre3r4'
# BASE_URL = 'https://api.finnworlds.com/api/v1'

# def get_company_ratings(company_ticker, date_from=None, date_to=None, rated=None):
#     url = f"{BASE_URL}/companyratings"
#     params = {'key': API_KEY, 'company_ticker': company_ticker}

#     if date_from:
#         params['date_from'] = date_from
#     if date_to:
#         params['date_to'] = date_to
#     if rated:
#         params['rated'] = rated

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Failed to fetch company ratings for {company_ticker}. Error: {response.text}")
#         return None

# def get_analyst_ratings(analyst_name, analyst_firm=None, date_from=None, date_to=None, rated=None):
#     url = f"{BASE_URL}/analystratings"
#     params = {'key': API_KEY, 'analyst_name': analyst_name}

#     if analyst_firm:
#         params['analyst_firm'] = analyst_firm
#     if date_from:
#         params['date_from'] = date_from
#     if date_to:
#         params['date_to'] = date_to
#     if rated:
#         params['rated'] = rated

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Failed to fetch analyst ratings for {analyst_name}. Error: {response.text}")
#         return None

# def get_consensus_ratings(company_ticker):
#     url = f"{BASE_URL}/consensusratings"
#     params = {'key': API_KEY, 'company_ticker': company_ticker}

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         return response.json()
#     else:
# #         print(f"Failed to fetch consensus ratings for {company_ticker}. Error: {response.text}")
# #         return None

# # if __name__ == "__main__":
# #     # Example usage
# #     company_ticker = "AAPL"
# #     analyst_name = "daniel_ives"

# #     company_ratings = get_company_ratings(company_ticker)
# #     if company_ratings:
# #         print("Company Ratings:")
# #         print(company_ratings)

# #     analyst_ratings = get_analyst_ratings(analyst_name)
# #     if analyst_ratings:
# #         print("\nAnalyst Ratings:")
# #         print(analyst_ratings)

# #     consensus_ratings = get_consensus_ratings(company_ticker)
# #     if consensus_ratings:
# #         print("\nConsensus Ratings:")
# #         print(consensus_ratings)
# ########### Python 2.7 #############
# import urllib, base64
# import http.client, urllib.request, urllib.parse, urllib.error, base64

# headers = {
#     # Request headers
#     'Ocp-Apim-Subscription-Key': '{subscription key}',
# }

# params = urllib.urlencode({
#     # Request parameters
#     'History': '{int}',
#     'Future': '{int}',
# })

# try:
#     conn = http.client.HTTPSConnection('api.etoro.com')
#     conn.request("GET", "/API/Internal/V1/FinancialReports/Estimates/{InstrumentID}?%s" % params, "{body}", headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))

# ####################################

# ########### Python 3.2 #############

# headers = {
#     # Request headers
#     'Ocp-Apim-Subscription-Key': '{subscription key}',
# }

# params = urllib.parse.urlencode({
#     # Request parameters
#     'History': '{int}',
#     'Future': '{int}',
# })

# try:
#     conn = http.client.HTTPSConnection('api.etoro.com')
#     conn.request("GET", "/API/Internal/V1/FinancialReports/Estimates/{InstrumentID}?%s" % params, "{body}", headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))

# ####################################