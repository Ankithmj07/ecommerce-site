from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db

class Products:
    def displayAllProducts(self):
        sqlProducts=text('SELECT * FROM products')
        resProducts=db.engine.execute(sqlProducts)
        assocData=resProducts.fetchall()

        return jsonify([dict(row) for row in assocData])
    
objProducts=Products()