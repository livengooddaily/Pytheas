from pprint import pprint

import pandas as pd

from pytheas import pytheas

Pytheas = pytheas.API()

#load pretrained rule weights
Pytheas.load_weights('pytheas/trained_rules.json')

filepath = '../data/Upload___Buergschaftsregister_fuer_HmbTG_31.12.2015_.csv'
file_annotations = Pytheas.infer_annotations(filepath)
delimiter = file_annotations['discovered_delimiter']
pprint(file_annotations)

cnt = 1
for table in file_annotations["tables"]:
    header = table['header']
    nrows = table['data_end']
    df = pd.read_csv(filepath, delimiter=delimiter, header=header, nrows=nrows)
    df.to_csv(f'./results/csv{cnt}.csv')
    cnt += 1
