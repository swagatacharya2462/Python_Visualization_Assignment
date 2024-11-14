import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Seed and Data Generation
np.random.seed(20)
data = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}

df = pd.DataFrame(data)

# Pivot the data to create a matrix of sales
pivot_df = df.pivot_table(index='Day', columns='Month', values='Sales', aggfunc='sum')

# Plotting the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, cmap='coolwarm', cbar_kws={'label': 'Total Sales'})
plt.title('Heatmap of Sales Variation Across Months and Days')
plt.ylabel('Day of Month')
plt.xlabel('Month')
plt.show()
