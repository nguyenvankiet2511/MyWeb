from flask import render_template, request
from SaleApp import app, dao, login
from SaleApp.admin import *


@app.route("/")
def index():
    key = request.args.get("key")
    categ = dao.get_Category()
    prod = dao.get_Product(key)
    return render_template('index.html', categories=categ, products=prod)

@app.route('/login_admin',methods=['post'])
def login_admin():
    pass
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
