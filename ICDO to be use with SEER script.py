# This script should be used with SEED script processing.
# The purpose of the function is to make a dictionary from ICDO codes and store the codes as keys and
# disease name as values. 
import re

def ICDO_dictionary():
 
    d = {}

    infile = open("icdo3.txt","r")
    for line in infile:
        # This regular expression will read the codes and disease names
        r = re.search("(\d+/\d+)\s+(.+)",line)
     
        if (r) :
            code = r.group(1)
            code = code.replace("/","")
            disease = r.group(2)
            disease=disease.rstrip()
            disease = disease.lower()
            d[code] = disease

    infile.close()
    return d        

def query_ICDO_dictionary():

    di = ICDO_dictionary()

    #This loop goes through every single line and finds the input code, and print it.
    while (True):
        code = input("Give the code without slash (empty to quit): ")
        if (code=="") :
            break
        if code in di:
            print("The disease is: ",di[code],"\n")
        else:
             print("The code does not exist in ICD-O.\n")
