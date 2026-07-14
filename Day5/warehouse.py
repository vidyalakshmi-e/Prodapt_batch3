products=[]
#add products to the list
product_qunatity=int(input("\nEnter the product qunatity:"))
for i in range(product_qunatity):
    name=input("Enter the product name:")
    products.append(name)
print(products)

#insert urgent product
u_product_name=input("\nEnter the urgent product name:")
products.append(u_product_name)
print(products)

#combine products from warehouse
print("\nNew warehouse")
new_products=[]
n_qun=int(input("Enter the new product qunatity:"))
for i in range(n_qun):
    name=input("Enter the new product name:")
    new_products.append(name) 
print("New products: ",new_products)  
products.extend(new_products)
print(products)

#remove discontinued product
dis_name=input("\nEnter the discontinued product name:")
print("The warehouse stops selling :",dis_name)
products.remove(dis_name)
print(products)

#process shipped product
ship_product=input("\nEnter the product to be shipped: ")
print("The last product",ship_product,"is shipped")
products.remove(ship_product)
print(products)

#count product appearance
c=0
c_product=input("\nEnter the product name to count: ")
for i in products:
    if i==c_product:
        c+=1
print("Count of",c_product,"is:",c)

#find product position
pos_product=input("\nEnter the product name to find its position: ")
inx=0
for i in products:
    if i==pos_product:
        print("Position of",pos_product,"is:",inx)
        break
    inx+=1
    

#sort product
print("Sorted products: " , sorted(products))

#reverse product
print("Reverse products: ", products[::-1])

#copy
product_copy=products.copy()
print("Copy of products: " , product_copy)

#clear
print("clearing the temporary list")
product_copy.clear()
