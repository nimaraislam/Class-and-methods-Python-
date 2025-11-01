class Cart:
    def __init__(self):
        self.product={}
        self.discount_code=""
        
    def add_item(self,name, price):
        if name == "":
           return "Ptoduct name is empty"
        else:
            self.product[name]=float(price)
            return self.product
        
    def calculate_total_amount(self):
        total_price=sum(self.product.values())
        return round(total_price,2)
    
    def apply_discount(self,discount_code):
        if discount_code == "ICA10":
            discount_amount = float(self.calculate_total_amount())*0.10
            return round(discount_amount,2)    
        elif discount_code == "STUDENT5":
            num_products_over_5 = len([price for price in self.product.values() if price>5 ])
            return num_products_over_5*5
        else:
            return 0
        
        