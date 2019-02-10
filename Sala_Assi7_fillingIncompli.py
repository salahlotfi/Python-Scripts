# An incomplete program for an "infinite" interactive loop to process a dictionary.

def main():
    d = {} # dictionary

    # Read the file's contents in the dictionary d
    filename = input("Give the file name: ")
    file = open(filename,"r")
    for line in file:
        # read key and value
        key, value = line.split(",")
        # remove whitespaces before and after
        key = key.lstrip()
        key = key.rstrip()
        value = value.lstrip()
        value = value.rstrip()
        # insert entry in the dictionary
        d[key] = value
    file.close()

    loop=True # continue looping if true

    while (loop):
        print("\n\nEnter one of the following menu choices:")
        print("1 Add an entry")
        print("2 Show value for a key")
        print("3 Delete an entry")
        print("4 Save the file")
        print("5 Print the current dictionary")
        print("6 Quit")
        choice = input("Choice 1-6: ")
        print("\n\n")

        if (choice=="1"): # Add an entry
            k = input("Give the key: ")
            v = input("Give its value: ")
            #vIs = d[k]
            if k in d.keys(): #== True: I can't use this type of membership because the contain of the file isn't yet a dictionnary. 
                print(k, "already exists in the dictionary.\n")
                yn=input("Would you like to overwrite it? Yes or No?")
                if yn[0].upper() == 'Y':
                    d[k]=v
                else:
                    k1=input("Alright. What is the new key?")
                    v1=input("What is the new value?")
                    d[k1]=v1        
            else:
                d[k]=v
                
        elif (choice=="2"): # Show value for a key
            k = input("Give the key: ")

            if k in d.keys(): #== True:
                print("%%The value for this key is '",d.get(k),"'.%%") #1
            else:
                print("There is no such a key in the dictionary")
            
        elif (choice=="3"): # Delete an entry
            k = input("Give the key to delete the entry: ")
            if k in d.keys(): #== True:
                del d[k]
                print("The value of'",k,"'is deleted.")  #2
                
            else:
                print("There is no such a key in the dictionary")

            
            # complete the rest
        elif (choice=="4"): # Save the file
             print("Saving the file")

             filew = open(filename,"w")
             for k, v in d.items():
                 
                 print(k,',',v, file = filew)
             filew.close()
             
        elif (choice=="5"): # Print the current dictionary
            l = list(d.keys()) # get all the keys
            l.sort() # sort them

            print(list(d.items())) #Here you dont use l.keys to print, because l.sort is to sort the contain of d. So, use d.keys
            
        elif (choice=="6"): # Quit

            loop=False         
        else:
            print("Incorrect choice")
main()
