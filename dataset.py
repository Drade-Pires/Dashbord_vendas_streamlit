import json
import pandas as pd
import os

file_path = os.path.join('dados', 'vendas.json')
with open(file_path, 'r') as file:
    data = json.load(file)



df = pd.DataFrame.from_dict(data)


df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')


file.close()
