# Generate a synthetic dataset with correlated features. Visualize the correlation matrix of a dataset using a heatmap.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
n_samples = 100
n_features = 5

X = np.random.randn(n_samples, 1)
data = np.hstack([X] + [X + np.random.randn(n_samples, 1) * 0.5 for _ in range(n_features - 1)])

columns = [f'Feature_{i+1}' for i in range(n_features)]
df = pd.DataFrame(data, columns=columns)

corr_matrix = df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()
