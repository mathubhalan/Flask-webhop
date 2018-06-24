# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:08:59 2018

@author: Mathu_Gopalan
"""

from flask_restful import Resource, reqparse
import sqlite3


class CreateOrder(Resource):
    TABLE_NAME = 'order_master'

    parser = reqparse.RequestParser()
    parser.add_argument('UserID',
        type=str,
        required=True,
        help="UserID cannot be left blank!"
    )
    parser.add_argument('Products',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('ShippingInfo',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    
    def post(self):
        data = CreateOrder.parser.parse_args()
        order_data = {'userid': data['UserID'], 'products': data['Products'], 'shippinginfo': data['ShippingInfo']}
        connection = sqlite3.connect('data1.db')
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES(?, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (order_data['userid'], order_data['products'],order_data['shippinginfo']))
        connection.commit()
        connection.close()
        return {"message": "Order created successfully."}, 201
