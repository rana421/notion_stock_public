import requests
import setting

NOTION_TOKEN = setting.NOTION_TOKEN
DATABASE_ID  = setting.DATABASE_ID
BASE_URL     = "https://api.notion.com"

# database一覧を取得

session = requests.Session()
session.headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": f"Bearer {NOTION_TOKEN}"
}

url = BASE_URL + "/v1/databases/" + DATABASE_ID + "/query"
response = session.post(url)

for page in response.json()["results"]:
    page_id = page["url"].split("/")[-1].split("-")[-1]
    stock_code = page["properties"]["証券コード"]["number"]

    # LINE証券APIより株価取得
    data = {"reqCodeList": [{"secCode": stock_code, "secTypeKbn": "STOCK"}]}
    price = requests.post('https://trade.line-sec.co.jp/exosphere/price-pool-front-api/v1/price/basic', json=data)
    currentPrice = price.json()["priceDataList"][0]["currentPrice"]

    financials = requests.get(f'https://trade.line-sec.co.jp/exosphere/exchange/v1/stock/{stock_code}/financials')
    # 配当利回り計算
    dividend = financials.json()["dividendPerShare"]
    if dividend is None:
        dividend = 0
    dividendYield = float(dividend) / float(currentPrice) * 100

    # Notionに株価を更新
    data = {
        "properties": {
            "現在値": {"number": int(float(currentPrice))},
            "配当利回り": {"number": round(dividendYield, 3)}
        }
    }

    url = BASE_URL + "/v1/pages/" + page_id
    response = session.patch(url, json=data)

    print("証券コード", stock_code)
    print("現在価格", currentPrice)
    print("一株当たり配当", dividend)
    print("配当利回り", dividendYield)
    print()
