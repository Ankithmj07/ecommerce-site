from flask import Flask,session,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import redis
from os import environ
from db import db
from random import *
from flask_migrate import Migrate
from flask_cors import CORS,cross_origin
from customerLogin import *
import secrets
from admin_login import users_blueprint
from home import product_blueprint
from admin_dashboard import admin_dashboard_blueprint
from cart import cart_blueprint
from customer import customer_blueprint
from orders import order_blueprint
from customerLogin import emailVerification_blueprint,customerDetails_blueprint
from OtherBrands import otherBrands_blueprint


app=Flask(__name__)

app.secret_key='EveryThingOutOfContext'



# DB Config
username='root'
password=''
server='127.0.0.1'
dbname='/ecommerce_store'
userrpass='mysql+pymysql://'+username+':'+password+'@'
app.config['SQLALCHEMY_DATABASE_URI']=userrpass+server+dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False





app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = 'C:\e-commerce-project\ecommerce-server/session'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True


Session(app)
CORS(app)

db.init_app(app)



# Register Blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(admin_dashboard_blueprint)
app.register_blueprint(cart_blueprint)
app.register_blueprint(customer_blueprint)
app.register_blueprint(order_blueprint)
app.register_blueprint(emailVerification_blueprint)
app.register_blueprint(customerDetails_blueprint)
app.register_blueprint(otherBrands_blueprint)

@app.route('/')
def hello_world():
	return render_template('index.html')



if __name__=='__main__':
    app.run(host='0.0.0.0',debug = True,port=8080)