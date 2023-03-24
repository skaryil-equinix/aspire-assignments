import pandas as pd

df = pd.read_csv('input_file.csv')

odd_rows = df.iloc[::2]
even_rows = df.iloc[1::2]

odd_rows.to_csv('odd_rows.csv', index=False)
even_rows.to_csv('even_rows.csv', index=False)