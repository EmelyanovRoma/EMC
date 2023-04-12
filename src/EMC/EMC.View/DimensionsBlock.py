class DimensionsBlock:
    def __init__(self, angle, capacity, conductance, frequency, inductance, lenght, resistance):
        self.__ang = angle
        self.__cap = capacity
        self.__con = conductance
        self.__freq = frequency
        self.__ind = inductance
        self.__lng = lenght
        self.__res = resistance

    def GetAngle(self):
        return self.__ang

    def SetAngle(self, angle):
        self.__ang = angle

    def GetCapacity(self):
        return self.__cap

    def SetCapacity(self, capacity):
        self.__cap = capacity

    def GetConductance(self):
        return self.__con

    def SetConductance(self, conductance):
        self.__con = conductance

    def GetFrequency(self):
        return self.__freq

    def SetFrequency(self, frequency):
        self.__freq = frequency

    def GetInductance(self):
        return self.__ind

    def SetInductance(self, inductance):
        self.__ind = inductance

    def GetLenght(self):
        return self.__lng

    def SetLenght(self, lenght):
        self.__lng = lenght

    def GetResistance(self):
        return self.__res

    def SetResistance(self, resistance):
        self.__res = resistance
