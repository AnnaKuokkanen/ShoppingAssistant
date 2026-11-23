import os
import serpapi
from models.Product import Product

# this method connects to the API and finds top 10 products matching the key words
def search_products(query):        
    client = serpapi.Client(api_key=os.getenv("SERPAPI_KEY"))

    google_results = client.search({
        "engine": "google_shopping",
        "q": query
    })

    shopping_results = google_results["shopping_results"][:10]
    product_list = list(map(lambda result: Product(result.get("title"), result.get("price"), result.get("rating")), shopping_results))
    
    return product_list

def get_immersive_product_details(product):
    client = serpapi.Client(api_key=os.getenv("SERPAPI_KEY"))
    results = client.search({
        "engine": "google_immersive_product",
        "page_token": product.get("immersive_product_page_token")
    })
    return results