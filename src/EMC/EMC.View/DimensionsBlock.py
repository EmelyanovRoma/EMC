# Класс с полями, отвечающими за единицы измерения
class DimensionsBlock:

    # Конструктор класса
    def __init__(self, angle, capacity, conductance, frequency, inductance, lenght, resistance):
        self.__ang = angle
        self.__cap = capacity
        self.__con = conductance
        self.__freq = frequency
        self.__ind = inductance
        self.__lng = lenght
        self.__res = resistance


    @property
    def Angle(self):
        return self.__ang

    @Angle.setter
    def Angle(self, angle):
        self.__ang = angle


    @property
    def Capacity(self):
        return self.__cap

    @Capacity.setter
    def Capacity(self, capacity):
        self.__cap = capacity


    @property
    def Conductance(self):
        return self.__con

    @Conductance.setter
    def Conductance(self, conductance):
        self.__con = conductance


    @property
    def Frequency(self):
        return self.__freq

    @Frequency.setter
    def Frequency(self, frequency):
        self.__freq = frequency


    @property
    def Inductance(self):
        return self.__ind

    @Inductance.setter
    def Inductance(self, inductance):
        self.__ind = inductance


    @property
    def Lenght(self):
        return self.__lng

    @Lenght.setter
    def Lenght(self, lenght):
        self.__lng = lenght


    @property
    def Resistance(self):
        return self.__res

    @Resistance.setter
    def Resistance(self, resistance):
        self.__res = resistance

    def ChangeFrequencyUnit(self):
        print("Choose frequency unit:" +
            "\n1) HZ;\n2) KHZ;\n3) MHZ;\n4) GHZ;\n5) THZ\n6) PHZ")

        value = input()
        if value == '1':
            self.Frequency = "HZ"
        if value == '2':
            self.Frequency = "KHZ"
        if value == '3':
            self.Frequency = "MHZ"
        if value == '4':
            self.Frequency = "GHZ"
        if value == '5':
            self.Frequency = "THZ"
        if value == '6':
            self.Frequency = "HZ"

    def ChangeInductivityUnit(self):
        print("\nChoose inductivity unit:" +
            "\n1) H;\n2) MH;\n3) UH;\n4) NH;\n5) PH\n6) FH")

        value = input()
        if value == '1':
            self.Inductance = "H"
        if value == '2':
            self.Inductance = "MH"
        if value == '3':
            self.Inductance = "UH"
        if value == '4':
            self.Inductance = "NH"
        if value == '5':    
            self.Inductance = "PH"
        if value == '6':     
            self.Inductance = "FH"

    def ChangeLenghtUnit(self):
        print("\nChoose lenght unit:" +
            "\n1) MIL;\n2) UM;\n3) MM;\n4) CM;\n5) IN\n6) M\n7) FT")

        value = input()
        if value == '1':
            self.Lenght = "MIL"
        if value == '2':
            self.Lenght = "UM"
        if value == '3':
            self.Lenght = "MM"
        if value == '4':
            self.Lenght = "CM"
        if value == '5':
            self.Lenght = "IN"
        if value == '6':
            self.Lenght = "M"
        if value == '7':
            self.Lenght = "FT"

    def ChangeResistanceUnit(self):
        print("\nChoose resistance unit:" +
            "\n1) WOH;\n2) OH;\n3) KOH;\n4) MOH;\n5) GOH\n6) TOH")

        value = input()
        if value == '1':
            self.Resistance = "WOH"
        if value == '2':
            self.Resistance = "OH"
        if value == '3':
            self.Resistance = "KOH"
        if value == '4':
            self.Resistance = "MOH"
        if value == '5':
            self.Resistance = "GOH"
        if value == '6':
            self.Resistance = "TOH"

    def ShowDimensionsBlock(self):
        print("\nDIM", 
            "\nANG ", self.Angle, 
            "\nCAP ", self.Capacity, 
            "\nCON ", self.Conductance, 
            "\nFREQ ", self.Frequency, 
            "\nIND ", self.Inductance, 
            "\nLNG ", self.Lenght, 
            "\nRES ", self.Resistance, 
            "\nEND DIM")
