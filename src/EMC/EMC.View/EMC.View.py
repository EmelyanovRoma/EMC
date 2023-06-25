def MakeFile():
    header = Header("SL636c7473", "04/12/2023 21:17:59", "xgeom 18.53-Lite 04/12/2023 21:17:50", "sonnet 18.53-Lite", "01/17/2019 10:20:25", "01/17/2019 10:20:25", "")
dimensions = DimensionsBlock("DEG", "PF", "/OH", "GHZ", "NH", "MIL", "OH")
control = ControlBlock("VARSWP", "-d", "0", "2", "N")
geometry = GeometryBlock("Lossless" ,"0","SUP","0","0","0","0","Lossless" ,"0","SUP","0","0","0","0","","","","","0","250","U")
dielectricLayers = ""
for i in range(len(geometry.defaultGeometryBox.dielectricLayers)):
            dielectricLayers = dielectricLayers + "      " + geometry.defaultGeometryBox.dielectricLayers[i].Thickness + " " + geometry.defaultGeometryBox.dielectricLayers[i].Erel + " " + geometry.defaultGeometryBox.dielectricLayers[i].Mrel + " " + geometry.defaultGeometryBox.dielectricLayers[i].Eloss + " " + geometry.defaultGeometryBox.dielectricLayers[i].Mloss + " " + geometry.defaultGeometryBox.dielectricLayers[i].Esignma + " " + geometry.defaultGeometryBox.dielectricLayers[i].Nzpart + " \"" + geometry.defaultGeometryBox.dielectricLayers[i].Name + "\"\n"


lines = ["FTYP SONPROJ 19 ! Sonnet Project File",
         "\nVER 18.53",
         "\nHEADER",
         "\nLIC " + header.Getlicense(),
         "\nDAT " + header.GetDate(),
         "\nBUILT_BY_CREATED " + header.GetbuiltByCreated(),
         "\nBUILT_BY_SAVED " + header.GetbuiltBySaved(),
         "\nMDATE " + header.GetmDate(),
         "\nHDATE " + header.GethDate(),
         "\nEND HEADER",
         "\nDIM",
         "\nANG " + dimensions.Angle,
         "\nCAP " + dimensions.Capacity,
         "\nCON " + dimensions.Conductance,
         "\nFREQ " + dimensions.Frequency,
         "\nIND " + dimensions.Inductance,
         "\nLNG " + dimensions.Lenght,
         "\nRES " + dimensions.Resistance,
         "\nEND DIM",
         "\nCONTROL",
         "\n" + control.Varswp,
         "\nOPTIONS " + control.Options,
         "\nSPEED " + control.Speed,
         "\nCACHE_ABS " + control.CacheABS,
         "\nQ_ACC " + control.QAcc,
         "\nEND CONTROL",
         "\nGEO",
         "\nTMET \"" + geometry.NameTMET + "\" " + geometry.PatternIdTMET + " " + geometry.TypeTMET + " " + geometry.Value1TMET + " " + geometry.Value2TMET + " " + geometry.Value3TMET + " " + geometry.Value4TMET,
         "\nBMET \"" + geometry.NameBMET + "\" " + geometry.PatternIdBMET + " " + geometry.TypeTMET + " " + geometry.Value1BMET + " " + geometry.Value2BMET + " " + geometry.Value3BMET + " " + geometry.Value4BMET,
         "\nBOX 1 350 250 70 50 20 0",
         "\n" + dielectricLayers,
         "TECHLAY " + geometry.defaultTechnologyLayer.LayType + " " + geometry.defaultTechnologyLayer.LayName1 + " " + geometry.defaultTechnologyLayer.LayName2 + " " + geometry.defaultTechnologyLayer.Mapping + " " + geometry.defaultTechnologyLayer.Type + "\n" + geometry.defaultTechnologyLayer.ILevel, 
         " " + geometry.defaultTechnologyLayer.NVertices + " " + geometry.defaultTechnologyLayer.MType + " " + geometry.defaultTechnologyLayer.FillType + " " + geometry.defaultTechnologyLayer.DebugId + " " + geometry.defaultTechnologyLayer.XMin + " " + geometry.defaultTechnologyLayer.YMin, 
         " " + geometry.defaultTechnologyLayer.XMax + " " + geometry.defaultTechnologyLayer.YMax + " " + geometry.defaultTechnologyLayer.ConMax + " " + geometry.defaultTechnologyLayer.Res1 + " " + geometry.defaultTechnologyLayer.Res2 + " " + geometry.defaultTechnologyLayer.Edgemesh,
         "\nEND",
         "\nEND",
         "\nLORGN " + geometry.X + " " + geometry.Y + " " + geometry.UL,
         "\nPOR1 " + geometry.port1.Type,
         "\nPOLY " + geometry.port1.IPolygon + " " + geometry.port1.NumPoints,
         "\n" + geometry.port1.IVertex + "\n" + geometry.port1.PortNum + " " + geometry.port1.Resist + " " + geometry.port1.React + " " + geometry.port1.Induct + " " + geometry.port1.Capac + " " + geometry.port1.XCoord + " " + geometry.port1.YCoord, 
         "\nNUM " + "1",
         "\n" + "0 " + "5 " + "-1 " + "N " + "47 " + "1 " + "1 " + "100 " + "100 " + "0 " + "0 " + "0 " + "Y", 
         "\nTLAYNAM Metal1 INH",
         "\n0 0 \n120 0 \n120 50 \n0 50 \n0 0"
         "\nEND",
         "\nEND GEO",
         "\nOPT",
         "\nMAX 100",
         "\nEND OPT",
         "\nVARSWP",
         "\nENABLED Y",
         "\nFREQ Y AY ABS_ENTRY 2.0 4.0 -1 300",
         "\nEND",
         "\nEND VARSWP"
         ]  



def Menu():
    print("[1] option 1")
    print("[1] option 1")
    print("[0] Выход")

Menu()
option = int(input("Выберите опцию: "))

while option != 0:
    if option == 1:
        # пишем опцию
        pass
    elif option == 2:
         # пишем опцию
        pass
    else:
        print("Такой опции нет")

    Menu()
    option = int(input("Выберите опцию: "))

print("Выход из программы ...")








#with open(r"C:\temp\example.son", "w") as f:   
#    f.writelines(lines)
#
#path = 'C://Program Files//Sonnet Software//18.53//bin'
#
#command = 'em -v C://temp//example.son'
#
#makeDirPath = 'C://'
#
#makeDirPathcommand = 'md temp'
#
#os.chdir(makeDirPath)
#os.system('md temp')
#
#os.chdir(path)
#os.system(command)
