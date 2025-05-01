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

def write_data(filename, data, int=0):
    v = ["fname","lname","sex","ID#","year lvl","program code"]
    if int == 1:
        v = ["College","Course Code","Course Name"]
    elif int == 2:
        v = ["College Name", "College Code"]
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(v)
        writer.writerows(data)
def load_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        return list(reader)
    