from flask import Blueprint,request,render_template
from classModules.insertIntoCart import objcartDetails
from classModules.getCartClass import objgetCartData
from classModules.deleteCartClass import objDeleteCart
from classModules.wishlistClass import objWishlist
from classModules.getWishlistDataClass import objgetWishlist
from classModules.BuyNowClass import objBuynow
from classModules.customerLoginClass import objLogin



cart_blueprint=Blueprint('cart_blueprint',__name__)



@cart_blueprint.route('/insert-cart/<product_id>',methods=['GET'])
def cartData(product_id):
    customer_id=objLogin.getCustomerId()
    return objcartDetails.getCartProduct(product_id,customer_id)


@cart_blueprint.route('/goToCart',methods=['GET'])
def goToCart():
    return render_template('add-to-cart.html')

@cart_blueprint.route('/get-cart-details',methods=['GET'])
def getCartData():
    customer_id=objLogin.getCustomerId()
    data=objgetCartData.getCartData(customer_id)
    return data

@cart_blueprint.route('/delete-cart/<product_id>',methods=['GET'])
def deleteCart(product_id):
    customer_id=objLogin.getCustomerId()
    return objDeleteCart.deleteCart(product_id,customer_id)

@cart_blueprint.route('/cart-subtotal',methods=['GET'])
def subtotal():
    customer_id=objLogin.getCustomerId()
    return objgetCartData.subTotal(customer_id)

@cart_blueprint.route('/wishlist/<product_id>',methods=['GET'])
def wishlist(product_id):
    customer_id=objLogin.getCustomerId()
    return objWishlist.wishlist(product_id,customer_id)

@cart_blueprint.route('/get-wishlist-data',methods=['GET'])
def getWishlist():
    customer_id=objLogin.getCustomerId()
    return objgetWishlist.getWishlistData(customer_id)

@cart_blueprint.route('/remove-from-wishlist/<product_id>',methods=['GET'])
def removeWish(product_id):
    customer_id=objLogin.getCustomerId()
    return objWishlist.remove(product_id,customer_id)

@cart_blueprint.route('/move-productid/<product_id>',methods=['GET'])
def moveProductId(product_id):
    pid=objBuynow.getpId(product_id)
    return render_template('buy-now.html')

@cart_blueprint.route('/BuynowDetails',methods=['GET'])
def BuynowProducts():
    return objBuynow.getProducts()

@cart_blueprint.route('/GoToBuyCart',methods=['GET'])
def gotoBuyCart():
    return render_template('cart-buy.html')

@cart_blueprint.route('/cartProducts',methods=['GET'])
def getCartProducts():
    customer_id=objLogin.getCustomerId()
    return objBuynow.getCartProducts(customer_id)


@cart_blueprint.route('/GoToWishlist',methods=["GET"])
def goToWishlist():
    return render_template("wishlist.html")

@cart_blueprint.route('/GotoOrders',methods=["GET"])
def goToOrders():
    return render_template('myOrder.html')