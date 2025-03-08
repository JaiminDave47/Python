import requests

def get_stocks():
    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    response = (requests.get(url)).json()
    if response["success"] and "data" in response:
        print(response["message"])
        data = response["data"]
        limit = int(data["limit"])
        stock_list = data["data"]
        return stock_list, limit
    else:
        raise Exception("Failed to fetch stock details")
        
def main():
    try:
        stocks, limit = get_stocks()
        for i in range(limit):
            print(f"{stocks[i]["Symbol"]}")
            print(f"Price: {stocks[i]["CurrentPrice"]}")
            print(f"it's Market Cap. is around {stocks[i]["MarketCap"]}\n")
    except Exception:
        print(str(Exception))

if __name__ == "__main__":
    main()