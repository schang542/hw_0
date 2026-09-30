import pandas as pd
df = pd.read_csv("nobel-prize-laureates.csv")
df = df[['awardYear', 'category', 'name']]
df.to_csv('nobel-prize-laureates.csv', index=False)