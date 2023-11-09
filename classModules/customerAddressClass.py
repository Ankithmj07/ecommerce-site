from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db


class Addresses:
    def getAddresses(self,c_id):
        sqlIns=text('INSERT INTO customer_addresses (customer_id, address_id) SELECT :c_id, (SELECT address_id FROM addresses WHERE address_id = (SELECT address_id FROM addresses ORDER BY address_id DESC LIMIT 1)) WHERE NOT EXISTS (SELECT 1 FROM customer_addresses WHERE address_id = (SELECT address_id FROM addresses ORDER BY address_id DESC LIMIT 1));')

        db.engine.execute(sqlIns,c_id=c_id)


        sqlAdd=text('SELECT addresses.* FROM customers JOIN customer_addresses ON customers.customer_id = customer_addresses.customer_id JOIN addresses ON customer_addresses.address_id = addresses.address_id WHERE customers.customer_id = :c_id ORDER BY addresses.address_id DESC')
        resAdd=db.engine.execute(sqlAdd,c_id=c_id)

        assocData=resAdd.fetchall()

        if len(assocData) > 0:
            return jsonify([dict(row) for row in assocData])
        else:
            return '0'
    

    def sendAddress(self,addressId):
        addressId=addressId
        sqlAdd=text('SELECT * FROM addresses WHERE address_id=:addressId')
        resAdd=db.engine.execute(sqlAdd,addressId=addressId)

        assocData=resAdd.fetchall()
        return jsonify([dict(row) for row in assocData])
    
objAddresses=Addresses()