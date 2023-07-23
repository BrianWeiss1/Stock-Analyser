import requests
def bozo():
    def get_stock_analysis_forecast(symbol, api_key):
        base_url = "https://www.alphavantage.co/query"
        endpoint = "EARNINGS"  # Using "endpoint" instead of "function" for the API parameter
        # Set the parameters for the API request
        params = {
            "function": endpoint,
            "symbol": symbol,
            "apikey": api_key
        }

        try:
            # Make the API request
            response = requests.get(base_url, params=params)
            data = response.json()

            # Check if the request was successful
            print(data)
            if "annualEarnings" in data and len(data["annualEarnings"]) > 0:
                return data["annualEarnings"]
            else:
                print("No analysis forecast values found for the specified stock.")
                return None

        except requests.exceptions.RequestException as e:
            print("Error while fetching data:", e)
            return None

    # Replace 'YOUR_API_KEY' with your Alpha Vantage API key
    api_key = "N6A6OZPCLEL8UYNP"
    stock_symbol = "CVNA"  # Replace with the desired stock symbol

    analysis_forecast_values = get_stock_analysis_forecast(stock_symbol, api_key)
    if analysis_forecast_values:
        print("Stock Analysis Forecast Values for", stock_symbol)
        print(analysis_forecast_values)

import yfinance as yf

def get_stock_forecasts(ticker_symbol):
    try:
        # Create a Ticker object for the stock
        stock = yf.Ticker(ticker_symbol)
        print(stock)
        # Get analyst recommendations and forecasts data
        analysts_info = stock.recommendations

        if analysts_info.empty:
            print(f"No analyst recommendations available for {ticker_symbol}.")
            return None

        # Display the latest recommendations and forecasts
        latest_forecast = analysts_info.tail(1)
        print(f"Latest analyst forecast for {ticker_symbol}:")
        print(latest_forecast)

        return latest_forecast

    except Exception as e:
        print(f"Error occurred while retrieving data: {e}")
        return None

# Example usage
stock_symbol = "AAPL"  # Replace this with the desired stock symbol
get_stock_forecasts(stock_symbol)
