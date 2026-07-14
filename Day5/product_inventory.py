categories=3
products=2
inventory = []

for i in range(categories):
    products_list = []
    category_name=input("\nEnter the category name:")
    for j in range(products):
        product_name=input("Enter the product name:")
        product_quantity=int(input("Qunatity: "))
        products_list.append([product_name, product_quantity])

    inventory.append([category_name, products_list])

for i in inventory:
    print("\nCategory: ",inventory[i][0])
    for j in inventory[i][1]:
        print(inventory[i][j][0],": ",inventory[i][j][1])   

