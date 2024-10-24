import pandas as pd

input_csv = pd.read_csv('test.csv')

deleate_columns = ['название колонки', 'название колонки', 'название колонки']
input_csv.drop(deleate_columns, axis=1, inplace=True)
input_csv.to_csv('test.csv', index=False)