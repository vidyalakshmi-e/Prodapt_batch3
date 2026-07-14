stores=3
days=7
store = []   
for i in range(stores):
    store_sales = []
    total_sales = 0
    print(f"Store {i+1}")
    for j in range(days):
        sale = int(input(f"Enter sales for Store {i+1} on Day {j+1}: "))
        store_sales.append(sale)
        total_sales += sale

    store.append(store_sales)

    print(f"Total sales of Store {i+1}: {total_sales}")

print("\nSales data:")
print(store)