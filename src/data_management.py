import json
import csv
import os


FNAME = 0
LNAME = 1
SEX = 2
ID = 3
YRLVL = 4
CCODE = 5
PCODE = 6

def write_data(filename, data):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["fname","lname","sex","ID#","year lvl","program code"])
        writer.writerows(data)
def load_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        return list(reader)
    

def write_data_json(filename, newfile):
    if os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(newfile, f, indent=4)    
def load_data_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
    return data 

