import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('world_population.csv')
print(data.head(10))

plt.figure(figsize=(12,8))
data.head(500).boxplot(column='Growth Rate', by='Continent')
plt.suptitle('')
plt.title('Country growth rates by continent')
plt.xlabel('Continent')
plt.ylabel('Growth rate')
plt.xticks(rotation=90)
plt.show()