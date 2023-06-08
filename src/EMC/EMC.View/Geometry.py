from GeometryBox import GeometryBox
from TechnologyLayer import TechnologyLayer
from Port import Port

class GeometryBlock:
    defaultGeometryBox = GeometryBox("0", "1", "1", "0", "0", "0", "0")
    defaultTechnologyLayer = TechnologyLayer("METAL", "Metal1", "Metal1", "0", "0",
                                      "0", "0", "-1", "N", "40", "1", "1", "100", "100", "0", "0", "0", "Y")
    port1 = Port("BOX", "47", "1", "3", "1", "50", "0", "0", "0", "0", "25")
    def __init__(self, nameTMET, patternIdTMET, typeTMET, value1TMET, value2TMET, value3TMET, value4TMET,
                 nameBMET, patternidBMET, typeBMET, value1BMET, value2BMET, value3BMET, value4BMET,
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
        self.__patternIdBMET = patternidBMET
        self.__typeBMET = typeBMET
        self.__value1BMET = value1BMET
        self.__value2BMET = value2BMET
        self.__value3BMET = value3BMET
        self.__value4BMET = value4BMET

        # GeometryBox
        self.__geometryBox = self.defaultGeometryBox

        # Techlay
        self.__technologyLayers = [self.defaultTechnologyLayer]

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
        self.__ports = [self.port1]
       
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
  
    #TOLEVEL
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