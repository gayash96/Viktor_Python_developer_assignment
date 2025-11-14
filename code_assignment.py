# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Product:
    def __init__(self, product_id: int, price: float):
        self.product_id = product_id
        self.price = price

    def display_basic_info(self):
        return f"Product Name: {self.__class__.__name__}, Price: EUR{self.price:.2f}"


class Book(Product):
    def __init__(self, product_id: int, price: float, title: str, author: str, number_of_pages: int,
                 weight_in_kg: float):
        super().__init__(product_id=product_id, price=price)
        self.weight_in_kg = weight_in_kg
        self.number_of_pages = number_of_pages
        self.title = title
        self.author = author

    def display_basic_info(self):
        base_info = super().display_basic_info()
        return f"{base_info}, Author: {self.author}, Title: {self.title}"


class MusicAlbum(Product):
    def __init__(self, product_id: int, price: float, title: str, artist: str, number_of_tracks: int,
                 weight_in_kg: float):
        super().__init__(product_id=product_id, price=price)
        self.weight_in_kg = weight_in_kg
        self.number_of_tracks = number_of_tracks
        self.title = title
        self.artist = artist

    def display_basic_info(self):
        base_info = super().display_basic_info()
        return f"{base_info}, Artist: {self.artist}, Title: {self.title}"


class SoftwareLicense(Product):
    def __init__(self, product_id: int, price: float, software_license_name: str):
        super().__init__(product_id=product_id, price=price)
        self.software_license_name = software_license_name

    def display_basic_info(self):
        base_info = super().display_basic_info()
        return f"{base_info}, Software License Name: {self.software_license_name}"


#######################################################################################
# Shopping Cart

class ShoppingCart:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> str:
        self.products.append(product)
        return f"Product {product.display_basic_info()} added to the cart."

    def remove_product(self, product: Product) -> str:
        if product in self.products:
            self.products.remove(product)
            return f"Product {product.display_basic_info()} removed from the cart."
        else:
            return "Product not found in the cart."

    def total_price(self) -> str:
        return f"EUR {sum(product.price for product in self.products)}"

    def total_weight(self) -> str:
        total_weight = 0.0
        for product in self.products:
            if hasattr(product, 'weight_in_kg'):
                total_weight += product.weight_in_kg
        return f"Total weight of the items: {total_weight} kg"


#######################################################################################
# Optional
# Recommendation system
def product_recommendation(carts: list[ShoppingCart]) -> str:
    following_products = {}
    for cart in carts:
        products = cart.products
        for i in range(len(products) - 1):
            current_product = products[i]
            next_product = products[i + 1]
            if current_product.display_basic_info() not in following_products:
                following_products[current_product.display_basic_info()] = {}
            if next_product.display_basic_info() not in following_products[current_product.display_basic_info()]:
                following_products[current_product.display_basic_info()][next_product.display_basic_info()] = 0
            following_products[current_product.display_basic_info()][next_product.display_basic_info()] += 1

    recommendations = {}
    for product, following in following_products.items():
        recommended_product = max(following, key=following.get)
        recommendations[product] = recommended_product

    for product, recommended in recommendations.items():
        return f"Customers who bought {product} also bought {recommended}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    book = Book(product_id=1, price=29.99, title="The book title", author="The book author",
                number_of_pages=180, weight_in_kg=0.5)
    print(book.display_basic_info())
    album = MusicAlbum(product_id=2, price=15.99, title="The album title", artist="The album artist",
                       number_of_tracks=12, weight_in_kg=0.2)
    print(album.display_basic_info())
    software = SoftwareLicense(product_id=3, price=199.99, software_license_name="Pro Software License")
    print(software.display_basic_info())

    cart = ShoppingCart()
    cart.add_product(book)
    cart.add_product(album)
    cart.add_product(software)

    print(cart.total_price())
    print(cart.total_weight())

    book2 = Book(product_id=4, price=39.99, title="Another book title", author="Another book author",
                 number_of_pages=250, weight_in_kg=0.7)

    cart2 = ShoppingCart()
    cart2.add_product(book)
    cart2.add_product(book2)
    cart2.add_product(album)

    carts = [cart, cart2]
    print(product_recommendation(carts))
