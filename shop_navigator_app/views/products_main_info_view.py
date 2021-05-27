from flask_restful import Resource
from shop_navigator_app.models.product import Product

from .. import db


class ProductsMainInfoView(Resource):
    def get(self):
        products_main_info = db.session.query(Product.id, Product.name).all()
        response_data = self.structure_product_dict(products_main_info)
        return response_data, 200

    def structure_product_dict(self, products_main_info):
        result_dict = dict()
        for product_main_info in products_main_info:
            result_dict[product_main_info[0]] = product_main_info[1]
        return result_dict