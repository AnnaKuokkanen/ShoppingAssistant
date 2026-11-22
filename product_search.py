import os
from dotenv import load_dotenv
import serpapi
from models.Product import Product

load_dotenv()

# this method connects to the API and finds top 10 products matching the key words
def search_products(keywords):        
    client = serpapi.Client(api_key=os.getenv("SERPAPI_KEY"))

    google_results = client.search({
        "engine": "google_shopping",
        "q": keywords[0]
    })

    shopping_results = google_results["shopping_results"][:10]
    product_list = list(map(lambda result: Product(result.get("title"), result.get("price"), result.get("rating")), shopping_results))
    
    return product_list
