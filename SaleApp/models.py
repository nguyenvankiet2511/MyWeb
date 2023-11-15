from sqlalchemy import Integer, String, Float, Column, ForeignKey, Boolean, Enum
from SaleApp import app, db
from sqlalchemy.orm import relationship
from enum import Enum as UserEnum
from flask_login import UserMixin


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False, default=0)
    img = Column(String(255))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    username = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        import  hashlib
        u= User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()
        c1 = Category(name="Mobile")
        c2 = Category(name="Laptop")
        db.session.add_all([c1, c2])

        p1 = Product(name="Iphone 13", price="240000000",
                     img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                     category_id=1)
        p2 = Product(name="SamSung Note 8", price="140000000",
                     img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                     category_id=1)
        p3 = Product(name="OPPO Reno 5", price="63000000",
                     img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                     category_id=1)
        p4 = Product(name="Iphone 15", price="550000000",
                     img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                     category_id=1)
        p5 = Product(name="Ipad Pro ", price="230000000",
                     img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                     category_id=2)
        p6 = Product(name="Laptop HP Icore5", price="280000000",
                     img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                     category_id=2)
        p7 = Product(name="Redme D3", price="440000000",
                     img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                     category_id=1)
        p8 = Product(name="Laptop Dell Corei5", price="200000000",
                     img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                     category_id=2)
        p9 = Product(name="Iphone 11 Pro Max", price="150000000",
                     img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                     category_id=1)
        p10 = Product(name="SamSung Garaxy Note10", price="130000000",
                      img='https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
                      category_id=1)
        db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        db.session.commit()
