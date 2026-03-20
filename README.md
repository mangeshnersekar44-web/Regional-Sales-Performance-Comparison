# Regional-Sales-Performance-Comparison
📌 Project Overview

This project focuses on analyzing regional sales data to uncover business insights, evaluate performance, and improve profitability. It combines data analysis, visualization, and machine learning to support data-driven decision-making.

🎯 Objectives

Analyze sales and profit performance across regions and products

Identify key factors impacting profitability

Evaluate the effect of discount strategies

Build an interactive Power BI dashboard

Develop machine learning models for profit prediction

🛠️ Tools & Technologies

Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)

MySQL (Data querying & analysis)

Power BI (Dashboard & visualization)

📂 Dataset Description

The dataset contains ~5200 records with the following fields:

Order Details: Order_ID, Order_Date, Ship_Date

Sales Info: Total_Revenue, Profit, Discount_Percent

Product Info: Product_Category, Product_Name

Customer Info: Customer_Name, Customer_Segment

Location: Region, State, City

Operations: Sales_Channel, Warehouse_Code, Sales_Rep

🔧 Data Processing

Converted date columns into datetime format

Handled missing values and duplicates

Created new features:

Delivery Days

Profit Margin

Year & Month

Converted categorical variables for machine learning

📊 Exploratory Data Analysis (EDA)

Sales performance by region

Profit distribution by product category

Top-performing sales representatives

Impact of discounts on profit

Monthly sales trends

📈 Power BI Dashboard

A one-page interactive dashboard was built with:

KPIs: Total Sales, Total Profit, Profit Margin, Total Orders

Visuals:

Sales by Region (Bar Chart)

Sales by Category (Donut Chart)

Monthly Sales Trend (Line Chart)

Discount vs Profit (Scatter Plot)

Top Sales Representatives

Filters (Slicers):

Region

Product Category

Sales Rep

Year

🧠 Machine Learning
Models Used:

Linear Regression

Random Forest Regressor

Logistic Regression (for classification)

Tasks:

Predict profit using regression models

Classify low-profit vs high-profit transactions

🔍 Key Insights

Higher discounts significantly reduce profitability

Certain regions generate high sales but lower profit margins

A small number of sales representatives drive most revenue

Product category plays a major role in profitability

Delivery time impacts operational efficiency

📁 Project Structure
regional-sales-analysis/
│
├── data/
├── notebook/
├── dashboard/
├── images/
├── README.md
└── requirements.txt
🚀 Business Impact

Helps identify high-performing regions and products

Supports better pricing and discount strategies

Enables data-driven decision-making

Improves overall business performance monitoring

📌 Conclusion

This project demonstrates how data analytics and machine learning can be used together to generate actionable business insights and improve strategic decision-making.

👨‍💻 Author

Mangesh Nersekar
Aspiring Data Analyst
