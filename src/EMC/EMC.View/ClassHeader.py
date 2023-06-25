class Header():
    def __init__(self, lic, dat, builtByCreated, builtBySaved, mDate, hDate,aNN):
        self.__lic = lic
        self.__dat = dat
        self.__builtByCreated = builtByCreated
        self.__builtBySaved = builtBySaved
        self.__mDate =  mDate
        self.__hDate = hDate
        self.__aNN = aNN
    
    @property
    def Lic(self):
        return self.__lic

    @Lic.setter
    def Lic(self, lic):
        self.__lic = lic

    @property
    def Date(self):
        return self.__dat

    @Date.setter
    def Date(self, dat):
        self.__dat = dat

    @property
    def BuiltByCreated(self):
        return self.__builtByCreated

    @BuiltByCreated.setter
    def BuiltByCreated(self, builtByCreated):
        self.__builtByCreated = builtByCreated

    @property
    def BuiltBySaved(self):
        return self.__builtBySaved

    @BuiltBySaved.setter
    def BuiltBySaved(self, builtBySaved):
        self.__builtBySaved = builtBySaved
 
    @property        
    def MDate(self):
        return self.__mDate

    @MDate.setter
    def MDate(self, mDate):
       self.__mDate =  mDate

    @property
    def HDate(self):
        return self.__hDate

    @HDate.setter
    def HDate(self, hDate):
        self.__hDate = hDate

    @property
    def ANN(self):
        return self.__aNN

    @ANN.setter
    def ANN(self, aNN):
        self.__aNN = aNN



