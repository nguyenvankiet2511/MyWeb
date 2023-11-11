from SaleApp.models import Category, Product


def get_Category():
    return Category.query.all()


def get_Product(key):
    product = Product.query
    if key:
        product = product.filter(Product.name.contains(key))
    return product.all()
