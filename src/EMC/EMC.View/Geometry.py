from DielectricLayer import DielectricLayer
from GeometryBox import GeometryBox
from TechnologyLayer import TechnologyLayer
from Port import Port
from Polygon import Polygon

class GeometryBlock:
    defaultGeometryBox = GeometryBox("1", "350", "250", "70", "50", "20", "0")
    defaultTechnologyLayer = TechnologyLayer("METAL", "Metal1", "Metal1", "-2", "0",
                                      "0", "0", "-1", "N", "40", "1", "1", "100", "100", "0", "0", "0", "Y")
    numberOfPolygons = 0
    debugId = 1
    numberOfPorts = 1

    def __init__(self, nameTMET, patternIdTMET, typeTMET, value1TMET, value2TMET, value3TMET, value4TMET,
                 nameBMET, patternIdBMET, typeBMET, value1BMET, value2BMET, value3BMET, value4BMET,
                 toLevel, conMax, meshingfill, pads, x, y, ul):
        #TMET
        self.__nameTMET = nameTMET
        self.__patternIdTMET = patternIdTMET
        self.__typeTMET = typeTMET
        self.__value1TMET = value1TMET
        self.__value2TMET = value2TMET
        self.__value3TMET = value3TMET
        self.__value4TMET = value4TMET

        #BMET
        self.__nameBMET = nameBMET
        self.__patternIdBMET = patternIdBMET
        self.__typeBMET = typeBMET
        self.__value1BMET = value1BMET
        self.__value2BMET = value2BMET
        self.__value3BMET = value3BMET
        self.__value4BMET = value4BMET

        # GeometryBox
        self.__geometryBox = self.defaultGeometryBox

        # Techlay
        self.__technologyLayers = [self.defaultTechnologyLayer]

        # Polygons
        self.__polygons = []

        #TOLEVEL
        self.__tolevel = toLevel
        self.__conmax2 = conMax
        self.__meshingfill = meshingfill
        self.__pads = pads

        #LORGN
        self.__x = x
        self.__y = y
        self.__ul = ul

        # Port
        self.__ports = []
       
    #TMET
    @property
    def NameTMET(self):
        return self.__nameTMET

    @NameTMET.setter
    def NameTMET(self, NameTMET):
        self.__nameTMET = NameTMET


    @property
    def PatternIdTMET(self):
        return self.__patternIdTMET

    @PatternIdTMET.setter
    def PatternIdTMET(self, PatternidTMET):
        self.__patternIdTMET = PatternidTMET


    @property
    def TypeTMET(self):
        return self.__typeTMET

    @TypeTMET.setter
    def TypeTMET(self, TypeTMET):
        self.__typeTMET = TypeTMET
        

    @property
    def Value1TMET(self):
        return self.__value1TMET

    @Value1TMET.setter
    def Value1TMET(self, Value1TMET):
        self.__value1TMET = Value1TMET


    @property
    def Value2TMET(self):
        return self.__value2TMET

    @Value2TMET.setter
    def Value2TMET(self, Value2TMET):
        self.j__Value2TMET = Value2TMET


    @property
    def Value3TMET(self):
        return self.__value3TMET

    @Value3TMET.setter
    def Value3TMET(self, Value3TMET):
        self.__value3TMET = Value3TMET


    @property
    def Value4TMET(self):
        return self.__value4TMET

    @Value4TMET.setter
    def Value4TMET(self, value4TMET):
        self.__value4TMET = value4TMET 


    #BMET
    @property
    def NameBMET(self):
        return self.__nameBMET

    @NameBMET.setter
    def NameBMET(self, nameBMET):
        self.__nameBMET = nameBMET


    @property
    def PatternIdBMET(self):
            return self.__patternIdBMET

    @PatternIdBMET.setter
    def PatternIdBMET(self, patternidBMET):
        self.__patternIdBMET = patternidBMET


    @property
    def TypeBMET(self):
            return self.__typeBMET

    @TypeBMET.setter
    def TypeBMET(self, typeBMET):
        self.__typeBMET = typeBMET
        

    @property
    def Value1BMET(self):
            return self.__value1BMET

    @Value1BMET.setter
    def Value1BMET(self, value1BMET):
        self.__value1BMET = value1BMET


    @property
    def Value2BMET(self):
            return self.__value2BMET

    @Value2BMET.setter
    def SetValue2BMET(self, value2BMET):
        self.__value2BMET = value2BMET


    @property
    def Value3BMET(self):
            return self.__value3BMET

    @Value3BMET.setter
    def Value3BMET(self, value3BMET):
        self.__value3BMET = value3BMET


    @property
    def Value4BMET(self):
            return self.__value4BMET

    @Value4BMET.setter
    def Value4BMET(self, value4BMET):
        self.__value4BMET = value4BMET
  
    
    # Geometry Box
    @property
    def GeometryBox(self):
        return self.__geometryBox

    @GeometryBox.setter
    def GeometryBox(self, geometryBox):
        self.__geometryBox = geometryBox


    # Technology Layers
    @property
    def TechnologyLayers(self):
        return self.__technologyLayers

    @TechnologyLayers.setter
    def TechnologyLayers(self, technologyLayers):
        self.__technologyLayers = technologyLayers

    # Polygons
    @property
    def Polygons(self):
        return self.__polygons

    @Polygons.setter
    def Polygons(self, polygons):
        self.__polygons = polygons


    # To Level
    def GetToLevel(self):
        return self.__tolevel
    def SetToLevel(self, ToLevel):
        self.__tolevel = ToLevel

    def GetConmax2(self):
        return self.__conmax2
    def SetConmax2(self, Conmax2):
        self.__conmax2 = Conmax2

    def GetMeshingfill(self):
        return self.__meshingfill
    def SetMeshingfill(self, Meshingfill):
        self.__meshingfill = Meshingfill

    def GetPads(self):
        return self.__pads
    def SetPads(self, Pads):
        self.__pads = Pads

    #LORGN
    @property
    def X(self):
        return self.__x

    @X.setter
    def SetX(self, x):
        self.__x = x
    

    @property
    def Y(self):
        return self.__y

    @Y.setter
    def SetY(self, y):
        self.__y = y
    
    
    @property
    def UL(self):
        return self.__ul

    @UL.setter
    def SetUL(self, ul):
        self.__ul = ul


    @property
    def Ports(self):
        return self.__ports

    @Ports.setter
    def Ports(self, ports):
        self.__ports = ports


    def AddDielectricLayer(self):
        name = input("Введите название слоя -> ")
        thickness = input("Введите толщину слоя -> ")
        erel = input("Введите диэлектрическую проницаемость -> ")
        mrel = input("Введите магнитную проницаемость -> ")
        eloss = input("Введите тангенс угла диэлектрических потерь -> ")
        mloss = input("Введите тангенс угла магнитных потерь -> ")   
        esignma = "0"
        nzpart = "0"       
    
        newDielectricLayer = DielectricLayer(thickness, erel, mrel, eloss, mloss, esignma, nzpart, name)
        self.GeometryBox.DielectricLayers.append(newDielectricLayer)
        self.defaultGeometryBox.NLev = str(int(self.defaultGeometryBox.NLev) + 1)


    def RemoveDielectricLayer(self):
        print("Выберите, какой диэлектрический слой нужно удалить:")

        for i in range(len(self.GeometryBox.DielectricLayers)):
            print("[" + str(i) + "]" + 
                  self.GeometryBox.DielectricLayers[i].GetDielectricLayerString())

        indexOfDeletedLayer = input("-> ")
        while int(indexOfDeletedLayer) < 0 or int(indexOfDeletedLayer) >= len(self.GeometryBox.DielectricLayers):
            print("Неправилно выбран удаляемый диэлектрический слой.")
            indexOfDeletedLayer = input("Выберите, какой диэлектрический слой нужно удалить: ")

        self.GeometryBox.DielectricLayers.pop(int(indexOfDeletedLayer))
        self.defaultGeometryBox.NLev = str(int(self.defaultGeometryBox.NLev) - 1)


    def AddPolygon(self):
        numOfVertices = input("Введите количество вершин полигона: ")
        while int(numOfVertices) < 3:
            print("\nКоличество вершин должно быть 3 или больше.")
            numOfVertices = input("Введите количество вершин полигона: ")

        print("\nВыберите какой технологический слой будет использоваться для полигона: ")
        for i in range(len(self.TechnologyLayers)):
            print("[" + str(i) + "] " + self.TechnologyLayers[i].GetTechnologyLayerString())
            
        index = input("-> ")
        while int(index) < 0 or int(index) >= len(self.TechnologyLayers):
            print("\nТехнологический слой выбран неверно.")
            index = input("Выберите технологический слой: ")

        xVertices = []
        yVertices = []

        for i in range(int(numOfVertices)):
            print("\nВведите координату вершины x" + str(i) + ": ")           
            xVertices.append(input("-> "))

            print("Введите координату вершины y" + str(i) + ": ")
            yVertices.append(input("-> "))
           
        xVertices.append(xVertices[0])
        yVertices.append(yVertices[0])

        newPolygon = Polygon(self.TechnologyLayers[int(index)].ILevel,
                             str(int(numOfVertices) + 1),
                             self.TechnologyLayers[int(index)].MType,
                             self.TechnologyLayers[int(index)].FillType,
                             str(self.debugId),
                             self.TechnologyLayers[int(index)].XMin,
                             self.TechnologyLayers[int(index)].YMin,
                             self.TechnologyLayers[int(index)].XMax,
                             self.TechnologyLayers[int(index)].YMax,
                             self.TechnologyLayers[int(index)].ConMax,
                             self.TechnologyLayers[int(index)].Res1,
                             self.TechnologyLayers[int(index)].Res2,
                             self.TechnologyLayers[int(index)].Edgemesh,
                             self.TechnologyLayers[int(index)].LayName1,
                             xVertices,
                             yVertices) 

        self.Polygons.append(newPolygon)
        self.numberOfPolygons += 1
        self.debugId += 1


    def RemovePolygon(self):
        print("Выберите, какой полигон нужно удалить:")

        for i in range(len(self.Polygons)):
            print("[" + str(i) + "]")
            self.Polygons[i].ShowPolygon()

        indexOfDeletedPolygon = input("-> ")
        while int(indexOfDeletedPolygon) < 0 or int(indexOfDeletedPolygon) >= len(self.Polygons):
            print("Неправильно выбран удаляемый полигон.")
            indexOfDeletedPolygon = input("Выберите, какой полигон нужно удалить: ")

        self.Polygons.pop(int(indexOfDeletedPolygon))
        self.numberOfPolygons -= 1


    def AddTechnologyLayer(self):
        layType = "METAL"
        layName1 = input("Введите название технологического слоя: ")
        layName2 = layName1
        mapping = "-2"
        Type = "0"

        print("Выберите уровень, на котором будем располагаться слой: ")
        for i in range(self.GeometryBox.NLev):
            print(i, "уровень")
        iLevel = input("-> ")

        nVertices = "0"
        mType = "-1"
        fillType = "N"
        debugId = self.debugId
        xMin = input("Введите минимальное значение x: ")
        yMin = input("Введите минимальное значение y: ")
        xMax = input("Введите максимальное значение x: ")
        yMax = input("Введите максимальное значение y: ")
        conMax = "0"
        res1 = "0"
        res2 = "0"
        edgemesh = "Y"

        newTechnologyLayer = TechnologyLayer(layType, layName1, layName2, mapping, Type,
                                             iLevel, nVertices, mType, fillType, debugId,
                                             xMin, yMin, xMax, yMax, conMax, res1, res2, 
                                             edgemesh)

        self.TechnologyLayers.append(newTechnologyLayer)
        self.debugId += 1


    def RemoveTechnologyLayer(self):
        print("Выберите, какой технологический слой нужно удалить:")

        for i in range(len(self.TechnologyLayers)):
            print("[" + str(i) + "] " + self.TechnologyLayers[i].GetTechnologyLayerString())
            
        indexOfDeletedLayer = input("-> ")
        while int(indexOfDeletedLayer) < 0 or int(indexOfDeletedLayer) >= len(self.TechnologyLayers):
            print("Неправильно выбран удаляемый полигон.")
            indexOfDeletedLayer = input("Выберите, какой полигон нужно удалить: ")

        self.TechnologyLayers.pop(int(indexOfDeletedLayer))


    def AddPort(self):
        print("Выберите полигон: ")
        for i in range(len(self.Polygons)):
            print("[" + str(i) + "]" + self.Polygons[i].GetPolygonString())           

        indexOfPolygon = input("-> ")
        while int(indexOfPolygon) < 0 or int(indexOfPolygon) >= len(self.Polygons):
            print("Неправильно выбран  полигон.")
            indexOfPolygon = input("Выберите полигон: ")

        print("Выберите, между какими вершинами будет располагаться порт: ")
        for i in range(int(self.Polygons[int(indexOfPolygon)].NVertices) - 1):
            j = i + 1
            if j == int(self.Polygons[int(indexOfPolygon)].NVertices) - 1:
                j = 0

            print("[" + str(i) + "] (" + 
                  str(self.Polygons[int(indexOfPolygon)].XVertices[i]) + "; " + 
                  str(self.Polygons[int(indexOfPolygon)].YVertices[i]) + ") и [" + 
                  str(j) + "] (" + 
                  str(self.Polygons[int(indexOfPolygon)].XVertices[j]) + "; " + 
                  str(self.Polygons[int(indexOfPolygon)].YVertices[j]) + ")")

        indexOfVertex = input("-> ")
        while int(indexOfVertex) < 0 or int(indexOfVertex) >= int(self.Polygons[int(indexOfPolygon)].NVertices) - 1:
            print("Неправильно выбрано расположение порта.")
            indexOfVertex = input("Выберите, между какими вершинами будет располагаться порт: ")

        Type = "BOX"
        iPolygon = self.Polygons[int(indexOfPolygon)].DebugId
        numPoints = "1"
        iVertex = str(indexOfVertex)
        portNum = str(self.numberOfPorts)
        resist = "50"
        react = "0"
        induct = "0"
        capac = "0"

        xDifference = (int(self.Polygons[int(indexOfPolygon)].XVertices[int(indexOfVertex)]) -
                      int(self.Polygons[int(indexOfPolygon)].XVertices[int(indexOfVertex) + 1])) / 2
        yDifference = (int(self.Polygons[int(indexOfPolygon)].YVertices[int(indexOfVertex)]) - 
                       int(self.Polygons[int(indexOfPolygon)].YVertices[int(indexOfVertex) + 1])) / 2
        xCoord = str(int(abs(xDifference)))
        yCoord = str(int(abs(yDifference)))

        newPort = Port(Type, iPolygon, numPoints, iVertex, portNum, resist, react, induct, capac, xCoord, yCoord)
        self.Ports.append(newPort)
        self.numberOfPorts += 1


    def RemovePort(self):
        print("Выберите, какой порт нужно удалить:")

        for i in range(len(self.Ports)):
            print("[" + str(i) + "] " + self.Ports[i].GetShowPortString())            

        indexOfDeletedPort = input("-> ")
        while int(indexOfDeletedPort) < 0 or int(indexOfDeletedPort) >= len(self.Ports):
            print("Неправильно выбран удаляемый полигон.")
            indexOfDeletedPort = input("Выберите, какой полигон нужно удалить: ")

        self.Ports.pop(int(indexOfDeletedPort))

    def ShowGeometryBlock(self):
        dielectricLayers = ""
        for i in range(len(self.GeometryBox.DielectricLayers)):
            dielectricLayers += "      " 
            dielectricLayers += self.GeometryBox.DielectricLayers[i].GetDielectricLayerString()

        technologyLayers = ""
        for i in range(len(self.TechnologyLayers)):
            technologyLayers += self.TechnologyLayers[i].GetTechnologyLayerString() + "END\nEND\n"
        
        ports = ""
        for i in range(len(self.Ports)):
            ports += self.Ports[i].GetShowPortString()
            
        polygons = ""
        for i in range(self.numberOfPolygons):
            polygons += self.Polygons[i].GetPolygonString()
            polygons += "END\n"

        print("\nGEO" +
              "\nTMET \"" + self.NameTMET + "\" " + self.PatternIdTMET + " " + self.Value1TMET +
              " " + self.Value2TMET + " " + self.Value3TMET + " " + self.Value4TMET + 
              "\nBMET \"" + self.NameBMET + "\" " + self.PatternIdBMET + " " + self.Value1BMET +
              " " + self.Value2BMET + " " + self.Value3BMET + " " + self.Value4BMET + 
              "\nBOX " + self.GeometryBox.NLev + " " + self.GeometryBox.XWidth + " " + 
              self.GeometryBox.YWidth + " " + self.GeometryBox.XCells2 + " " + 
              self.GeometryBox.YCells2 + " " + self.GeometryBox.NSubs + " " + self.GeometryBox.Eeff +
              "\n" + dielectricLayers + technologyLayers +
              "LORGN " + self.X + " " + self.Y + " " + self.UL + 
              "\n" + ports +
              "NUM " + str(self.numberOfPolygons) + "\n" + polygons +
              "END GEO\n")