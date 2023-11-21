from SaleApp.models import Category, Product, User, UserRole
from SaleApp import app, db, admin
from flask import redirect
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import current_user, logout_user


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class ProductView(AuthenticatedAdmin):
    can_view_details = True
    edit_modal = True
    details_modal = True
    can_export = True
    column_filters = ['name', 'price']
    column_searchable_list = ['name']


class UserView(AuthenticatedAdmin):
    pass


class CategoryView(AuthenticatedAdmin):
    can_view_details = True
    edit_modal = True
    details_modal = True
    can_export = True
    column_filters = ['name']
    column_searchable_list = ['name']


class AboutUsView(AuthenticatedUser):
    @expose("/")
    def index(self):
        return self.render('admin/about_us.html')


class Static_Report(AuthenticatedUser):
    @expose("/")
    def index(self):
        return self.render('admin/statistic_report.html')


class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(UserView(User, db.session))
admin.add_view(AboutUsView(name="Information"))
admin.add_view(Static_Report(name="Report"))
admin.add_view(LogoutView(name='Logout'))
