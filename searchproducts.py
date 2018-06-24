from flask_restful import Resource
import sqlite3

class SearchProducts(Resource):
    TABLE_NAME = 'product'

    def get(self):
        connection = sqlite3.connect('data1.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'specialty': row[0], 'products': row[1]})
        connection.close()

        return {'products': items}
