import yfinance as yf
import os
from openai import OpenAI

def get_latest_price(ticker):
    data = yf.Ticker(ticker).history(period="5d")
    if data.empty:
        return "取得失敗"
    return round(float(data["Close"].iloc[-1]), 4)

def get_market_data():
    return {
        "USDJPY": get_latest_price("JPY=X"),
        "US10Y": get_latest_price("^TNX"),
        "WTI": get_latest_price("CL=F"),
        "S&P500": get_latest_price("^GSPC"),
        "VIX": get_latest_price("^VIX"),
        "DXY": get_latest_price("DX-Y.NYB"),
    }

def analyze(data):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    prompt = f"""
    以下の市場データからUSDJPYの環境を分析してください。

    {data}

    出力：
    ・円安要因
    ・円高要因
    ・今日の市場環境（レンジ / ブレイク / リスクオフ）
    ・トレード方針（10〜30pips想定）
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def main():
    data = get_market_data()

    print("【市場データ】")
    print(data)

    result = analyze(data)

    print("\n【AI分析】")
    print(result)

if __name__ == "__main__":
    main()
