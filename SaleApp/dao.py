import hashlib
from SaleApp import app
from SaleApp.models import Category, Product, User


def get_Category():
    return Category.query.all()


def get_Product(key, cate_id, page=None):
    product = Product.query
    if key:
        product = product.filter(Product.name.contains(key))
    if cate_id:
        product = product.filter(Product.category_id.__eq__(cate_id))
    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size
        return product.slice(start, start + page_size)
    return product.all()


def count_Product():
    return Product.query.count()


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password)).first()
