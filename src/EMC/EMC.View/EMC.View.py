from Geometry import GeometryBlock

abc = GeometryBlock("Lossless" ,"0","SUP","0","0","0","0","Lossless" ,"0","SUP","0","0","0","0","1","350","250","70","50","20","0","0","1","1","0","0","0","0","Air")

print("GEO")
print("TMET",abc.GetNameTMET(),abc.GetPatternidTMET(),abc.GetTypeTMET(),abc.GetValue1TMET(),abc.GetValue1TMET(),abc.GetValue2TMET(),abc.GetValue3TMET(),abc.GetValue4TMET())
print("BMET",abc.GetNameBMET(),abc.GetPatternidBMET(),abc.GetTypeBMET(),abc.GetValue1BMET(),abc.GetValue1BMET(),abc.GetValue2BMET(),abc.GetValue3BMET(),abc.GetValue4BMET())
print("BOX",abc.Getnlev(),abc.Getxwidth(),abc.Getywidth(),abc.Getxcells2(),abc.Getycells2(),abc.Getnsubs(),abc.Geteeff())
print("   ",abc.Getthickness(),abc.Geterel(),abc.Getmrel(),abc.Geteloss(),abc.Getmloss(),abc.Getesignma(),abc.Getnzpart(),abc.Getname(),abc.Getnlev())
print("   ","0","1","1","0","0","0","0", "Substrate")
print("TECHLAY","METAL","Metal1","<UNSPECIFIED>","-2","-65534")
print("0","0","-1","N","9","1","1","100","100","0","0","0","Y")      
print("END")
print("END")  
print("LORGN","0","250","U")
print("NUM","0")
print("END","GEO")