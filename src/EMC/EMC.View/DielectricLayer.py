class DielectricLayer:
    def __init__(self, thickness, erel, mrel, eloss, mloss, esignma, nzpart, name):
        self.__thickness = thickness    
        self.__erel = erel
        self.__mrel = mrel
        self.__eloss = eloss
        self.__mloss = mloss
        self.__esignma = esignma
        self.__nzpart = nzpart
        self.__name = name

    @property
    def Thickness(self):
        return self.__thickness

    @Thickness.setter
    def Thickness(self, thickness):
        self.__thickness = thickness


    @property
    def Erel(self):
        return self.__erel

    @Erel.setter
    def Erel(self, erel):
        self.__erel = erel


    @property
    def Mrel(self):
        return self.__mrel

    @Mrel.setter
    def Mrel(self, mrel):
        self.__mrel = mrel


    @property
    def Eloss(self):
        return self.__eloss

    @Eloss.setter
    def Eloss(self, eloss):
        self.__eloss = eloss


    @property
    def Mloss(self):
        return self.__mloss

    @Mloss.setter
    def Mloss(self, mloss):
        self.__mloss = mloss


    @property
    def Esignma(self):
        return self.__esignma

    @Esignma.setter
    def Esignma(self, esignma):
        self.__esignma = esignma


    @property
    def Nzpart(self):
        return self.__nzpart

    @Nzpart.setter
    def Nzpart(self, nzpart):
        self.__nzpart = nzpart


    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name
