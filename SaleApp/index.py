from flask import render_template, request, redirect
from SaleApp import app, dao, login
from SaleApp.admin import *
import math
from flask_login import login_user, current_user


@app.route("/")
def index():
    key = request.args.get("key")
    cate_id = request.args.get('cate_id')
    page = request.form.get('page')
    categ = dao.get_Category()
    prod = dao.get_Product(key, cate_id, page)
    num = dao.count_Product()
    page_size = app.config['PAGE_SIZE']
    return render_template('index.html', categories=categ, products=prod, pages=math.ceil(num / page_size))


@app.route('/login_admin', methods=['post'])
def login_admin():
    username = request.form.get('username')
    password = request.form.get("password")

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
    return redirect('/admin')


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    from SaleApp import admin

    app.run(debug=True)
