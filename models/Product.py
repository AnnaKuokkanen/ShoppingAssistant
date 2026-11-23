class Product:
    def __init__(self, title, price, rating):
        self.title = title
        self.price = price
        self.rating = rating
        self.source
        self.description

    def __str__(self):
        return f"{self.title}, price: {self.price}, rating: {self.rating}"