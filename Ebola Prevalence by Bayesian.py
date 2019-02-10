# This program calculates the Baseyan probability of having a disease given the positive result of the test
# based on the sensivity and specificity of the test, and the prevalence of the disease in the population.

def main():
    print("Given the test sensivitity and specificity, and the population prevalence,\n this program calculates the probability of having it if the test is positive.")
    name = str(input("What is the name of the disease?\n"))   
    sen = eval(input("Pleaes provide the sensitivity of the test:\n"))
    preval = eval(input("Pleaes provide the prevalence of the diseas in the population:\n"))
    spe = eval(input("Pleaes provide the specificity of the test:\n"))

    prob = (sen*preval)/((sen*preval)+(1-spe)*(1-preval))
    print(prob)

    print("The Bayesian probability of having",name,"if the test is positive is",prob,".")

main()

    
