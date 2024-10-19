import sys
from termcolor import colored
import time
print("\nHello! What is the amount of Sensitivity you would prefer?\n\n\n\n\n")
print("1. " + colored('LOW' , 'green') + " sensitivity (>500 Million MC)")
print("2. " + colored('MEDIUM' , 'yellow') + " sensitivity (>100 Million MC)")
print("3. " + colored('HIGH' , 'red') + " sensitivity (>20 Million MC)\n\n\n\n\n")
sensitivityInput = input("")





def removeList(symbol):
    for i in range(0, len(listMedian)):
        if listMedian[i][0] == symbol:
            listMedian.remove(listMedian[i])
            break


fmean = open("documents/meanlist.txt", 'r')
fmedian = open("documents/medianlist.txt", 'r')

listMean = fmean.readlines()
listMean = eval(listMean[0])

listMedian = fmedian.readlines()
listMedian = eval(listMedian[0])

fmedian.close()
fmean.close()

fMediumSense = open("documents/mediumSensitivity.txt", 'r')
listMediumSense = fMediumSense.readlines()
listMediumSense = eval(listMediumSense[0])
fMediumSense.close()


fLowSense = open("documents/lowSensitivity.txt", 'r')
listLowSense = fLowSense.readlines()
listLowSense = eval(listLowSense[0])
fLowSense.close()


fHighSense = open("documents/highSensitivity.txt", 'r')
listHighSense = fHighSense.readlines()
listHighSense = eval(listHighSense[0])
fHighSense.close()





removeList('ENIC')
removeList('ASND')
removeList('HEPS')
removeList('TLS')
removeList('GGAL')
removeList('DHC')
removeList('BMA')
removeList('TVE')
removeList('CANO')
removeList('PYPD')
removeList('HTOO')
removeList('JOAN')
removeList('OSA')
removeList('LSF')
removeList('CCLD')

removeList('HSDT')
removeList('KALA')
removeList('SIEN')
removeList('KPRX')
removeList('ARTL')
removeList('NSTG')
removeList('PRST')
removeList('CNTX')
removeList('QNRX')


sensitiveList = []
if sensitivityInput == '1': # swapped cause messed up
    # Do LOW sensitivity
    # I want to go through the list of search through current list
    # compare with low sensitivity
    for i in range(len(listMedian)):
        try:
            if listLowSense[listMedian[i][0]] == True:
                sensitiveList.append(listMedian[i]) 
        except:
            # print("Keyboard Error: 401")
            pass
            # time.sleep(1000)
elif sensitivityInput == '2':
    for i in range(len(listMedian)):
        try:
            if listMediumSense[listMedian[i][0]] == True:
                sensitiveList.append(listMedian[i]) 
        except:
            pass
elif sensitivityInput == '3':
    for i in range(len(listMedian)):
        try:
            if listHighSense[listMedian[i][0]] == True:
                sensitiveList.append(listMedian[i]) 
        except:
            pass
elif sensitivityInput == '0':
    print("Keyboard Error: 401")
    time.sleep(50)
    sensitiveList = listMedian
else:
    print("Keyboard Error: 401")
    time.sleep(1000)
print("The top 3 investments for " + colored("BUYING", 'green') + " are: (MEDIAN)")
previousExtenedAmount = 3

for i in range(previousExtenedAmount):
    text = colored(str(round(((sensitiveList[len(sensitiveList)-(i+1)][1])/100) + 1, 2)), 'green')
    text2 = colored("x ", 'green')
    print(str(i+1) + ". " + str(sensitiveList[len(sensitiveList)-(i+1)][0]) + ": " + text + text2)
print("\n")

print("The top 3 investments for " + colored("SHORTING", 'red') + " are: (MEDIAN)")
for i in range(previousExtenedAmount):
    text = colored(str(round(((sensitiveList[i][1])/100) + 1, 2)), 'red')
    text2 = colored("x ", 'red')

    print(str(i+1) + ". " + str(sensitiveList[i][0]) + ": " + text + text2)
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
            text = colored(str(round(((sensitiveList[len(sensitiveList)-(i+1)][1])/100) + 1, 2)), 'green')
            text2 = colored("x ", 'green')
            print(str(i+1) + ". " + str(sensitiveList[len(sensitiveList)-(i+1)][0]) + ": " + text + text2)        
        print("\n\n\nThe top " + str(increaseAmount) + " investments for " + colored("SHORTING", 'red') + " are: (MEDIAN)\n")
        for i in range(increaseAmount):
            text = colored(str(round(((sensitiveList[i][1])/100) + 1, 2)), 'red')
            text2 = colored("x ", 'red')

            print(str(i+1) + ". " + str(sensitiveList[i][0]) + ": " + text + text2)            
    else:
        thing == False
        break




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


#

#ASTS
#