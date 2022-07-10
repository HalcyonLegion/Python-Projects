from math import*

#An App to calculate the sum of different quantities of products of different values

price_product_1=input("What is the price of product 1? : ")   #Step 1 create products and quantity input prompts
quantity_product_1=input("How many of product 1 would you like? : ")
price_product_2=input("What is the price of product 2? : ")
quantity_product_2=input("How many of product 2 would you like? : ")
price_product_3=input("What is the price of product 3? : ")
quantity_product_3=input("How many of product 3 would you like? : ")

result_product_1=float(price_product_1)*float(quantity_product_1)
result_product_2=float(price_product_2)*float(quantity_product_2)
result_product_3=float(price_product_3)*float(quantity_product_3)

result=result_product_1+result_product_2+result_product_3

print("Your final price is " +str(result))  #makes it look pretty, if you add "text" you need +str to blend numbers with text.


