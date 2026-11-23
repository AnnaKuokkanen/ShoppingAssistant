from dotenv import load_dotenv
from product_search import search_products
from query_extraction import extract_query
from langgraph.graph import StateGraph, MessagesState, START, END

def main():
    load_dotenv()

    print("Hello! Describe the product you are looking for: ")
    description = input()
    query = extract_query(description)

    matched_products = search_products(query)
    print("Your matched products are \n")
    for p in matched_products:
        print(p)

if __name__ == "__main__":
    main()