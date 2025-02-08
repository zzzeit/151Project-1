import json
import os


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
    return data 

def write_data(filename, newfile):
    if os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(newfile, f, indent=4)

def sortDb(file):
    write_data("./database/students.json", sorted(file, key=lambda s: s['lname']))

class Student:
    def __init__(self, database, ID):
        print(database[0])
        # sortDb(database)