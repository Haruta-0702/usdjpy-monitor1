import yfinance as yf

def get_latest_price(ticker):
    data = yf.Ticker(ticker).history(period="5d")
    if data.empty:
        return "取得失敗"
    return round(float(data["Close"].iloc[-1]), 4)

def main():
    market_data = {
        "USDJPY": get_latest_price("JPY=X"),
        "US10Y": get_latest_price("^TNX"),
        "WTI": get_latest_price("CL=F"),
        "S&P500": get_latest_price("^GSPC"),
        "VIX": get_latest_price("^VIX"),
        "DXY": get_latest_price("DX-Y.NYB"),
    }

    print("【市場データ取得結果】")
    for name, value in market_data.items():
        print(f"{name}: {value}")

if __name__ == "__main__":
    main()
