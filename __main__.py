from dotenv import load_dotenv
from product_search import search_products
from query_extraction import formulate_description, extract_query
from langgraph.graph import StateGraph, MessagesState, START, END

def main():
    load_dotenv()

    print("Hello! Describe the product you are looking for: ")
    description = input()
    structured_description = formulate_description(description)
    print(f"Structured description: {structured_description}")
    search_query = extract_query(structured_description)
    print(f"Seach query: {search_query}")

    #matched_products = search_products(search_query)
    #print("Your matched products are \n")
    #for p in matched_products:
        #print(p)

if __name__ == "__main__":
    main()