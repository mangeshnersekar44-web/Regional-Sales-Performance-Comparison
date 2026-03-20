-- Active: 1772520994257@@127.0.0.1@3306@sales_analysis
SELECT * FROM regional_sales LIMIT 10;

SELECT COUNT(*) FROM regional_sales;

SELECT DISTINCT Region FROM regional_sales;

#🔹 Total Sales
SELECT SUM(Total_Revenue) AS Total_Sales FROM regional_sales;

#🔹 Total Profit
SELECT SUM(Profit) AS Total_Profit FROM regional_sales;

#🔹 Profit Margin
SELECT 
    (SUM(Profit) / SUM(Total_Revenue)) * 100 AS Profit_Margin
FROM regional_sales;

#🔹 Sales by Region
SELECT 
    Region,
    SUM(Total_Revenue) AS Sales
FROM regional_sales
GROUP BY Region
ORDER BY Sales DESC;

#🔹 Profit by Category
SELECT 
    Product_Category,
    SUM(Profit) AS Profit
FROM regional_sales
GROUP BY Product_Category
ORDER BY Profit DESC;

#🔹 Top 10 Sales Reps
SELECT 
    Sales_Rep,
    SUM(Total_Revenue) AS Sales
FROM regional_sales
GROUP BY Sales_Rep
ORDER BY Sales DESC
LIMIT 10;

#🔹 Monthly Sales Trend
SELECT 
    MONTH(Order_Date) AS Month,
    SUM(Total_Revenue) AS Sales
FROM regional_sales
GROUP BY Month
ORDER BY Month;

#🔹 Discount Impact
SELECT 
    Discount_Percent,
    AVG(Profit) AS Avg_Profit
FROM regional_sales
GROUP BY Discount_Percent
ORDER BY Discount_Percent;

#🔹 Delivery Time
SELECT 
    AVG(DATEDIFF(Ship_Date, Order_Date)) AS Avg_Delivery_Days
FROM regional_sales;

#🔹 Revenue per Customer Segment
SELECT 
    Customer_Segment,
    SUM(Total_Revenue) AS Revenue
FROM regional_sales
GROUP BY Customer_Segment;

#🔹 Profit Category (CASE WHEN)
SELECT *,
    CASE 
        WHEN Profit < (SELECT AVG(Profit) FROM regional_sales)
        THEN 'Low Profit'
        ELSE 'High Profit'
    END AS Profit_Category
FROM regional_sales;

#🔹 Top Region by Profit
SELECT Region, SUM(Profit) AS Total_Profit
FROM regional_sales
GROUP BY Region
ORDER BY Total_Profit DESC
LIMIT 1;

#🔹 Most Profitable Product
SELECT Product_Name, SUM(Profit) AS Profit
FROM regional_sales
GROUP BY Product_Name
ORDER BY Profit DESC
LIMIT 1;

#🔹 Top Sales Rep per Region
SELECT *
FROM (
    SELECT 
        Region,
        Sales_Rep,
        SUM(Total_Revenue) AS Sales,
        RANK() OVER (PARTITION BY Region ORDER BY SUM(Total_Revenue) DESC) AS rnk
    FROM regional_sales
    GROUP BY Region, Sales_Rep
) t
WHERE rnk = 1;

#🔹 Identify Loss Risk Orders
SELECT 
    *,
    CASE 
        WHEN Discount_Percent > 20 THEN 'High Risk'
        WHEN Discount_Percent BETWEEN 10 AND 20 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS Risk_Level
FROM regional_sales;