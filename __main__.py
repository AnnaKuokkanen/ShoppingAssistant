from product_search import search_products

def main():
    print("Hello! Give me up to five keywords to describe the product you are looking for: ")
    keywords = []
    for i in range(5):
        next_keyword = input()
        if not next_keyword: 
            break
        keywords.append(next_keyword)

    matched_products = search_products(keywords)
    print("Your matched products are \n")
    for p in matched_products:
        print(p)

if __name__ == "__main__":
    main()