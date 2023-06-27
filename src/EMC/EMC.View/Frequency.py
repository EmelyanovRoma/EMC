class Frequency :
    def __init__(self, y, ay, sweepType):
        self.__y = y
        self.__ay = ay
        self.__sweepType = sweepType


    @property
    def Y(self):
        return self.__y

    @Y.setter
    def Y(self,y):
        self.__y = y


    @property
    def AY(self):
        return self.__ay

    @AY.setter
    def AY(self,ay):
        self.__ay = ay


    @property
    def SweepType(self):
        return self.__sweepType

    @SweepType.setter
    def SweepType(self, sweepType):
        self.__sweepType = sweepType


    @property
    def Default(self):
        return self.__default

    @Default.setter
    def Default(self, default):
        self.__default = default


    def ChangeSweepType(self):
        print("Выберите тип развертки:\n" + 
              "1) Адаптивная развертка;\n" +
              "2) Линейная развертка;\n" +
              "3) Экспоненциальная развертка;\n" +
              "4) Список частот;\n" + 
              "5) Постоянная частота.\n")

        value = int(input("-> "))
        match value:
            case 1:
                startFreq = input("Введите начальную частоту -> ")
                endFreq = input("Введите конечную частоту -> ")
                self.SweepType = "ABS_ENTRY " + startFreq + " " + endFreq + " -1 300"
            case 2:
                startFreq = input("Введите начальную частоту -> ")
                endFreq = input("Введите конечную частоту -> ")
                step = input("Введите размер шаг -> ")
                self.SweepType = "SWEEP " + startFreq + " " + endFreq + " " + step
            case 3:
                startFreq = input("Введите начальную частоту -> ")
                endFreq = input("Введите конечную частоту -> ")
                numOfPoints = input("Введите количество точек -> ")
                self.SweepType = "ESWEEP " + + startFreq + " " + endFreq + " " + numOfPoints
            case 4:
                self.SweepType = "LIST"
                numOfFreq = int(input("Введите количество частот -> "))
                
                for i in range(numOfFreq):
                    self.SweepType += input("Введите частоту -> ") + " "
            case 5:
                singleFreq = input("Введите постоянную частоту -> ")
                self.SweepType = "STEP " + singleFreq       
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeSweepType()

    def ShowFrequency(self):
        print("\nFREQ " +
              self.Y + " " +
              self.AY + " " +
              self.SweepType + "\n")