import requests

def get_product():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        product_data = data["data"]
        print("Current Page Items: ", product_data["currentPageItems"])
        product_list = product_data["data"]
        limit = int(product_data["limit"])
    else:
        raise Exception("Failed to fetch product details")
    return product_list, limit

def main():
    try:
        product_list, limit = get_product()
        for i in range(limit):
            print(f"Category: {product_list[i]["category"]}")
            print(f"Title: {product_list[i]["title"]}")
            print(f"Price: {product_list[i]["price"]}")
            print("\n")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()