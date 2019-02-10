# This program counts number of deaths cauased by Panic Disorder
# between black and white races in 2010. 
 

def main() :
    infile = open("Mort10us.dat","r")
    wcount = 0
    bcount = 0
    wpanic = 0
    bpanic = 0
    for line in infile: # for each record
        race = line[59:61] # read the race
        if (race == "01"):
            wcount += 1
        elif (race == "02") :
            bcount += 1
        causes = line[161:301]   # read the causes
        if (causes.count("F41") > 0) : # ICD code for Panic Disoders
            if (race=="01") :
                wpanic += 1
            elif (race=="02") :
                bpanic += 1                
    infile.close()

    print("Total Whites in file: ",wcount)
    print("Total Blacks in file: ",bcount)
    print("Total Whites with Panic: ",wpanic)
    print("Total Blacks with Panic: ",bpanic)
    print("Percent Whites with Panic: ",100*wpanic/wcount,"%")
    print("Percent Blacks with Panic: ",100*bpanic/bcount,"%")


main()

#ICD Code: F41.0 Panic disorder [episodic paroxysmal anxiety]
            
        
        
