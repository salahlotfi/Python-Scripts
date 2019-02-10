#This program is written based on regular expression to count disease (Panic Disoder in this case)
#death counts in a given year. It can be improved to make the disease code and year more interactively, but this is just an example
# that it can be nicely done. The disease code is based on ICDo code characters. 

import re

def diseasedeathCount(filename, diseaseRE, start, end) : # start and end arguments refer to start and end characters that
    #should be used for the disease code in the file. You can refer to CDC documentation for the character positions.
    
    diseasedeathCount = 0
    alldeathCount = 0
    infile = open(filename, "r")
    for line in infile :
        alldeathCount += 1
        if re.search(diseaseRE, line[start:end]) :
            diseasedeathCount += 1
    infile.close()
    return diseasedeathCount, alldeathCount


def main() :
    c,a = diseasedeathCount("Mort99us.dat","F20",161,301)
    print("In the year 1999 there were",c,"deaths due to Panic Disorder,\
 which is",round(100000*c/a,2),"per 100,000")

    c,a = diseasedeathCount("Mort02US.dat", "F20", 162, 302)
    print("In the year 2002 there were",c,"deaths due to Panic Disorder,\
 which is",round(100000*c/a,2),"per 100,000")
       
    c,a = diseasedeathCount("Mort04US.dat", "F20", 164, 304)
    print("In the year 2004 there were",c,"deaths due to Panic Disorder,\
 which is",round(100000*c/a,2),"per 100,000")

    c,a = diseasedeathCount("VS09MORT.DUSMCPUB", "F20", 164, 304)
    print("In the year 2009 there were",c,"deaths due to Panic Disorder,\
 which is",round(100000*c/a,2),"per 100,000")

    c,a = diseasedeathCount("VS14MORT.DUSMCPUB", "F20", 164, 304)
    print("In the year 2014 there were",c,"deaths due to Panic Disorder,\
 which is",round(100000*c/a,2),"per 100,000")

    c,a = diseasedeathCount("VS15MORT.DUSMCPUB", "F20", 164, 304)
    print("In the year 2015 there were",c,"deaths due to Panic Disorder,\
 which is",round(100000*c/a,2),"per 100,000")

    c,a = diseasedeathCount("VS16MORT.DUSMCPUB", "F20", 164, 304)
    print("In the year 2016 there were",c,"deaths due to Panic Disorder,\
 which is",round(100000*c/a,2),"per 100,000")

main()
