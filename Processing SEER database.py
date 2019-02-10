#This script is written to process the SEER database. Using different age groups between men and women,
#This script can provide frequency distribution of various cancer diagnoses given the years data is collected.

import glob

import icdo # Used another script called icdo to process dictionary. This script and icdo should be in the same folder.
import icdo.nodot # this is another variant of icdo with removed Dot. 


def main():
    # Here you impor the file, and make a list of all the relevant file names in the SEER dataset folder.
    # By playing around with year and month using "*" character, you can choice the year of interest. 
    filelist = glob.glob("SEER_1973_2015_TEXTDATA/incidence/yr*/*.TXT")

    di = {} # setting up the dictionary to store 8 types of cancers (age groups * gender)
           

    for file in filelist:  # the initial process of each each file
        infile = open(file,"r")
        for line in infile:
            disease = line[52:57] # The character position (52:57) obtained from ICD-Oncology-3 code (Histology+Behavior) 
            gender = line[23]
            age = int(line[24:27])
            # index is the location in the list which needs to be updated
            if gender=="1" : # men... 1 is a string here. 
                if age < 25 :
                    index = 0
                elif age < 50 :
                    index = 2
                elif age < 75 :
                    index = 4
                elif age < 131:
                    index = 6
            if gender=="2" : # women
                if age < 25 :
                    index = 1
                elif age < 50 :
                    index = 3
                elif age < 75 :
                    index = 5
                elif age < 131 :
                    index = 7
            if disease in di :
                di[disease][index] += 1
            else :
                di[disease] = [0]*8 # Making a list of eight zeros to be appended
                di[disease][index] += 1
        infile.close()

    icdo_di = icdo.ICDO_dictionary() # Now using icdo dictionary (the ICD-O)to get the names for the codes

    outfile = open("output.csv","w")
    print("Cancer type, Men 0-24, Women 0-24, Men 25-49, Women 25-49, Men 50-74, Women 50-74, Men 75+ , Women 75+",file=outfile)
    for code in icdo_di:
        if code in di :
            counts = di[code]
            s = icdo_di[code].replace(",","") # making the string to be printed
            for count in counts :
                s += "," + str(count) # concatenate to that string
        print(s, file=outfile)
    outfile.close()

main()
