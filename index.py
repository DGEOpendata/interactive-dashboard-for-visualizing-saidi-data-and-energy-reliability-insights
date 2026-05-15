python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the SAIDI dataset
data = pd.read_csv('SAIDI.csv')

# Convert year to datetime for better plotting
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Create a line plot of SAIDI data
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Year', y='SAIDI', marker='o', label='SAIDI')
plt.title('SAIDI (System Average Interruption Duration Index) Over Time')
plt.xlabel('Year')
plt.ylabel('SAIDI (Minutes per Customer)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('SAIDI_Trend.png')
plt.show()

# Generate a CSV report for further analysis
summary = data.describe()
summary.to_csv('SAIDI_Summary_Report.csv')

print("Visualization and summary report generated successfully!")
