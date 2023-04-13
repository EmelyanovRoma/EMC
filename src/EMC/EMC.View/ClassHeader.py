class Header():
    def __init__(self, lic, dat, builtByCreated, builtBySaved, mDate, hDate,aNN):
        self.__lic = lic
        self.__dat = dat
        self.__builtByCreated = builtByCreated
        self.__builtBySaved = builtBySaved
        self.__mDate =  mDate
        self.__hDate = hDate
        self.__aNN = aNN
    
    def Getlicense(self):
        return self.__lic

    def Setlicense(self, lic):
        self.__lic = lic

    def GetDate(self):
        return self.__dat

    def SetDate(self, dat):
        self.__dat = dat

    def GetbuiltByCreated(self):
        return self.__builtByCreated

    def SetbuiltByCreated(self, builtByCreated):
        self.__builtByCreated = builtByCreated

    def GetbuiltBySaved(self):
        return self.__builtBySaved

    def SetbuiltBySaved(self, builtBySaved):
        self.__builtBySaved = builtBySaved
    
    def GetmDate(self):
        return self.__mDate

    def SetmDate(self, mDate):
       self.__mDate =  mDate

    def GethDate(self):
        return self.__hDate

    def SethDate(self, hDate):
        self.__hDate = hDate

    def GetaNN(self):
        return self.__aNN

    def SetaNN(self, aNN):
        self.__aNN = aNN

        




