from DimensionsBlock import DimensionsBlock

abc = DimensionsBlock("DEG", "PF", "OH", "GHZ", "NH", "MIL", "OH")
abc.SetAngle("RAD")
print("abc = ", abc.GetAngle(), abc.GetCapacity(), abc.GetConductance(), abc.GetFrequency(), abc.GetInductance(), abc.GetLenght(), abc.GetResistance())