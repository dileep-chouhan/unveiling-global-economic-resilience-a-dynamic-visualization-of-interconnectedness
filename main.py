import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
num_countries = 10
num_years = 5
countries = [f'Country {i}' for i in range(1, num_countries + 1)]
years = range(2019, 2019 + num_years)
data = {
    'Country': [],
    'Year': [],
    'GDP_Growth': [],
    'Inflation': [],
    'Unemployment': []
}
for country in countries:
    for year in years:
        data['Country'].append(country)
        data['Year'].append(year)
        data['GDP_Growth'].append(np.random.normal(loc=2, scale=1)) # Simulate GDP growth
        data['Inflation'].append(np.random.normal(loc=2, scale=0.5)) # Simulate inflation
        data['Unemployment'].append(np.random.normal(loc=5, scale=2)) # Simulate unemployment
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Analysis ---
# (In a real-world scenario, this section would involve more extensive data cleaning)
df['GDP_Growth'] = df['GDP_Growth'].clip(lower=0) # Ensure GDP growth is non-negative.
df['Inflation'] = df['Inflation'].clip(lower=0) # Ensure inflation is non-negative.
df['Unemployment'] = df['Unemployment'].clip(lower=0) # Ensure unemployment is non-negative.
# Calculate average values over the years for each country.
average_data = df.groupby('Country')[['GDP_Growth', 'Inflation', 'Unemployment']].mean()
# --- 3. Visualization ---
# Correlation Matrix
correlation_matrix = average_data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix of Economic Indicators')
plt.savefig('correlation_matrix.png')
print("Plot saved to correlation_matrix.png")
# GDP Growth Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='GDP_Growth', data=average_data.reset_index())
plt.title('Average GDP Growth by Country')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('gdp_growth.png')
print("Plot saved to gdp_growth.png")
#Further visualizations could be added here to explore other relationships and insights.  For example, a scatter plot matrix could show relationships between all three variables.  A more sophisticated dashboard could be built using libraries like Plotly Dash.