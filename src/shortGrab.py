import sys
from termcolor import colored, cprint


fmean = open("documents/meanlist.txt", 'r')
fmedian = open("documents/medianlist.txt", 'r')

listMean = fmean.readlines()
listMean = eval(listMean[0])

listMedian = fmedian.readlines()
listMedian = eval(listMedian[0])

print("The top 3 investments for " + colored("BUYING", 'green') + " are: (MEDIAN)")
previousExtenedAmount = 3

for i in range(previousExtenedAmount):
    text = colored(str(round(((listMedian[len(listMedian)-(i+1)][1])/100) + 1, 2)), 'green')
    text2 = colored("x ", 'green')
    print(str(i+1) + ". " + str(listMedian[len(listMedian)-(i+1)][0]) + ": " + text + text2)
print("\n")

print("The top 3 investments for " + colored("SHORTING", 'red') + " are: (MEDIAN)")
for i in range(previousExtenedAmount):
    text = colored(str(round(((listMedian[i][1])/100) + 1, 2)), 'red')
    text2 = colored("x ", 'red')

    print(str(i+1) + ". " + str(listMedian[i][0]) + ": " + text + text2)
print("\n")
thing = True
while(thing == True):
    extendAnswer = input("Would you like to extend this? (y/n) ")
    print("\n")


    if extendAnswer == 'y' or extendAnswer == 'Y':
        extendAmount = input("How much would you like to extend this by? ")
        print("\n")
        increaseAmount = int(extendAmount)+previousExtenedAmount
        previousExtenedAmount = increaseAmount
        print("The top " + str(increaseAmount) + " investments for " + colored("BUYING", 'green') +  " are: (MEDIAN)\n")
        for i in range(increaseAmount):
            text = colored(str(round(((listMedian[len(listMedian)-(i+1)][1])/100) + 1, 2)), 'green')
            text2 = colored("x ", 'green')
            print(str(i+1) + ". " + str(listMedian[len(listMedian)-(i+1)][0]) + ": " + text + text2)        
        print("\n\n\nThe top " + str(increaseAmount) + " investments for " + colored("SHORTING", 'red') + " are: (MEDIAN)\n")
        for i in range(increaseAmount):
            text = colored(str(round(((listMedian[i][1])/100) + 1, 2)), 'red')
            text2 = colored("x ", 'red')

            print(str(i+1) + ". " + str(listMedian[i][0]) + ": " + text + text2)            
    else:
        thing == False
        break


previousExtenedAmount = 3

print("The top 3 investments for " + colored("BUYING", 'green') + " are: (MEAN)")
for i in range(previousExtenedAmount):
    text = colored(str(round(((listMean[len(listMean)-(i+1)][1])/100) + 1, 2)), 'green')
    text2 = colored("x ", 'green')
    print(str(i+1) + ". " + str(listMean[len(listMean)-(i+1)][0]) + ": " + text + text2)   
print("\n")

print("The top 3 investments for " + colored("SHORTING", 'red') + " are: (MEAN)")
for i in range(previousExtenedAmount):
    text = colored(str(round(((listMean[i][1])/100) + 1, 2)), 'red')
    text2 = colored("x ", 'red')

    print(str(i+1) + ". " + str(listMean[i][0]) + ": " + text + text2)
print("\n")

previousExtenedAmount = 3
thing = True
while(thing == True):
    extendAnswer = input("Would you like to extend this? (y/n) ")
    print("\n")

    if extendAnswer == 'y' or extendAnswer == 'Y':
        extendAmount = input("How much would you like to extend this by? ")
        print("\n")
        increaseAmount = int(extendAmount)+previousExtenedAmount
        previousExtenedAmount = increaseAmount
        
        print("The top " + str(increaseAmount) + " investments for " + colored("BUYING", 'green')+ " are: (MEDIAN)\n")
        for i in range(increaseAmount):
            text = colored(str(round(((listMean[len(listMean)-(i+1)][1])/100) + 1, 2)), 'green')
            text2 = colored("x ", 'green')
            print(str(i+1) + ". " + str(listMean[len(listMean)-(i+1)][0]) + ": " + text + text2)        
        print("\n\n\nThe top " + str(increaseAmount) + " investments for " + colored("SHORTING", 'red') + " are: (MEDIAN)\n")
        for i in range(increaseAmount):
            text = colored(str(round(((listMean[i][1])/100) + 1, 2)), 'red')
            text2 = colored("x ", 'red')

            print(str(i+1) + ". " + str(listMean[i][0]) + ": " + text + text2)
    else:
        thing == False
        break
