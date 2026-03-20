# ================================
# 1. IMPORT LIBRARIES
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, accuracy_score, classification_report, confusion_matrix

# ================================
# 2. LOAD DATA
# ================================
df = pd.read_csv("regional_sales_performance.csv")

# ================================
# 3. DATA CLEANING
# ================================
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'])

df = df.drop_duplicates()

# Convert numeric columns safely
df['Total_Revenue'] = pd.to_numeric(df['Total_Revenue'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Discount_Percent'] = pd.to_numeric(df['Discount_Percent'], errors='coerce')

print(df.info())
print(df.isnull().sum())

# ================================
# 4. FEATURE ENGINEERING
# ================================
df['Delivery_Days'] = (df['Ship_Date'] - df['Order_Date']).dt.days

# Avoid division by zero
df['Profit_Margin'] = (df['Profit'] / df['Total_Revenue'].replace(0, np.nan)) * 100

df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month

# ✅ FIXED CLASSIFICATION TARGET (balanced)
threshold = df['Profit'].median()
df['Is_Low_Profit'] = df['Profit'].apply(lambda x: 1 if x < threshold else 0)

print("Class Distribution:\n", df['Is_Low_Profit'].value_counts())

# ================================
# 5. EDA
# ================================
print(df.groupby('Region')['Total_Revenue'].sum().sort_values(ascending=False))
print(df.groupby('Product_Category')['Profit'].sum())
print(df.groupby('Sales_Rep')['Total_Revenue'].sum().sort_values(ascending=False).head(10))
print(df[['Discount_Percent', 'Profit']].corr())

# ================================
# 6. VISUALIZATION
# ================================
plt.figure()
sns.barplot(x='Region', y='Total_Revenue', data=df)
plt.title("Sales by Region")
plt.xticks(rotation=45)
plt.show()

plt.figure()
sns.scatterplot(x='Discount_Percent', y='Profit', data=df)
plt.title("Discount vs Profit")
plt.show()

plt.figure()
df.groupby('Month')['Total_Revenue'].sum().plot()
plt.title("Monthly Sales Trend")
plt.show()

# ================================
# 7. DATA PREPARATION FOR ML
# ================================
df_ml = df.copy()

# Select only useful columns
df_ml = df_ml[['Total_Revenue', 'Discount_Percent', 'Delivery_Days',
               'Product_Category', 'Region', 'Profit', 'Is_Low_Profit']]

# Encode categorical variables
df_ml = pd.get_dummies(df_ml, drop_first=True)

# Features & targets
X = df_ml.drop(['Profit', 'Is_Low_Profit'], axis=1)
y_reg = df_ml['Profit']
y_clf = df_ml['Is_Low_Profit']

# Train-test split
X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)
_, _, y_train_clf, y_test_clf = train_test_split(X, y_clf, test_size=0.2, random_state=42)

# ================================
# 8. REGRESSION MODEL (LINEAR)
# ================================
lr = LinearRegression()
lr.fit(X_train, y_train_reg)

y_pred_lr = lr.predict(X_test)

print("\n--- Linear Regression ---")
print("R2 Score:", r2_score(y_test_reg, y_pred_lr))
print("MAE:", mean_absolute_error(y_test_reg, y_pred_lr))

# ================================
# 9. REGRESSION MODEL (RANDOM FOREST)
# ================================
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train_reg)

y_pred_rf = rf.predict(X_test)

print("\n--- Random Forest ---")
print("R2 Score:", r2_score(y_test_reg, y_pred_rf))

# ================================
# 10. CLASSIFICATION MODEL
# ================================
# Safety check
if len(y_train_clf.unique()) < 2:
    print("\n⚠️ Only one class present. Skipping classification.")
else:
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train_clf)

    y_pred_clf = clf.predict(X_test)

    print("\n--- Classification Model ---")
    print("Accuracy:", accuracy_score(y_test_clf, y_pred_clf))
    print(classification_report(y_test_clf, y_pred_clf))

    # Confusion Matrix
    cm = confusion_matrix(y_test_clf, y_pred_clf)

    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

# ================================
# 11. FEATURE IMPORTANCE
# ================================
feature_importance = pd.Series(rf.feature_importances_, index=X.columns)
feature_importance = feature_importance.sort_values(ascending=False)

print("\nTop 10 Important Features:")
print(feature_importance.head(10))

plt.figure()
feature_importance.head(10).plot(kind='bar')
plt.title("Top Features")
plt.show()

print("\n--- Regional Sales Performance Analysis Completed ---")