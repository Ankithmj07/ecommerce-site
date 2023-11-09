from flask import Blueprint,request,render_template,url_for,jsonify
from classModules.productClass import objProducts
from classModules.adsClass import objAds
from classModules.visitorClass import objVisitors
from classModules.contactClass import objContact
from classModules.productClickClass import objProductClick
from classModules.productDetailsClass import objProductDetails
from classModules.bannerProductsClass import objBannerProducts
from classModules.searchProductClass import objSearch


product_blueprint=Blueprint('product_blueprint',__name__)
@product_blueprint.route('/products',methods=['GET'])

def products():
    return objProducts.displayAllProducts()

@product_blueprint.route('/track-ad-click',methods=['GET'])

def logAdClick():
    return objAds.saveAdClicks()

@product_blueprint.route('/track-visitors',methods=['GET'])
def logVisitors():
    return objVisitors.saveVisitors()

@product_blueprint.route('/save-contacts',methods=['POST'])
def logContacts():
    
    # Recieving the data from client / front end
    customerName=request.form['customerName']
    customerEmail=request.form['customerEmail']
    customerMobile=request.form['customerMobile']
    customerQuery=request.form['customerQuery']

    # check if Name, Email, Mobile is empty


    if not customerName and not customerEmail and not customerMobile:
        return '[{"errFlag":1,"message":"Some Fields are Empty"}]'

    return objContact.saveContact(customerName,customerEmail,customerMobile,customerQuery)

@product_blueprint.route('/trackProductClick/<product_id>',methods=['GET'])
def trackProductClick(product_id):
    data=objProductClick.saveProductClick(product_id)
    other_page_url=url_for('product_blueprint.trackProductClick',product_id=product_id)

    #return jsonify({"other_page_url": other_page_url})
    return render_template('product-details.html')


@product_blueprint.route('/product-details',methods=['GET'])
def trackProductId():
    return objProductDetails.productDetails()

@product_blueprint.route('/banner-product-id/<pName>',methods=['GET'])
def bannerPid(pName):
    return objBannerProducts.bannerPid(pName)


@product_blueprint.route('/search-products',methods=['POST'])
def searchProducts():
    productName=request.form['searchInput']

    if productName=='':
        return '0'
    else:
        return objSearch.searchProducts(productName)
    
    

