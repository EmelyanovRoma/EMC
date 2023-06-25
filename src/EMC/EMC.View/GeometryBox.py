from DielectricLayer import DielectricLayer

class GeometryBox:
    substrateDielectricLayer = DielectricLayer(1, 1, 1, 0, 0, 0, 0, "Substrate")
    airDielectricLayer = DielectricLayer(1, 1, 1, 0, 0, 0, 0, "Air")

    def __init__(self, nLev, xWidth, ywidth, xCells2, yCells2, nSubs, eeff):
        self.__nLev = nLev
        self.__xWidth = xWidth
        self.__yWidth = ywidth
        self.__xCells2 = xCells2
        self.__yCells2 = yCells2
        self.__nSubs = nSubs
        self.__eeff = eeff
        self.dielectricLayers = [self.airDielectricLayer, self.substrateDielectricLayer]
    
    @property
    def DielectricLayers(self):
        return self.__dielectricLayers

    @DielectricLayers.setter
    def DielectricLayers(self, dielectricLayers):
        self.__dielectricLayers = dielectricLayers

    @property
    def NLev(self):
        return self.__nLev

    @NLev.setter
    def NLev(self, nLev):
        self.__nLev = nLev


    @property
    def XWidth(self):
        return self.__xWidth

    @XWidth.setter
    def XWidth(self, xWidth):
        self.__xWidth = xWidth


    @property
    def YWidth(self):
        return self.__yWidth

    @YWidth.setter
    def YWidth(self, yWidth):
        self.__yWidth = yWidth


    @property 
    def XCells2(self):
        return self.__xCells2

    @XCells2.setter
    def XCells2(self, xCells2):
        self.__xCells2 = xCells2


    @property
    def YCells2(self):
        return self.__yCells2

    @YCells2.setter
    def YCells2(self, yCells2):
        self.__yCells2 = yCells2


    @property
    def NSubs(self):
        return self.__nSubs

    @NSubs.setter
    def NSubs(self, nSubs):
        self.__nSubs = nSubs


    @property
    def Eeff(self):
        return self.__eeff

    @Eeff.setter
    def Eeff(self, eeff):
        self.__eeff = eeff


    def ShowGeometryBox(self):
        print("BOX " + self.NLev +
        " " + self.XWidth +
        " " + self.YWidth +
        " " + self.XCells2 +
        " " + self.YCells2 +
        " " + self.NSubs +
        " " + self.Eeff)

        for i in range(len(self.__dielectricLayers)):
            print("      " + self.dielectricLayers[i].Thickness +
            " " + self.dielectricLayers[i].Erel +
            " " + self.dielectricLayers[i].Mrel +
            " " + self.dielectricLayers[i].Eloss +
            " " + self.dielectricLayers[i].Mloss +
            " " + self.dielectricLayers[i].Esignma +
            " " + self.dielectricLayers[i].Nzpart +
            " \"" + self.dielectricLayers[i].Name + "\"")

    def ShowDielectricLayer(self):
        print("\n " + self.Thickness +
        " " + self.Erel +
        " " + self.Mrel +
        " " + self.Eloss +
        " " + self.Mloss +
        " " + self.Esignma +
        " " + self.Nzpart +
        " \"" + self.Name + "\"")