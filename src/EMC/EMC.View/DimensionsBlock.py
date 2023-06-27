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
        print("\nВыберите единицу измерения частоты:" +
              "\n1) Гц;\n2) кГц;\n3) МГц;\n4) ГГц;\n5) ТГц;\n6) ПГц\n")

        value = int(input("-> "))
        match value:
            case 1:
                self.Resistance = "HZ"
            case 2:
                self.Resistance = "KHZ"
            case 3:
                self.Resistance = "MHZ"
            case 4:
                self.Resistance = "GHZ"
            case 5:
                self.Resistance = "THZ"
            case 6:
                self.Resistance = "PHZ"
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeFrequencyUnit()

    def ChangeInductivityUnit(self):
        print("\n\nВыберите единицу измерения индуктивности:" +
            "\n1) Гн;\n2) мГн;\n3) мкГн;\n4) нГн;\n5) пГн\n6) фГн\n")

        value = int(input("-> "))
        match value:
            case 1:
                self.Resistance = "H"
            case 2:
                self.Resistance = "MH"
            case 3:
                self.Resistance = "UH"
            case 4:
                self.Resistance = "NH"
            case 5:
                self.Resistance = "PH"
            case 6:
                self.Resistance = "FH"
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeInductivityUnit()

    def ChangeLenghtUnit(self):
        print("\nВыберите единицу измерения расстояния:" +
            "\n1) мил;\n2) мкм;\n3) мм;\n4) см;\n5) дюйм\n6) метр\n7) фут\n")
        
        value = int(input("-> "))
        match value:
            case 1:
                self.Resistance = "MIL"
            case 2:
                self.Resistance = "UM"
            case 3:
                self.Resistance = "MM"
            case 4:
                self.Resistance = "CM"
            case 5:
                self.Resistance = "IN"
            case 6:
                self.Resistance = "M"
            case 7:
                self.Resistance = "FT"
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeLenghtUnit()

    def ChangeResistanceUnit(self):
        print("\nВыберите единицу измерения сопротивления:" +
            "\n1) мОм;\n2) Ом;\n3) кОм;\n4) МОм;\n5) ГОм\n6) ТОм\n")

        value = int(input("-> "))
        match value:
            case 1:
                self.Resistance = "WOH"
            case 2:
                self.Resistance = "OH"
            case 3:
                self.Resistance = "KOH"
            case 4:
                self.Resistance = "MOH"
            case 5:
                self.Resistance = "GOH"
            case 6:
                self.Resistance = "TOH"
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeResistanceUnit()

    def ChangeCapacitanceUnit(self):
        print("\nВыберите единицу измерения емкости:" + 
              "\n1) Ф; \n2) мФ;\n3) мкФ;\n4) нФ;\n5) пФ;\n6) фФ\n")

        value = int(input("-> "))
        match value:
            case 1:
                self.Capacity = "F"
            case 2:
                self.Capacity = "MF"
            case 3:
                self.Capacity = "UF"
            case 4:
                self.Capacity = "NF"
            case 5:
                self.Capacity = "PF"
            case 6:
                self.Capacity = "FF"               
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeCapacitanceUnit()

    def ShowDimensionsBlock(self):
        print("\nDIM", 
            "\nANG ", self.Angle, 
            "\nCAP ", self.Capacity, 
            "\nCON ", self.Conductance, 
            "\nFREQ ", self.Frequency, 
            "\nIND ", self.Inductance, 
            "\nLNG ", self.Lenght, 
            "\nRES ", self.Resistance, 
            "\nEND DIM\n")
