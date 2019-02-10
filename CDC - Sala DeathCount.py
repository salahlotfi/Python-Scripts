# This script is created to count the number of deaths
# given diseases in a given year reported by CDC database.
# The disease codes are obtained from ICDO dictionary, so you need to put
# the icd_nodot script as well as database file in the same folder. The final file is a .CSV file.

import icd_nodot

def main() :
    dictionary = {} # This death_causes.ctionary holds cause of death as keys and counts as values.
            
    infile = open("Mort99us.dat","r") # This is a sample CDC file, correspondeath_causes.gn to 1999.
    for line in infile:
        death_causes= line[161:301]   # Character 161:301 will read the causes of death.
        cause_list = death_causes.split() # to split the causes with space 
        for cause in cause_list :   # for each cause
            a = cause[2:]   # Slice and grab any character after 2. 
            dictionary[a] = dictionary.get(a,0) + 1  # append all cauases to the dictionary. 
    infile.close()

    icddictionary = icd_nodot.ICD_dictionary() # This function uses ICD dictionary with dots removed from codes to find diseases name and write it.
    outfile = open("CDC_out.csv","w")
    for key in dictionary:
        if (key in icddictionary): # These two lines write disease name if the code is known. Otherwise, write only the key.
            print(dictionary[key],",",icddictionary[key].replace(",",""),file=outfile) 
        else:
            print(dictionary[key],",",key,file=outfile) 
    outfile.close()        


main()
        
        
