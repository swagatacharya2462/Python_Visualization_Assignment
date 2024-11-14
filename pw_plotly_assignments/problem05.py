import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(25)
data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Population': np.random.randint(100, 1000, 5),
    'GDP': np.random.randint(500, 2000, 5)
}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
plt.scatter(df['GDP'], df['Population'], s=df['Population']*10, alpha=0.5)

for i, country in enumerate(df['Country']):
    plt.text(df['GDP'][i] + 20, df['Population'][i] + 20, country)

plt.xlabel('GDP')
plt.ylabel('Population')
plt.title('Bubble Chart: Country Population vs GDP')

plt.show()
