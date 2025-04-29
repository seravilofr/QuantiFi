import yfinance as yf

def get_indices_values():
    indices = {
        "S&P 500": "^GSPC",
        "CAC 40": "^FCHI",
        "DAX": "^GDAXI"
    }

    results = {}

    for name, symbol in indices.items():
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        if not data.empty:
            price = round(data['Close'].iloc[-1], 2)
            results[name] = price
        else:
            results[name] = None  # En cas de problème

    return results

if __name__ == "__main__":
    values = get_indices_values()
    for name, price in values.items():
        if price:
            print(f"{name}: {price}")
        else:
            print(f"{name}: données non disponibles")
