import numpy as np
products = np.array([input("Enter product 1: "), input("Enter product 2: "), input("Enter product 3: "), input("Enter product 4: "), input("Enter product 5: ")])
sales = np.array([[float(input(f"Enter sales for month 1, {products[0]}: ")), float(input(f"Enter sales for month 1, {products[1]}: ")), float(input(f"Enter sales for month 1, {products[2]}: ")), float(input(f"Enter sales for month 1, {products[3]}: ")), float(input(f"Enter sales for month 1, {products[4]}: "))],
                  [float(input(f"Enter sales for month 2, {products[0]}: ")), float(input(f"Enter sales for month 2, {products[1]}: ")), float(input(f"Enter sales for month 2, {products[2]}: ")), float(input(f"Enter sales for month 2, {products[3]}: ")), float(input(f"Enter sales for month 2, {products[4]}: "))],
                  [float(input(f"Enter sales for month 3, {products[0]}: ")), float(input(f"Enter sales for month 3, {products[1]}: ")), float(input(f"Enter sales for month 3, {products[2]}: ")), float(input(f"Enter sales for month 3, {products[3]}: ")), float(input(f"Enter sales for month 3, {products[4]}: "))],
                  [float(input(f"Enter sales for month 4, {products[0]}: ")), float(input(f"Enter sales for month 4, {products[1]}: ")), float(input(f"Enter sales for month 4, {products[2]}: ")), float(input(f"Enter sales for month 4, {products[3]}: ")), float(input(f"Enter sales for month 4, {products[4]}: "))],
                  [float(input(f"Enter sales for month 5, {products[0]}: ")), float(input(f"Enter sales for month 5, {products[1]}: ")), float(input(f"Enter sales for month 5, {products[2]}: ")), float(input(f"Enter sales for month 5, {products[3]}: ")), float(input(f"Enter sales for month 5, {products[4]}: "))],
                  [float(input(f"Enter sales for month 6, {products[0]}: ")), float(input(f"Enter sales for month 6, {products[1]}: ")), float(input(f"Enter sales for month 6, {products[2]}: ")), float(input(f"Enter sales for month 6, {products[3]}: ")), float(input(f"Enter sales for month 6, {products[4]}: "))],
                  [float(input(f"Enter sales for month 7, {products[0]}: ")), float(input(f"Enter sales for month 7, {products[1]}: ")), float(input(f"Enter sales for month 7, {products[2]}: ")), float(input(f"Enter sales for month 7, {products[3]}: ")), float(input(f"Enter sales for month 7, {products[4]}: "))],
                  [float(input(f"Enter sales for month 8, {products[0]}: ")), float(input(f"Enter sales for month 8, {products[1]}: ")), float(input(f"Enter sales for month 8, {products[2]}: ")), float(input(f"Enter sales for month 8, {products[3]}: ")), float(input(f"Enter sales for month 8, {products[4]}: "))],
                  [float(input(f"Enter sales for month 9, {products[0]}: ")), float(input(f"Enter sales for month 9, {products[1]}: ")), float(input(f"Enter sales for month 9, {products[2]}: ")), float(input(f"Enter sales for month 9, {products[3]}: ")), float(input(f"Enter sales for month 9, {products[4]}: "))],
                  [float(input(f"Enter sales for month 10, {products[0]}: ")), float(input(f"Enter sales for month 10, {products[1]}: ")), float(input(f"Enter sales for month 10, {products[2]}: ")), float(input(f"Enter sales for month 10, {products[3]}: ")), float(input(f"Enter sales for month 10, {products[4]}: "))],
                  [float(input(f"Enter sales for month 11, {products[0]}: ")), float(input(f"Enter sales for month 11, {products[1]}: ")), float(input(f"Enter sales for month 11, {products[2]}: ")), float(input(f"Enter sales for month 11, {products[3]}: ")), float(input(f"Enter sales for month 11, {products[4]}: "))],
                  [float(input(f"Enter sales for month 12, {products[0]}: ")), float(input(f"Enter sales for month 12, {products[1]}: ")), float(input(f"Enter sales for month 12, {products[2]}: ")), float(input(f"Enter sales for month 12, {products[3]}: ")), float(input(f"Enter sales for month 12, {products[4]}: "))]])
print(f"Sales data shape: {sales.shape}")
print(f"Sales data type: {sales.dtype}")
print("=" *50)
print("Sales Data Analysis".center(50))
print("=" *50)
print(f"Sales of January: {sales[0]}")
print("Yearly Sales of each product: ")
for i, product in enumerate(products):
    yearly_sales = np.sum(sales[:, i])
    print(f"{product}: {yearly_sales}")
Highest_sales_product_index = np.argmax(np.sum(sales, axis=0))
#print(f"Product with highest sales: {products[Highest_sales_product_index]} with sales of {np.sum(sales[:, Highest_sales_product_index])}")
Lowest_sales_product_index = np.argmin(np.sum(sales, axis=0))
#print(f"Product with lowest sales: {products[Lowest_sales_product_index]} with sales of {np.sum(sales[:, Lowest_sales_product_index])}")
average_sales_per_product = np.mean(sales, axis=0)
#print("Average sales per product: ")
#for i, product in enumerate(products):
#    print(f"{product}: {average_sales_per_product[i]}")
Yearly_sales_per_product = np.sum(sales, axis=0)
print("Yearly Sales per Product: ")
#for i, product in enumerate(products):
#    print(f"{product}: {Yearly_sales_per_product[i]}")
print("=" *50)
print("Monthly Sales Analysis".center(50))
print("=" *50)
print("Total Sales per Month: ")
total_sales_per_month = np.sum(sales, axis=1)
for i, total in enumerate(total_sales_per_month):
    print(f"Month {i+1}: {total}")
print("Total Sales per Product: ")
for i, product in enumerate(products):
    print(f"{product}: {Yearly_sales_per_product[i]}")
best_product = np.argmax(Yearly_sales_per_product)
worst_product = np.argmin(Yearly_sales_per_product)
print(f"Best Product: {products[best_product]} with sales of {Yearly_sales_per_product[best_product]}")
print(f"Worst Product: {products[worst_product]} with sales of {Yearly_sales_per_product[worst_product]}")
best_sales_month = np.argmax(total_sales_per_month)
worst_sales_month = np.argmin(total_sales_per_month)
print(f"Best Sales Month: Month {best_sales_month + 1} with sales of {total_sales_per_month[best_sales_month]}")
print(f"Worst Sales Month: Month {worst_sales_month + 1} with sales of {total_sales_per_month[worst_sales_month]}")
sales_performance = np.where(sales > average_sales_per_product, "Above Average", "Below Average")
print("Sales Performance per Product per Month: ")
for i, product in enumerate(products):
    print(f"{product}: {sales_performance[:, i]}")
product_yearly_sales_exceeding = np.where(Yearly_sales_per_product > np.sum(Yearly_sales_per_product) / len(Yearly_sales_per_product), products, None)
print("Products with Yearly Sales Exceeding : ")
for product in product_yearly_sales_exceeding:
    if product is not None:
        print(product)
monthly_sales_whose_exceeding = np.where(total_sales_per_month > np.sum(total_sales_per_month) / len(total_sales_per_month), [f"Month {i+1}" for i in range(len(total_sales_per_month))], None)
print("Months with Total Sales Exceeding : ")
for month in monthly_sales_whose_exceeding:
    if month is not None:
        print(month)
products_sold = np.where(sales > 0, products, None)
print("Products with Sales Recorded: ")
for product in products_sold:
    if product is not None:
        print(product)
bonus = np.array([50, 100, 150, 200, 250])
print("Bonus for each product: ")
for i, sales in enumerate(Yearly_sales_per_product):
    if sales > 1000:
        print(f"{products[i]}: {bonus[i]}")