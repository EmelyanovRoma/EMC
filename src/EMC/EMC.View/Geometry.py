class GeometryBlock:
    def __init__(self,NameTMET,PatternidTMET,TypeTMET,Value1TMET,Value2TMET,Value3TMET,Value4TMET,
                 NameBMET,PatternidBMET,TypeBMET,Value1BMET,Value2BMET,Value3BMET,Value4BMET,
                 nlev,xwidth,ywidth,xcells2,ycells2,nsubs,eeff,
                 thickness,erel,mrel,eloss,mloss,esignma,nzpart,name, LayType, LayName, Mapping, 
                 Type, Ilevel, Nvertices, Mtype, Filltype, Debugid, Xmin, Ymin, Xmax, Ymax, Conmax1, 
                 Res1, Res2, Edgemesh, ToLevel, Conmax2, Meshingfill, Pads, X, Y, UL):
        #TMET
        self.__NameTMET = NameTMET
        self.__PatternidTMET = PatternidTMET
        self.__TypeTMET = TypeTMET
        self.__Value1TMET = Value1TMET
        self.__Value2TMET = Value2TMET
        self.__Value3TMET = Value3TMET
        self.__Value4TMET = Value4TMET
        #BMET
        self.__NameBMET = NameBMET
        self.__PatternidBMET = PatternidBMET
        self.__TypeBMET = TypeBMET
        self.__Value1BMET = Value1BMET
        self.__Value2BMET = Value2BMET
        self.__Value3BMET = Value3BMET
        self.__Value4BMET = Value4BMET
        #BOX
        self.__nlev = nlev
        self.__xwidth = xwidth
        self.__ywidth = ywidth
        self.__xcells2 = xcells2
        self.__ycells2 = ycells2
        self.__nsubs = nsubs
        self.__eeff = eeff
        #Box
        self.__thickness = thickness
        self.__erel = erel
        self.__mrel = mrel
        self.__eloss = eloss
        self.__mloss = mloss
        self.__esignma = esignma
        self.__nzpart = nzpart
        self.__name = name
        #TECHLAY
        self.__lay_type = LayType
        self.__lay_name = LayName
        self.__mapping = Mapping
        self.__type = Type
        self.__ilevel = Ilevel
        self.__nvertices = Nvertices
        self.__mtype = Mtype
        self.__filltype = Filltype
        self.__debugid = Debugid
        self.__xmin = Xmin
        self.__ymin = Ymin
        self.__xmax = Xmax
        self.__ymax = Ymax
        self.__conmax1 = Conmax1
        self.__res1 = Res1
        self.__res2 = Res2
        self.__edgemesh = Edgemesh
        #TOLEVEL
        self.__tolevel = ToLevel
        self.__conmax2 = Conmax2
        self.__meshingfill = Meshingfill
        self.__pads = Pads
        #LORGN
        self.__x = X
        self.__y = Y
        self.__uL = UL

        #Box
    def Getthickness(self):
        return self.__thickness
    def Setthickness(self, thickness):
        self.__thickness = thickness

        #Box
    def Getthickness(self):
        return self.__thickness
    def Setthickness(self, thickness):
        self.__thickness = thickness


    def Geterel(self):
            return self.__erel
    def Seterel(self, erel):
        self.__erel = erel

    def Getmrel(self):
            return self.__mrel
    def Setmrel(self, mrel):
        self.__mrel = mrel
        
    def Geteloss(self):
            return self.__eloss
    def Seteloss(self, eloss):
        self.__eloss = eloss

    def Getmloss(self):
            return self.__mloss
    def Setmloss(self, mloss):
        self.__mloss = mloss

    def Getesignma(self):
            return self.__esignma
    def Setesignma(self, esignma):
        self.__esignma = esignma

    def Getnzpart(self):
            return self.__nzpart
    def Setnzpart(self, nzpart):
        self.__nzpart = nzpart 

    def Getname(self):
            return self.__name
    def Setname(self, name):
        self.__name = name
    #BOX
    def Getnlev(self):
        return self.__nlev
    def Setnlev(self, nlev):
        self.__nlev = nlev

    def Getxwidth(self):
            return self.__xwidth
    def Setxwidth(self, xwidth):
        self.__xwidth = xwidth

    def Getywidth(self):
            return self.__ywidth
    def Setywidth(self, ywidth):
        self.__ywidth = ywidth
        
    def Getxcells2(self):
            return self.__xcells2
    def Setxcells2(self, xcells2):
        self.__xcells2 = xcells2

    def Getycells2(self):
            return self.__ycells2
    def Setycells2(self, ycells2):
        self.__ycells2 = ycells2

    def Getnsubs(self):
            return self.__nsubs
    def Setnsubs(self, nsubs):
        self.__nsubs = nsubs

    def Geteeff(self):
            return self.__eeff
    def Seteeff(self, eeff):
        self.__eeff = eeff 
    #TMET
    def GetNameTMET(self):
        return self.__NameTMET
    def SetNameTMET(self, NameTMET):
        self.__NameTMET = NameTMET

    def GetPatternidTMET(self):
            return self.__PatternidTMET
    def SetPatternidTMET(self, PatternidTMET):
        self.__PatternidTMET = PatternidTMET

    def GetTypeTMET(self):
            return self.__TypeTMET
    def SetTypeTMET(self, TypeTMET):
        self.__TypeTMET = TypeTMET
        
    def GetValue1TMET(self):
            return self.__Value1TMET
    def SetValue1TMET(self, Value1TMET):
        self.__Value1TMET = Value1TMET

    def GetValue2TMET(self):
            return self.__Value2TMET
    def SetValue2TMET(self, Value2TMET):
        self.j__Value2TMET = Value2TMET

    def GetValue3TMET(self):
            return self.__Value3TMET
    def SetValue3TMET(self, Value3TMET):
        self.__Value3TMET = Value3TMET

    def GetValue4TMET(self):
            return self.__Value4TMET
    def SetValue4TMET(self, Value4TMET):
        self.__Value4TMET = Value4TMET 

        #BMET
    def GetNameBMET(self):
        return self.__NameBMET
    def SetNameBMET(self, NameBMET):
        self.__NameBMET = NameBMET

    def GetPatternidBMET(self):
            return self.__PatternidBMET
    def SetPatternidBMET(self, PatternidBMET):
        self.__PatternidBMET = PatternidBMET

    def GetTypeBMET(self):
            return self.__TypeBMET
    def SetTypeBMET(self, TypeBMET):
        self.__TypeBMET = TypeBMET
        
    def GetValue1BMET(self):
            return self.__Value1BMET
    def SetValue1BMET(self, Value1BMET):
        self.__Value1BMET = Value1BMET

    def GetValue2BMET(self):
            return self.__Value2BMET
    def SetValue2BMET(self, Value2BMET):
        self.__Value2BMET = Value2BMET

    def GetValue3BMET(self):
            return self.__Value3BMET
    def SetValue3BMET(self, Value3BMET):
        self.__Value3BMET = Value3BMET

    def GetValue4BMET(self):
            return self.__Value4BMET
    def SetValue4BMET(self, Value4BMET):
        self.__Value4BMET = Value4BMET

    #TECHLAY
    def GetLayType(self):
        return self.__lay_type
    def SetLayType(self, LayType):
        self.__lay_type = LayType

    def GetLayName(self):
        return self.__lay_name
    def SetLayName(self, LayName):
        self.__lay_name = LayName

    def GetMapping(self):
        return self.__mapping
    def SetMapping(self, Mapping):
        self.__mapping = Mapping

    def GetType(self):
        return self.__type
    def SetType(self, Type):
        self.__type = Type

    def GetIlevel(self):
        return self.__ilevel
    def SetIlevel(self, Ilevel):
        self.__ilevel = Ilevel

    def GetNvertices(self):
        return self.__nvertices
    def SetNvertices(self, Nvertices):
        self.__nvertices = Nvertices

    def GetMtype(self):
        return self.__mtype
    def SetMtype(self, Mtype):
        self.__mtype = Mtype

    def GetFilltype(self):
        return self.__filltype
    def SetFilltype(self, Filltype):
        self.__filltype = Filltype
       
    def GetDebugid(self):
        return self.__debugid
    def SetDebugid(self, Debugid):
        self.__debugid = Debugid

    def GetXmin(self):
        return self.__xmin
    def SetXmin(self, Xmin):
        self.__xmin = Xmin

    def GetYmin(self):
        return self.__ymin
    def SetYmin(self, Ymin):
        self.__ymin = Ymin

    def GetXmax(self):
        return self.__xmax
    def SetXmax(self, Xmax):
        self.__xmax = Xmax

    def GetYmax(self):
        return self.__ymax
    def SetYmax(self, Ymax):
        self.__ymax = Ymax

    def GetConmaxx1(self):
        return self.__conmax1
    def SetConmax1(self, Conmax1):
        self.__conmax1 = Conmax1

    def GetRes1(self):
        return self.__res1
    def SetRes1(self, Res1):
        self.__res1 = Res1

    def GetRes2(self):
        return self.__res2
    def SetRes2(self, Res2):
        self.__res2 = Res2
    
    def GetEdgemesh(self):
        return self.__edgemesh
    def SetEdgemesh(self, Edgemesh):
        self.__edgemesh = Edgemesh
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
    def GetX(self):
        return self.__x
    def SetX(self, X):
        self.__x = X
    
    def GetY(self):
        return self.__y
    def SetY(self, Y):
        self.__y = Y
    
    def GetUL(self):
        return self.__uL
    def SetUL(self, UL):
        self.__uL = UL