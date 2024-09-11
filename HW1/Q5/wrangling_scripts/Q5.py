"""
cse6242 s23
Q5.py - utilities to supply data to the templates.

This file contains a pair of functions for retrieving and manipulating data
that will be supplied to the template for generating the table. """
import csv

def username():
    return 'sdiep6'

def data_wrangling():
    with open('data/movies.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        table = list()
        # Feel free to add any additional variables
        ...
        count = 0
        # Read in the header
        for header in reader:
            break
        
        # Read in each row
        for row in reader:
            table.append(row)
            
            # Only read first 100 data rows - [2 points] Q5.4.a
            count +=1
            if count == 100:
                break
        
        # Order table by the last column - [3 points] Q5.4.b
        table.sort(reverse = True, key = lambda x:float(x[2]) )
        print(len(table))
    
    return header, table

