import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(15)
data = {
    'Grade': np.random.choice(['A', 'B', 'C', 'D', 'F'], 200),
    'Score': np.random.randint(50, 100, 200)
}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
sns.violinplot(x='Grade', y='Score', data=df)
plt.title('Distribution of Scores Across Different Grades')
plt.show()

np.random.seed(20)
data = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}
df_sales = pd.DataFrame(data)

sales_pivot = df_sales.pivot_table(index='Day', columns='Month', values='Sales', aggfunc='mean')

plt.figure(figsize=(10, 8))
sns.heatmap(sales_pivot, annot=True, cmap='YlGnBu', fmt='.0f', linewidths=0.5)
plt.title('Sales Variation Across Different Months and Days')
plt.show()
