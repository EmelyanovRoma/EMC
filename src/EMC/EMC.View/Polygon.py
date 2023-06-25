class Polygon:
    def __init__(self, iLevel, nVertices, mType, fillType, debugId, xMin, 
                 yMin, xMax, yMax, conMax, res1, res2, edgemesh, xVertices, yVertices):
        self.__iLevel = iLevel
        self.__nVertices = nVertices
        self.__mType = mType
        self.__fillType = fillType
        self.__debugId = debugId
        self.__xMin = xMin
        self.__yMin = yMin
        self.__xMax = xMax
        self.__yMax = yMax
        self.__conMax = conMax
        self.__res1 = res1
        self.__res2 = res2
        self.__edgemesh = edgemesh
        self.__xVertices = xVertices
        self.__yVertices = yVertices
    
    @property
    def ILevel(self):
        return self.__iLevel

    @ILevel.setter
    def ILevel(self, iLevel):
        self.__iLevel = iLevel


    @property
    def NVertices(self):
        return self.__nVertices

    @NVertices.setter
    def NVertices(self, nVertices):
        self.__nVertices = nVertices


    @property
    def MType(self):
        return self.__mType

    @MType.setter
    def MType(self, mType):
        self.__mType = mType


    @property
    def FillType(self):
        return self.__fillType

    @FillType.setter
    def FillType(self, fillType):
        self.__fillType = fillType


    @property
    def DebugId(self):
        return self.__debugId

    @DebugId.setter
    def DebugId(self, debugId):
        self.__debugId = debugId


    @property
    def XMin(self):
        return self.__xMin

    @XMin.setter
    def XMin(self, xMin):
        self.__xMin = xMin


    @property
    def YMin(self):
        return self.__yMin

    @YMin.setter
    def YMin(self, yMin):
        self.__yMin = yMin


    @property
    def XMax(self):
        return self.__xMax

    @XMax.setter
    def XMax(self, xMax):
        self.__xMax = xMax


    @property
    def YMax(self):
        return self.__yMax

    @YMax.setter
    def Ymax(self, yMax):
        self.__yMax = yMax


    @property
    def ConMax(self):
        return self.__conMax

    @ConMax.setter
    def ConMax(self, conMax):
        self.__conMax = conMax


    @property
    def Res1(self):
        return self.__res1

    @Res1.setter
    def Res1(self, res1):
        self.__res1 = res1


    @property
    def Res2(self):
        return self.__res2

    @Res2.setter
    def Res2(self, res2):
        self.__res2 = res2


    @property
    def Edgemesh(self):
        return self.__edgemesh

    @Edgemesh.setter
    def Edgemesh(self, edgemesh):
        self.__edgemesh = edgemesh


    @property
    def XVertices(self):
        return self.__xVertices

    @XVertices.setter
    def XVertices(self, xVertices):
        self.__xVertices = xVertices


    @property
    def YVertices(self):
        return self.__yVertices

    @YVertices.setter
    def YVertices(self, yVertices):
        self.__yVertices = yVertices

    def ShowPolygon(self):
        print(str(self.ILevel) + " " +
              str(self.NVertices) + " " +
              str(self.MType) + " " +
              str(self.FillType) + " " +
              str(self.DebugId) + " " +
              str(self.XMin) + " " +
              str(self.YMin) + " " +
              str(self.XMax) + " " +
              str(self.YMax) + " " +
              str(self.ConMax) + " " +
              str(self.Res1) + " " +
              str(self.Res2) + " " +
              str(self.Edgemesh))

        for i in range(len(self.XVertices)):
            print(str(self.XVertices[i]) + " " + str(self.YVertices[i]))