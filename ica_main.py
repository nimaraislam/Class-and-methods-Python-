from ica import Cart
def main():
    my_cart=Cart()
    print("====================Welcome to ICA POS======================")
    print(">>Please enter your product and price.Type 'Done' to stop.")
    while True:
        product_name=input("Product name(or 'done'): ").lower().strip()
        if product_name == "done".lower():
            break
        while True:
            product_price=input(f"Enter price for '{product_name}':").strip()
            try:
                product_price_float=float(product_price)
                if product_price_float <= 0.0:
                    print("Invalid price")
                    continue
                my_cart.add_item(product_name,product_price_float)
                break
            except ValueError:
                print("Invalid price")
    print("======= Discount Codes =======")
    print("--- Available Codes : 'ICA10' and 'STUDENT5'---")
    discount_code=input("Discount Codes: ").upper().strip()
    print("--------------Pay Slip--------------")
    print(f"Sl Item -- Price (kr)")
    for index,(product,price) in enumerate(my_cart.product.items(),start=1):
            print(f"{index}. {product} -- {price:.2f} kr")
    print("-----------------------------------------")
    total_amount= my_cart.calculate_total_amount()
    print(f"Total Amount: {total_amount:.2f} kr")
    discount_amount=my_cart.apply_discount(discount_code)
    #valid_codes = ("ICA10", "STUDENT5")
    #if discount_code not in valid_codes:
    if discount_code == "ICA10" or discount_code == "STUDENT5":
         print(f"Discount Amount for '{discount_code}' : {discount_amount:.2f} kr.")
    amount_after_discount =total_amount- discount_amount     
    print(f"You need to pay: {amount_after_discount:.2f} kr")
        
main()