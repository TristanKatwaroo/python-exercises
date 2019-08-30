from country import Country

dataFile = open("data.txt", "r")
continentFile = open("continent.txt", "r")

countryCat = []
cDictionary = {}
popDictionary = {}
areaDictionary = {}

# Fill the country dictionary
for line in continentFile:
    #cLine = continentFile.readline()
    #print(line)
    line = line.rstrip()
    line = line.split(",")
    if line[0] != "Country":
       # print(line[0])
        #countryCat.append(line[0])
        cDictionary[line[0]] = line[1]

# Fill the catalogue
for line in dataFile:
    #cLine = continentFile.readline()
    #print(line)
    line = line.rstrip()
    line = line.split("|")
    if line[0] != "Country":
        #print(line[0])
        countryCat.append(line[0])
        popDictionary[line[0]] = line[1]
        areaDictionary[line[0]] = line[2]

print(cDictionary)
print(countryCat)
print(popDictionary)
print(areaDictionary)


def findCountry(cntry):
    if cntry in countryCat:
        return cntry
    else:
        return None

def setPopulationOfCountry(cntry, cPop):
    if cntry in countryCat:
        popDictionary[cntry] = cPop
        return True
    else:
        return False

def setAreaOfCountry(cntry, cSz):
    if cntry in countryCat:
        areaDictionary[cntry] = cSz
        return True
    else:
        return False

def addCountry(cntry, cPop, cSz, theCont):
    if cntry not in countryCat:
        countryCat.append(cntry)
        cDictionary[cntry] = theCont
        popDictionary[cntry] = cPop
        areaDictionary[cntry] = cSz
        return True
    else:
        return False

def deleteCountry(cntry):
    countryCat.remove(cntry)
    cDictionary.pop(cntry)
    popDictionary.pop(cntry)
    areaDictionary.pop(cntry)

#theCont = "Europe"

def getCountriesByContinent(theCont):
    cntryList = []
    for item in cDictionary.items():
        if item[1] == theCont:
            cntryList.append(item[0])
    return cntryList

def getCountriesByArea(theCont):
    cntryList = []
    popTuple = {}
    #theCont = "Europe"

    for item in cDictionary.items():
        if item[1] == theCont:
            cntryList.append(item[0])
    #return cntryList
    for item in areaDictionary.items():
        if item[0] in cntryList:
            popTuple[item[0]] = item[1]
    return popTuple

def getCountriesByPopulation(theCont):
    cntryList = []
    popTuple = {}
    #theCont = "Europe"

    for item in cDictionary.items():
        if item[1] == theCont:
            cntryList.append(item[0])
    #return cntryList
    for item in popDictionary.items():
        if item[0] in cntryList:
            popTuple[item[0]] = item[1]
    return popTuple


def main():
   # theCont = "Europe"
#    lst = getCountriesByContinent(theCont)
#    if len(lst) > 0:
#        print()
#        print("Countries in " + theCont + " are:")
#        for cobj in lst:
#            print(cobj)

#    alst = getCountriesByPopulation(theCont)
#    if len(alst) > 0:
#        print()
#        if theCont == "":
#            print("Countries by population are:")
#        else:
#            print("Countries in "+theCont+" by population are:")
#        for ac in alst:
#            print(ac[0],ac[1])

    print(getCountriesByPopulation())


main()
