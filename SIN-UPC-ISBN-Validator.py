# program to validate SINs, UPCs, ISBNs
# author: sean flannigan, 000270501


def validateSIN():
    
    validEntryFlag = False
    sumOfDigs = 0
    alphaDoubleFlag = False
    checkDigitMissing = False
    tempNum = 0

    # validation while loop for SINs entered by user. requires
    # user to enter a 9 digit number with either 1 or zero alpha
    # character to denote a missing digit
    while validEntryFlag is False:
        sinNum = input("\nEnter the SIN you wish to check, with no spaces,\
 and an 'x' if there is a missing main digit or check digit. Example: 12345678x: ")
        alphaCount = 0
        badCharFlag = False
        for i in sinNum:
            if i.isalpha():
                alphaCount += 1
            if i.isalpha() is False and i.isdecimal() is False:
                badCharFlag = True
        if (len(sinNum) == 9) and (alphaCount <= 1) and badCharFlag is False:
            validEntryFlag = True
        else:
            print("\nSorry, SIN entry is invalid. See example.\n")

    # data manipulation for loop to crawl the valid SIN
    # to add to the sum variable, mark a missing check digit,
    # or to mark where a missing digit would be doubled
    for i in range(len(sinNum)):
        if sinNum[i].isdecimal() and (i % 2 == 0):
            sumOfDigs += int(sinNum[i])
        elif sinNum[i].isdecimal() and (i % 2 == 1):
            if int(sinNum[i]) <= 4:
                # numbers that are equal to or less than 4
                # are simply doubled then added to the sum
                sumOfDigs += (int(sinNum[i]) * 2)
            else:
                # numbers above 4 that need to be doubled
                # will result in a 2 digit number and must
                # then follow the SIN validation quirk of
                # having their individual digits added to the
                # sum rather than the number as a whole.
                # temp number variable used to build the number,
                # turn it into a string in order to slice it, then
                # turn each slice into an int to add to the sum
                tempNum = str(int(sinNum[i]) * 2)
                sumOfDigs += int(tempNum[0])
                sumOfDigs += int(tempNum[1])
        elif sinNum[i].isalpha() and (i % 2 == 1):
            alphaDoubleFlag = True
        elif sinNum[i].isalpha() and i == 8:
            checkDigitMissing = True

    # once the sum is built validation of the SIN can follow
    # depending on various check flags or whether or not
    # a digit is missing from the SIN
    if alphaCount == 0:
        if sumOfDigs % 10 == 0:
            print("\nSIN is valid.\n")
        else:
            print("\nSIN is not valid.\n")
    elif checkDigitMissing is True:
        if sumOfDigs % 10 == 0:
            print("\nCheck digit is 0.\n")
        else:
            print("\nCheck digit is " + str(10 - (sumOfDigs % 10)) + "\n")
    elif alphaDoubleFlag is False:
        if sumOfDigs % 10 == 0:
            print("\nMissing digit is 0.\n")
        else:
            print("\nMissing digit is " + str(10 - (sumOfDigs % 10)) + "\n")
    elif alphaDoubleFlag is True:
        if sumOfDigs % 10 == 0:
            print("\nMissing digit is 0.\n")
        else:
            tempNum = (10 - (sumOfDigs % 10))
            if tempNum % 2 == 0:
                # if the temp num is even it is simply halved
                # to derive the missing digit
                print("\nMissing digit is " + str(int(tempNum / 2)) + "\n")
            else:
                # if the temp num is odd, 9 is added to bring the number
                # back to its 2-digit variant, which is then halved to
                # derive the missing digit
                print("\nMissing digit is " + str(int((tempNum + 9) / 2)) + "\n")
        


def validateUPC():
    
    validEntryFlag = False
    sumOfDigs = 0
    alphaTripleFlag = False
    checkDigitMissing = False
    tempNum = 0

    # validation while loop for UPCs entered by user. requires
    # user to enter a 12 digit number with either 1 or zero alpha
    # character to denote a missing digit
    while validEntryFlag is False:
        upcNum = input("\nEnter the UPC you wish to check, with no spaces,\
 and an 'x' if there is a missing main digit or check digit. Example: 12345678912x: ")
        alphaCount = 0
        badCharFlag = False
        for i in upcNum:
            if i.isalpha():
                alphaCount += 1
            if i.isalpha() is False and i.isdecimal() is False:
                badCharFlag = True
        if (len(upcNum) == 12) and (alphaCount <= 1) and badCharFlag is False:
            validEntryFlag = True
        else:
            print("\nSorry, UPC entry is invalid. See example.\n")

    
    # data manipulation for loop to crawl the valid UPC
    # to add to the sum variable, mark a missing check digit,
    # or to mark where a missing digit would be tripled
    for i in range(len(upcNum)):
        if upcNum[i].isdecimal() and (i % 2 == 0):
            sumOfDigs += (int(upcNum[i]) * 3)
        elif upcNum[i].isdecimal() and (i % 2 == 1):
            sumOfDigs += int(upcNum[i])
        elif upcNum[i].isalpha() and (i % 2 == 0):
            alphaTripleFlag = True
        elif upcNum[i].isalpha() and i == 11:
            checkDigitMissing = True

    # once the sum is built validation of the UPC can follow
    # depending on various check flags or whether or not
    # a digit is missing from the UPC
    if alphaCount == 0:
        if sumOfDigs % 10 == 0:
            print("\nUPC is valid.\n")
        else:
            print("\nUPC is not valid.\n")
    elif checkDigitMissing is True:
        if sumOfDigs % 10 == 0:
            print("\nCheck digit is 0.\n")
        else:
            print("\nCheck digit is " + str(10 - (sumOfDigs % 10)) + "\n")
    elif alphaTripleFlag is False:
        if sumOfDigs % 10 == 0:
            print("\nMissing digit is 0.\n")
        else:
            print("\nMissing digit is " + str(10 - (sumOfDigs % 10)) + "\n")
    elif alphaTripleFlag is True:
        if sumOfDigs % 10 == 0:
            print("\nMissing digit is 0.\n")
        else:
            tempNum = (10 - (sumOfDigs % 10))
            if tempNum % 3 == 0:
                # if temp num is a multiple of 3 it is simply divided
                # by 3 to derive the missing pre-tripled digit
                print("\nMissing digit is " + str(int(tempNum / 3)) + "\n")
            else:
                # if temp num is NOT a multiple of 3, the mod of 10
                # is added to it until it becomes a multiple of 3, at
                # which point it is simply divided by 3 to derive the
                # missing pre-tripled digit
                while tempNum % 3 != 0:
                    tempNum += 10
                print("\nMissing digit is " + str(int(tempNum / 3)) + "\n")



def validateISBN():
    
    validEntryFlag = False
    sumOfDigs = 0
    missingDigMultiple = 0
    checkDigitMissing = False
    tempNum = 0

    # validation while loop for ISBNs entered by user. requires
    # user to enter a 10 digit number with either 1 or zero alpha
    # character to denote a missing digit
    while validEntryFlag is False:
        isbnNum = input("\nEnter the ISBN you wish to check, with no spaces,\
 and an 'x' if there is a missing main digit or check digit. Example: 123456789x: ")
        alphaCount = 0
        badCharFlag = False
        for i in isbnNum:
            if i.isalpha():
                alphaCount += 1
            if i.isalpha() is False and i.isdecimal() is False:
                badCharFlag = True
        if (len(isbnNum) == 10) and (alphaCount <= 1) and badCharFlag is False:
            validEntryFlag = True
        else:
            print("\nSorry, ISBN entry is invalid. See example.\n")

    # data manipulation for loop to crawl the valid ISBN
    # to add to the sum variable, mark a missing check digit,
    # or to store the multiple of the missing digit required
    # to satisfy the ISBN validation sequence
    # digit positions 1-9 are multiplied by 1-9 respectively
    # before adding to the sum
    for i in range(len(isbnNum)):
        if isbnNum[i].isalpha() and i != 9:
            missingDigMultiple = i + 1
        elif isbnNum[i].isalpha() and i == 9:
            checkDigitMissing = True
        elif isbnNum[i].isdecimal() and i != 9:
            sumOfDigs += int(isbnNum[i]) * (i + 1)
        elif isbnNum[i].isdecimal() and i == 9:
            checkDigit = int(isbnNum[i])

    # once the sum is built validation of the ISBN can follow
    # depending on various check flags or whether or not
    # a digit is missing from the UPC
    if alphaCount == 0:
        if sumOfDigs % 11 == checkDigit:
            print("\nISBN is valid.\n")
        else:
            print("\nISBN is not valid.\n")
    elif checkDigitMissing is True:
        if sumOfDigs % 11 == 10:
            print("\nCheck digit is X (10).\n")
        else:
            print("\nCheck digit is " + str(sumOfDigs % 11) + ".\n")
    else:
        if sumOfDigs % 11 == checkDigit:
            print("\nMissing digit is 0.\n")
        else:
            # in the case of a missing digit somewhere in the ISBN
            # that isn't the check digit, the sum without that missing
            # digit (modded down) is subtracted from the check digit. this
            # likely returns a negative number, which is then put into a
            # while loop that continuously adds the mod, 11, until the number
            # is both no longer negative AND is a perfect multiple of the
            # missing digits multiple. at which point the newly built
            # number is simply divided by the missing digit's multiple
            # to derive the missing digit
            tempNum = (checkDigit - (sumOfDigs % 11))
            while (tempNum <= 0) or (tempNum % missingDigMultiple != 0):
                tempNum += 11
            print("\nMissing digit is " + str(int(tempNum / missingDigMultiple)) + ".\n")
            




# main code run. menu contained in a while loop checked by boolean flag, options call
# methods defined above

quitFlag = False

while quitFlag is False:
    menuChoice = input("\nPress 1 for SIN Verification \nPress 2 for UPC Verification \
\nPress 3 for ISBN Verification \nPress Q to quit \nEnter your selection: ")
    if menuChoice == "1":
        validateSIN()
    elif menuChoice == "2":
        validateUPC()
    elif menuChoice == "3":
        validateISBN()
    elif menuChoice.lower() == "q":
        quitFlag = True
    else:
        print("\nSorry, selection invalid.\n")
