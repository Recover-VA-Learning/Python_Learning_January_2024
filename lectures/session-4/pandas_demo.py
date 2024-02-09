import pandas as pd

# Create a DataFrame
data = {'Name': ['Tim', 'Stuart', 'Ally', 'Kierra'],
        'Age': [36, 28, 25, 25],
        'City': ['St Paul', 'St Paul', 'Plymouth', 'Minneapolis']}
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Accessing columns
print("\nAccessing columns:")
print(df['Name'])
print(df.Age)

# Accessing rows
print("\nAccessing rows:")
print(df.loc[0])
print(df.iloc[2])

# Filtering data
print("\nFiltering data:")
filtered_df = df[df['Age'] > 28]
print(filtered_df)

# Adding a new column
df['Group'] = ['Design', 'Design', 'Research', 'Research']
print("\nDataFrame with a new column:")
print(df)

# Grouping data
print("\nGrouping data:")
grouped_df = df.groupby('Group').count()
print(grouped_df)
