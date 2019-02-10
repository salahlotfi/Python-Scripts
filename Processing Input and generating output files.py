# This program removes names and email addresses occurring in a given input file and saves it in an output file.

import re
def deidentify():
    infilename = input("Give the input file name: ")
    outfilename = input("Give the output file name: ")
    name = str (input("What name/deidentifier do you want to replace the names with in the file?"))
    email = str (input("What email deidentifier do you want to use as the replacement in the file?"))

    infile = open(infilename,"r")
    text = infile.read()
    infile.close()

    # replace names
    nameRE = "(Ms\.|Mr\.|Dr\.|Prof\.|Miss\.) [A-Z](\.|[a-z]+) [A-Z](\.|[a-z]+) [A-Z][a-z]+" # improve this regular expression  \s[A-Z](\.|[a-z])
    deidentified_text = re.sub(nameRE,name,text)
    emailRE = "\w+@(\w+\.)+(edu|com|org)"
    deidentified_email = re.sub (emailRE,email,deidentified_text)


    outfile = open(outfilename,"w")
    print(deidentified_email, file=outfile)
    outfile.close()
    

deidentify()
