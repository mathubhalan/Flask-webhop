# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:09:27 2018

@author: Mathu_Gopalan
"""
from flask import Flask
from flask_restful import Api
from createorder import CreateOrder
from searchproducts import SearchProducts

app = Flask(__name__)
api = Api(app)

api.add_resource(SearchProducts, '/SearchProducts')
api.add_resource(CreateOrder, '/CreateOrder')


if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
