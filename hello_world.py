import csv
import json
from pathlib import Path

#data_folder = Path(sys.environ.get('KBC_DATADIR'))
data_folder = Path('./data')

source_file_path = Path('data/in/tables/input.csv')
result_file_path = Path('data/out/tables/output.csv')

#source_file_path = data_folder.joinpath('in/tables/input.csv')
#result_file_path = data_folder.joinpath('out/tables/output.csv')

#config = json.load(open(data_folder.joinpath('config.json')))
#param_print_lines = config['parameters']['print_rows']

print('Running')

with open(source_file_path, 'r') as input, open(result_file_path, 'w+', newline='') as out:
    reader = csv.DictReader(input)
    new_columns = reader.fieldnames

    new_columns.append('row_number')
    writer = csv.DictWriter(out, fieldnames=new_columns, lineterminator='\n', delimiter = ',')
    writer.writeheader()
    for index, l in enumerate(reader):
        #if param_print_lines:
            #print(f'Printing line {index}: {l}')
        l['row_number'] = index
        writer.writerow(l)
print('done')