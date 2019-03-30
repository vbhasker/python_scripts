import os
import glob
import json
import shutil

try:
    os.mkdir(r'./processed')
except OSError as err:
    print('./processed folder already exist')

subtotal = 0.0

for file_path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(file_path) as f:
        content = json.load(f)
        subtotal += float(content['value'])

    destination = file_path.replace('new', 'processed')
    shutil.move(file_path, destination)
    print(f'Moved file {file_path} to {destination}')

print(f'Receipt subtotal is ${round(subtotal, 2)}')
