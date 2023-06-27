class Port:
    def __init__(self, Type, iPolygon, numPoints, iVertex, portNum, resist, react, induct, capac, xCoord, yCoord):
        self.__type = Type
        self.__iPolygon = iPolygon
        self.__numPoints = numPoints
        self.__iVertex = iVertex
        self.__portNum = portNum
        self.__resist = resist
        self.__react = react
        self.__induct = induct
        self.__capac = capac
        self.__xCoord = xCoord
        self.__yCoord = yCoord

    @property
    def Type(self):
        return self.__type

    @Type.setter
    def Type(self, Type):
        self.__type = Type


    @property
    def IPolygon(self):
        return self.__iPolygon

    @IPolygon.setter
    def IPolygon(self, iPolygon):
        self.__iPolygon = iPolygon


    @property
    def NumPoints(self):
        return self.__numPoints

    @NumPoints.setter
    def NumPoints(self, numPoints):
        self.__numPoints = numPoints


    @property
    def IVertex(self):
        return self.__iVertex

    @IVertex.setter
    def IVertex(self, iVertex):
        self.__iVertex = iVertex


    @property
    def PortNum(self):
        return self.__portNum

    @PortNum.setter
    def PortNum(self, portNum):
        self.__portNum = portNum


    @property
    def Resist(self):
        return self.__resist

    @Resist.setter
    def Resist(self, resist):
        self.__resist = resist


    @property
    def React(self):
        return self.__react

    @React.setter
    def React(self, react):
        self.__react = react


    @property
    def Induct(self):
        return self.__induct

    @Induct.setter
    def Induct(self, induct):
        self.__induct = induct


    @property
    def Capac(self):
        return self.__capac

    @Capac.setter
    def Capac(self, capac):
        self.__capac = capac


    @property
    def XCoord(self):
        return self.__xCoord

    @XCoord.setter
    def XCoord(self, xCoord):
        self.__xCoord = xCoord


    @property
    def YCoord(self):
        return self.__yCoord

    @YCoord.setter
    def YCoord(self, yCoord):
        self.__yCoord = yCoord

    def GetShowPortString(self):
        return("POR1 " + self.Type + "\n" +
              "POLY " + self.IPolygon + " " + 
              self.NumPoints + "\n" + 
              self.IVertex + "\n" +
              self.PortNum + " " +
              self.Resist + " " +
              self.React + " " +
              self.Induct + " " +
              self.Capac + " " +
              self.XCoord + " " +
              self.YCoord + "\n")