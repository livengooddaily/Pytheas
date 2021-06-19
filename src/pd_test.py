import os
from pprint import pprint

import pandas as pd

from pytheas import pytheas

Pytheas = pytheas.API()

#load pretrained rule weights
Pytheas.load_weights('pytheas/trained_rules.json')

directory = '../data/open_data/hypoparsr/original/'

for file in os.listdir(directory):
    filepath = directory + file
    file_name = file.split('/')[-1].split('.')[0]

    print('PROCESSING:', file_name)

    try:
        file_annotations = Pytheas.infer_annotations(filepath, max_lines=500)
        delimiter = file_annotations['discovered_delimiter']

        cnt = 1
        for table in file_annotations["tables"]:
            header = table['header']
            #if isinstance(header, list):
            nrows = table['data_end']
            df = pd.read_csv(filepath, delimiter=delimiter, header=header, nrows=nrows)
            print(df.head())
            df.to_csv(f'./results/{file_name}_{cnt}.csv', index=False)
            cnt += 1
    except Exception as e:
        print(f"***ERROR***\nFile: {file_name}\n{e}")
        pass
