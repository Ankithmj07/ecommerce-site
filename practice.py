class College:
    student='Sachin'
    branch='CSE'
    sem=6

    def __init__(self):
        print("The message is from Constructor")

    def departments(self,deptName):
        self.deptName=deptName
    
    def mainBranch(self):
        print(self.deptName)
        

    
std1=College()
print(f"{std1.student} is from {std1.sem} sem {std1.branch}")
std1.departments("CSE")
std1.mainBranch()




json_data=[
  {
    "discount_price": "22250.00",
    "id": 1,
    "product_color": "Silver",
    "product_id": 1,
    "product_image": "https://rukminim2.flixcart.com/image/416/416/kg8avm80/mobile/g/z/c/apple-iphone-12-pro-max-dummyapplefsn-original-imafwgcyyemh9hbg.jpeg?q=70",
    "product_name": "iPhone 12 Pro Max 128 GB - Silver",
    "product_original_price": "119000.00",
    "product_price": "96750.00",
    "product_qty": 2
  }
]
print(len(json_data))

for i in range(len(json_data)):
    print(json_data[i]["discount_price"])
    
    # Representational State Transfer (REST)
# Simple Object Acces protocal  (SOAP)
addId=[
  {
    "address_id": 6
  }
]
for i in addId:
    add=i.get('address_id',None)

print(add)


gadgetswave='zxtngftfusvhxpkw'
mj='ekjytruigbqgzyzz'

"SELECT id,p_name FROM `products` WHERE p_name LIKE '%iphone%';"


html='<div class="slide first">
                    <div style="position: relative;">
                        <img class="slideImage" src="\static\images\slide(1).jpg" style="width: 95%;">
                        <div style="position: absolute;top: 0;margin-top: 45%;margin-left: 8%;display: flex;width: 100%;">
                            <button class="btn" style= "font-size: 14px;font-weight: 600; color: #1d1d1f;line-height: 20px;background-color: #fff;width: 145px;height: 43px;border-radius: 30px;">Stream now&nbsp;&nbsp;<img src="\static\images\play-button (1).png" style="width: 15px;"></button>
                            <h4 style="font-size: 19px;font-weight: 500;color: #fff;margin-left: 3%;margin-top: 0.7%;"><span style="font-weight: 600;">Crime : </span>Coming to theaters October 20.</h4>
                        </div>
                    </div>
                </div>'