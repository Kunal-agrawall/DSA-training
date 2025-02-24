import pandas as pd

df = pd.DataFrame({
    'country':['India', 'Russia', 'Belarus', 'Ukraine'],
    'population':[140, 14.6, 5, 2.5],
    'square':[2334334, 238778399, 831318, 873278]
})

print(f"Columns : {df.columns}")
print(f"Index   : {df.index}\n")

print(f"Country Data:\n{df['country']}\n") # or print(df.country)

# Assign new Index
df.index = ['IND', 'RU', 'BY', 'UA']
df.index.name = 'Country Code'
print(f"Data with new Index:\n{df}\n")


# Access Index
# loc for index label
# iloc for index position
print(f"Data at IND:          \n{df.loc['IND']}\n")
print(f"Country at IND:       \n{df.loc['IND']['country']}\n")
print(f"Population of IND, RU:\n{df.loc[['IND', 'RU'], 'population']}\n")
print(f"Data at Index 0:      \n{df.iloc[0]}\n")

# Slicing is possible
print(f"Slice:\n{df.loc['IND':'BY', :]}\n") # [row, column]


# Conditioning
print(f"Population > 10:\n{df[df.population>10][['country','square']]}\n")


# Add new column
df['density'] = df['population'] / df['square']
print(f"New Column Added:\n{df}")