import yfinance as yf

def get_index_value(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    if not data.empty:
        return round(data['Close'].iloc[-1], 2)
    else:
        return None

if __name__ == "__main__":
    indices = {
        "S&P 500": "^GSPC",
        "CAC 40": "^FCHI",
        "DAX": "^GDAXI"
    }

    for name, symbol in indices.items():
        value = get_index_value(symbol)
        if value:
            print(f"{name}: {value}")
        else:
            print(f"{name}: données non disponibles")

