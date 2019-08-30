class Country:                                                  # Creates class
    def __init__(self, name, population, area, continent):      # Creates constructor

        # This segment initiates instance variables
        self._name = name
        self._population = population
        self._area = area
        self._continent = continent

    # This segment creates getter methods
    def getName(self):
        self._name = str(self._name)
        return self._name

    def getPopulation(self):
        return self._population

    def getArea(self):
        return self._area

    def getContinent(self):
        return self._continent

    def setPopulation(self, cPop):
        self._population = cPop

    def setArea(self, cSz):
        self._area = cSz


    def setContinent(self, theCont):
        self._area = theCont


    def getPopDensity(self):
        density = self._population/self._area
        return round(density, 2)


    def __repr__(self):
        return "{} (pop: {}, size: {}) in {}".format(self._name, self._population, self._area, self._continent)


