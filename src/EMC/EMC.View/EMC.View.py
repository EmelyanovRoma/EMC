from DimensionsBlock import DimensionsBlock
from ClassHeader import Header
from ControlBlock import ControlBlock
from Geometry import GeometryBlock

header = Header("SL636c7473", "04/12/2023 21:17:59", "xgeom 18.53-Lite 04/12/2023 21:17:50", "sonnet 18.53-Lite", "01/17/2019 10:20:25", "01/17/2019 10:20:25", "")

lines = ["FTYP SONPROJ 19 ! Sonnet Project File",
         "\nVER 18.53",
         "\nHEADER",
         "\nLIC " + header.Getlicense(),
         "\nDAT " + header.GetDate(),
         "\nBUILT_BY_CREATED " + header.GetbuiltByCreated(),
         "\nBUILT_BY_SAVED " + header.GetbuiltBySaved(),
         "\nMDATE " + header.GetmDate(),
         "\nHDATE " + header.GethDate(),
         "\nANN " + header.GetaNN(),
         "\nEND HEADER",
         ]  
with open(r"example.txt", "w") as f:
    
    f.writelines(lines)
