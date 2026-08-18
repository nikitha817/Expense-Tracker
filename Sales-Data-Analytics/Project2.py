import numpy as np
month = np.array(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
def get_sales_data(month, products, sales):
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
    print(f"Sales of {month[0]}: {sales[0]}")
    print("Yearly Sales of each product: ")
    for i, product in enumerate(products):
        yearly_sales = np.sum(sales[:, i])
        print(f"{product}: {yearly_sales}")
    
    return products, sales
def report_sales(products, sales):
    if sales is None or products is None:
        print("Sales data is not available. Please get sales data first.")
        return
    print("=" *50)
    print("Sales Report: ".center(50))
    print("=" *50)
    average_sales_per_product = np.mean(sales, axis=0)
    Yearly_sales_per_product = np.sum(sales, axis=0)
    Highest_sales_product_index = np.argmax(Yearly_sales_per_product)
    print(f"Product with highest sales: {products[Highest_sales_product_index]} with sales of {Yearly_sales_per_product[Highest_sales_product_index]}")
    Lowest_sales_product_index = np.argmin(Yearly_sales_per_product)
    print(f"Product with lowest sales: {products[Lowest_sales_product_index]} with sales of {Yearly_sales_per_product[Lowest_sales_product_index]}")
    print("Average sales per product: ")
    for i, product in enumerate(products):
        print(f"{product}: {average_sales_per_product[i]}")
    print("Yearly Sales per Product: ")
    for i, product in enumerate(products):
        print(f"{product}: {Yearly_sales_per_product[i]}")
    print("=" *50)
    print("Monthly Sales Analysis".center(50))
    print("=" *50)
    print("Total Sales per Month: ")
    total_sales_per_month = np.sum(sales, axis=1)
    for i, total in enumerate(total_sales_per_month):
        print(f"Month {month[i]}: {total}")
    print("Total Sales per Product: ")
    for i, product in enumerate(products):
        print(f"{product}: {Yearly_sales_per_product[i]}")
    best_product = np.argmax(Yearly_sales_per_product)
    worst_product = np.argmin(Yearly_sales_per_product)
    print(f"Best Product: {products[best_product]} with sales of {Yearly_sales_per_product[best_product]}")
    print(f"Worst Product: {products[worst_product]} with sales of {Yearly_sales_per_product[worst_product]}")
    best_sales_month = np.argmax(total_sales_per_month)
    worst_sales_month = np.argmin(total_sales_per_month)
    print(f"Best Sales Month: Month {month[best_sales_month]} with sales of {total_sales_per_month[best_sales_month]}")
    print(f"Worst Sales Month: Month {month[worst_sales_month]} with sales of {total_sales_per_month[worst_sales_month]}")
    sales_performance = np.where(sales > average_sales_per_product, 'sales increased', 'sales decreased')
    print("Sales Performance per Product per Month: ")
    for i, product in enumerate(products):
        print(f"{product}: {sales_performance[:, i]}")
    bonus = np.array([50, 100, 150, 200, 250])
    print("Bonus for each product: ")
    sales = sales + bonus
    print(sales)
    sales= sales + 100
    print(sales)
def profit_analysis(products, sales):
    if sales is None or products is None:
        print("Sales data is not available. Please get sales data first.")
        return
    profit_per_unit = np.array([10000, 15000, 20000, 25000, 30000])
    monthly_profit = sales * profit_per_unit
    total_profit = np.sum(monthly_profit, axis=0)
    most_profitable_product_index = np.argmax(total_profit)
    least_profitable_product_index = np.argmin(total_profit)
    print("=" *50)
    print("Profit Analysis: ".center(50))
    print("=" *50)
    total_profit_per_product = np.sum(monthly_profit, axis=0)
    for i, product in enumerate(products):
        print(f"Total profit for {product}: {total_profit_per_product[i]}")
    print(f"Most Profitable Product: {products[most_profitable_product_index]} with profit of {total_profit[most_profitable_product_index]}")
    print(f"Least Profitable Product: {products[least_profitable_product_index]} with profit of {total_profit[least_profitable_product_index]}")
def growth_analysis(products, sales):
    if sales is None or products is None:
        print("Sales data is not available. Please get sales data first.")
        return
    growth_rate = np.zeros(len(sales))
    for i in range(1, len(sales)):
        growth_rate[i] = (sales[i] - sales[i-1]) / sales[i-1] * 100
    print("=" *50)
    print("Growth Analysis: ".center(50))
    print("=" *50)
    for i, product in enumerate(products):
        print(f"Growth rate for {product}: {growth_rate[i]:.2f}%")
    highest_growth_product_index = np.argmax(growth_rate)
    lowest_growth_product_index = np.argmin(growth_rate)
    print(f"Highest Growth Product: {products[highest_growth_product_index]} with growth rate of {growth_rate[highest_growth_product_index]:.2f}%")
    print(f"Lowest Growth Product: {products[lowest_growth_product_index]} with growth rate of {growth_rate[lowest_growth_product_index]:.2f}%")
def sales_normalization(sales):
    if sales is None:
        print("Sales data is not available. Please get sales data first.")
        return
    normalized_sales = (sales - np.min(sales, axis=0)) / (np.max(sales, axis=0) - np.min(sales, axis=0))
    print("=" *50)
    print("Sales Normalization: ".center(50))
    print("=" *50)
    print(normalized_sales)
def main():
    while True:
        print("=" *50)
        print("Sales Data Analytics".center(50))
        print("1.Get Sales Data\n2.Report Sales\n3.Profit Analysis\n4.Growth Analysis\n5.Sales Normalization\n6.Exit")
        user_input = input("What do you want to do? ").strip()
        if user_input.lower() == '1':
            products, sales = get_sales_data()
        elif user_input.lower() == '2':
            report_sales(products, sales)
        elif user_input.lower() == '3':
            profit_analysis(products, sales)
        elif user_input.lower() == '4':
            growth_analysis(products, sales)
        elif user_input.lower() == '5':
            sales_normalization(sales)
        elif user_input.lower() == '6':
            print("Exiting the program.")
            return
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()