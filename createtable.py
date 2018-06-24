# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:13:51 2018

@author: Mathu_Gopalan
"""

import sqlite3

connection = sqlite3.connect('data1.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS order_master (userid text, products text, shippinginfo text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS product (specialty int, products text)"
cursor.execute(create_table)

prd_data = (1,"Sensodyne, Aquafresh, Corsodyl")
insert_qry = "INSERT INTO product VALUES (?,?)"
cursor.execute(insert_qry,prd_data)



connection.commit()

connection.close()
