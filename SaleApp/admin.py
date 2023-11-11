from SaleApp.models import Category, Product, User
from SaleApp import app, db, admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose

class AboutUsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/about_us.html')
class Static_Report(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/statistic_report.html')

class ProductView(ModelView):
    can_view_details = True
    edit_modal = True
    details_modal = True
    can_export = True
    column_filters = ['name', 'price']
    column_searchable_list = ['name']

class CategoryView(ModelView):
    can_view_details = True
    edit_modal = True
    details_modal = True
    can_export = True
    column_filters = ['name']
    column_searchable_list = ['name']


admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(AboutUsView(name="Information"))
admin.add_view(Static_Report(name="Report"))
