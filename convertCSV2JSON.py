# Name: Sophie Stiekema
# Student number: 10992499
"""
This script reads a CSV file and converts it into a JSON file
"""

import csv
import json
import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

def open_csv(input):
    """
    Converts csv file into a dataframe
    """
    data = pd.read_csv(input, encoding='latin-1', usecols = ['Area Abbreviation', 'Item', 'Element', 'Y1961', 'Y1962', 'Y1963', 'Y1964', 'Y1965', 'Y1966', 'Y1967', 'Y1968', 'Y1969', 'Y1970', 'Y1971', 'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977', 'Y1978', 'Y1979', 'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985', 'Y1986', 'Y1987', 'Y1988', 'Y1989', 'Y1990', 'Y1991', 'Y1992', 'Y1993', 'Y1994', 'Y1995', 'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001', 'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009', 'Y2010', 'Y2011', 'Y2012', 'Y2013' ])
    print(data.head())
    return data

def clean_data(data):
    """
    Clean & preprocess dataframe
    """
    #check for missing data:
    data_null = data[data.isnull().any(axis=1)]
    print(data_null)

    # label misisng data as NaN
    #data = data.mask(data=='unknown')

    # convert numbers to floats
    #data['Pop'] = data['Pop'].str.replace(',', '.')
    #data['Pop'] = data['Pop'].astype(float)

    # remove extra spaces
    #data['Region'] = data['Region'].str.rstrip()

    return data


def save_json(data):
    """
    Convert the dataframe to JSON via a dictionary
    """
    #create a jsonfile
    jsonfile = open('data.json', 'w')

    #data = data.set_index("Area Abbreviation")

    #create a dictionary to store the information & write it to json
    #dic = data.to_dict(orient='index')
    dic = dict(data.set_index('Area Abbreviation').groupby(level=0).apply(lambda  x : x.to_json(orient = 'records')))

    jsonfile.write(json.dumps(dic))

if __name__ == "__main__":

    #open csv file
    data = open_csv("FAO.csv")

    #clean data
    #data = clean_data(data)

    #translate into a json file
    save_json(data)
