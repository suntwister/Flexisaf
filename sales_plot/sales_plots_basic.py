import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv("sales_plot\company_sales_data.csv")

# Line plot for total profit
plt.plot(data['month_number'], data['total_profit'], marker='o')
plt.title("Company Profit per Month")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()


# # Subplots for Bathing soap and Facewash
plt.subplot(2, 1, 1)   # 2 rows, 1 column, first plot
plt.plot(data['month_number'], data['bathingsoap'], marker='o')
plt.title("Bathing Soap Sales")

plt.subplot(2, 1, 2)   # second plot
plt.plot(data['month_number'], data['facewash'], marker='o')
plt.title("Facewash Sales")

plt.tight_layout()
plt.show()
