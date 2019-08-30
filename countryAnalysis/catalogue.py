from country import Country

class CountryCatalogue:
    def __init__(self, dataFile, continentFile):            # Constructor creates the two data structures;
                                                            # countryCat and cDictionary
        data = open(dataFile, "r")
        continent = open(continentFile, "r")
        self._countryCat = []
        self._cDictionary = {}
        self._popDictionary = {}
        self._areaDictionary = {}

        # Fill the country dictionary
        for line in continent:
            line = line.rstrip()
            line = line.split(",")
            if line[0] != "Country":
                self._cDictionary[line[0]] = line[1]

        # Fill the catalogue
        for line in data:
            line = line.rstrip()
            line = line.split("|")
            if line[0] != "Country":
                self._countryCat.append(line[0])
                self._popDictionary[line[0]] = line[1]
                self._areaDictionary[line[0]] = line[2]
        data.close()
        continent.close()

    def findCountry(self, cntry):
        if cntry in self._countryCat:
            return cntry
        else:
            return None

    def setPopulationOfCountry(self, cntry, cPop):
        if cntry in self._countryCat:
            self._popDictionary[cntry] = cPop
            return True
        else:
            return False

    def setAreaOfCountry(self, cntry, cSz):
        if cntry in self._countryCat:
            self._areaDictionary[cntry] = cSz
            return True
        else:
            return False

    def addCountry(self, cntry, cPop, cSz, theCont):
        if cntry not in self._countryCat:
            self._countryCat.append(cntry)
            self._cDictionary[cntry] = theCont
            self._popDictionary[cntry] = cPop
            self._areaDictionary[cntry] = cSz
            return True
        else:
            return False

    def deleteCountry(self, cntry):
        self._countryCat.remove(cntry)
        self._cDictionary.pop(cntry)
        self._popDictionary.pop(cntry)
        self._areaDictionary.pop(cntry)

    #theCont = "Europe"

    def getCountriesByContinent(self, theCont):
        cntryList = []
        for item in self._cDictionary.items():
            if item[1] == theCont:
                cntryList.append(item[0])
        return cntryList

    def getCountriesByArea(self, theCont):
        cntryList = []
        popTuple = {}
        #theCont = "Europe"

        for item in self._cDictionary.items():
            if item[1] == theCont:
                cntryList.append(item[0])
        #return cntryList
        for item in self._areaDictionary.items():
            if item[0] in cntryList:
                popTuple[item[0]] = item[1]
        return popTuple

    def getCountriesByPopulation(self, theCont):
        cntryList = []
        popTuple = {}
        #theCont = "Europe"

        for item in self._cDictionary.items():
            if item[1] == theCont:
                cntryList.append(item[0])
        #return cntryList
        for item in self._popDictionary.items():
            if item[0] in cntryList:
                popTuple[item[0]] = item[1]
        return popTuple

    def getCountryCat(self):
        list = []
        for element in self._countryCat:
            list.append(element)
        return list

    def printCountryCatalogue(self):
        for element in self._countryCat:
            print(element)

    def filterCountriesByPopDensity(self, lb, ub):
        list = []
        for element in self._popDictionary:
            if lb <= element <= ub:
                list.append(element)
        newList = []
        i = 0
        length = len(list)
        while i < length:
            largest = -1
            largestElement = None
            for element in list:
                if element > largest:
                    largest = element
                    largestElement = element
            list.remove(largestElement)
            #newList.append((largestElement.getName(), largestElement.getPopDensity()))
            i = i+1
        return newList

    def findMostPopulousContinent(self):
        continents = []
        for key in self._cDictionary:
            if key not in continents:
                continents.append(self._cDictionary[key])
        mostPopulous = ("", -1)
        for element in continents:
            countries = self.getCountriesByContinent(self, theCont)
            pop = 0
            for line in countries:
                pop = pop + 1
            if mostPopulous[1] < pop:
                mostPopulous = (element, pop)
        return mostPopulous

    def saveCountryCatalogue(self, outFile):
        outFile = open(outFile, "w")
        list = []
        for element in self._countryCat:
            list.append(element.getName())
        list.sort()
        print(list)
        i = 0
        for element in list:
            for x in self._countryCat:
                if element == x.getName():
                    i = i+1
                    outFile.write("{}|{}|{}|{:.2f}|{:.2f}\n".format(x.getName(), x.getContinent(), x.getPopulation(), x.getArea(), x.getPopDensity()))
        outFile.close()

        if len(self._countryCat) == i:
            return i
        else:
            return -1

