import os
from DimensionsBlock import DimensionsBlock
from ClassHeader import Header
from ControlBlock import ControlBlock
from Geometry import GeometryBlock
from Frequency import Frequency
from Port import Port
from Polygon import Polygon

class FileOut:
    header = Header("SL636c7473", "04/12/2023 21:17:59", "xgeom 18.53-Lite 04/12/2023 21:17:50", 
                    "sonnet 18.53-Lite", "01/17/2019 10:20:25", "01/17/2019 10:20:25", "")
    dimensions = DimensionsBlock("DEG", "PF", "/OH", "GHZ", "NH", "MIL", "OH")
    control = ControlBlock("VARSWP", "-d", "0", "2", "N")
    geometry = GeometryBlock("Lossless", "0", "SUP", "0", "0", "0", "0", "Lossless", "0", "SUP",
                             "0", "0", "0", "0", "", "", "", "", "0", "250", "U")
    frequency = Frequency("Y", "AY", "ABS_ENTRY 2.0 4.0 -1 300")

    def MakeDielectricLayersString(self):
        dielectricLayers = ""
        for i in range(len(self.geometry.GeometryBox.DielectricLayers)):
            dielectricLayers += "      "
            dielectricLayers += self.geometry.GeometryBox.DielectricLayers[i].GetDielectricLayerString()
        
        return dielectricLayers

    def MakeTechnologyLayersString(self):
        technologyLayers = ""
        for i in range(len(self.geometry.TechnologyLayers)):
            technologyLayers += self.geometry.TechnologyLayers[i].GetTechnologyLayerString()
            technologyLayers += "END\nEND\n"

        return technologyLayers

    def MakePortsString(self):
        ports = ""
        for i in range(len(self.geometry.Ports)):
            ports += self.geometry.Ports[i].GetShowPortString()       
        
        return ports

    def MakePolygonsString(self):
        polygons = ""
        for i in range(self.geometry.numberOfPolygons):
            polygons += self.geometry.Polygons[i].GetPolygonString()
            polygons += "END\n"

        return polygons

    def MakeFile(self):
        
        lines = ["FTYP SONPROJ 19 ! Sonnet Project File",
                 "\nVER 18.53",
                 "\nHEADER",
                 "\nLIC " + self.header.Lic,
                 "\nDAT " + self.header.Date,
                 "\nBUILT_BY_CREATED " + self.header.BuiltByCreated,
                 "\nBUILT_BY_SAVED " + self.header.BuiltBySaved,
                 "\nMDATE " + self.header.MDate,
                 "\nHDATE " + self.header.HDate,
                 "\nEND HEADER",
                 "\nDIM",
                 "\nANG " + self.dimensions.Angle,
                 "\nCAP " + self.dimensions.Capacity,
                 "\nCON " + self.dimensions.Conductance,
                 "\nFREQ " + self.dimensions.Frequency,
                 "\nIND " + self.dimensions.Inductance,
                 "\nLNG " + self.dimensions.Lenght,
                 "\nRES " + self.dimensions.Resistance,
                 "\nEND DIM",
                 "\nCONTROL",
                 "\n" + self.control.Varswp,
                 "\nOPTIONS " + self.control.Options,
                 "\nSPEED " + self.control.Speed,
                 "\nCACHE_ABS " + self.control.CacheABS,
                 "\nQ_ACC " + self.control.QAcc,
                 "\nEND CONTROL",
                 "\nGEO",
                 "\nTMET \"" + self.geometry.NameTMET + "\" " + self.geometry.PatternIdTMET + " " + 
                 self.geometry.TypeTMET + " " + self.geometry.Value1TMET + " " + self.geometry.Value2TMET + 
                 " " + self.geometry.Value3TMET + " " + self.geometry.Value4TMET,
                 "\nBMET \"" + self.geometry.NameBMET + "\" " + self.geometry.PatternIdBMET + " " + 
                 self.geometry.TypeTMET + " " + self.geometry.Value1BMET + " " + self.geometry.Value2BMET + 
                 " " + self.geometry.Value3BMET + " " + self.geometry.Value4BMET,
                 "\nBOX " + self.geometry.defaultGeometryBox.NLev + " " + 
                 self.geometry.defaultGeometryBox.XWidth + " " + self.geometry.defaultGeometryBox.YWidth + " " + 
                 self.geometry.defaultGeometryBox.XCells2 + " " + self.geometry.defaultGeometryBox.YCells2 + " " + 
                 self.geometry.defaultGeometryBox.NSubs + " " + self.geometry.defaultGeometryBox.Eeff,
                 "\n" + self.MakeDielectricLayersString(),
                 self.MakeTechnologyLayersString(),
                 "LORGN " + self.geometry.X + " " + self.geometry.Y + " " + self.geometry.UL + "\n",
                 self.MakePortsString(),
                 "NUM " + str(self.geometry.numberOfPolygons) + "\n",
                 self.MakePolygonsString(),
                 "END GEO\n",
                 "OPT\n", 
                 "MAX 100\n", 
                 "END OPT\n",
                 "VARSWP\n",
                 "ENABLED Y\n",
                 "FREQ " + self.frequency.Y + " " + self.frequency.AY + " " + 
                 self.frequency.SweepType + "\n",
                 "END\n",
                 "END VARSWP"
                 ]

        with open(r"C:\temp\example.son", "w") as f:   
            f.writelines(lines)

        
        path = 'C://Program Files//Sonnet Software//18.53//bin'
        
        command = 'em -v C://temp//example.son'
        
        os.chdir(path)
        os.system(command)
       