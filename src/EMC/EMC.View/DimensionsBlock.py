class DimensionsBlock:
    def __init__(self, angle, capacity, conductance, frequency, inductance, lenght, resistance):
        self.ang = angle
        self.cap = capacity
        self.con = conductance
        self.freq = frequency
        self.ind = inductance
        self.lng = lenght
        self.res = resistance

    def GetAngle(self):
        return self.ang

    def SetAngle(self, angle):
        self.ang = angle

    def GetCapacity(self):
        return self.cap

    def SetCapacity(self, capacity):
        self.cap = capacity

    def GetConductance(self):
        return self.con

    def SetConductance(self, conductance):
        self.con = conductance

    def GetFrequency(self):
        return self.freq

    def SetFrequency(self, frequency):
        self.freq = frequency

    def GetInductance(self):
        return self.ind

    def SetInductance(self, inductance):
        self.ind = inductance

    def GetLenght(self):
        return self.lng

    def SetLenght(self, lenght):
        self.lng = lenght

    def GetResistance(self):
        return self.res

    def SetResistance(self, resistance):
        self.res = resistance