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
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["fname","lname","sex","ID#","year lvl","program code"])
        writer.writerows(data)
def load_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        return list(reader)
    