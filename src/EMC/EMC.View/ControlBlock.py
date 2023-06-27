class ControlBlock:
    def __init__(self, varswp, options, speed, cacheABS, qAcc):
        self.__varswp = varswp
        self.__options = options
        self.__speed = speed
        self.__cacheAbs = cacheABS
        self.__qAcc = qAcc


    @property
    def Varswp(self):
        return self.__varswp

    @Varswp.setter
    def Varswp(self, varswp):
        self.__varswp = varswp


    @property
    def Options(self):
        return self.__options
    
    @Options.setter
    def Options(self, options):
        self.__options = options


    @property
    def Speed(self):
        return self.__speed

    @Speed.setter
    def Speed(self, speed):
        self.__speed = speed


    @property
    def CacheABS(self):
        return self.__cacheAbs

    @CacheABS.setter
    def CacheABS(self, cacheAbs):
        self.__cacheAbs = cacheAbs


    @property
    def QAcc(self):
        return self.__qAcc

    @QAcc.setter
    def QAcc(self, qAcc):
        self.__qAcc = qAcc


    def ChangeOptions(self):
        print("\nВыберите параметр управления анализом:" +
              "\n1) Генерация плотности тока;" +
              "\n2) Многочастотное кэширование;" + 
              "\n3) Экономия памяти;" + 
              "\n4) Резонирующая коробка;" +
              "\n5) De-embedding.")

        value = int(input("-> "))
        match value:
            case 1:
                self.Options = "-j"
            case 2:
                self.Options = "-A"
            case 3:
                self.Options = "-m"
            case 4:
                self.Options = "-b"
            case 5:
                self.Options = "-d"
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeOptions()

    def ChangeSpeed(self):
        print("\nВыберите скорость анализа/управления памятью:" + 
              "\n1) Fine/Edge Meshing (Left on Slider);" + 
              "\n2) Coarse/Edge Meshing (Middle on Slider);" + 
              "\n3) Coarse/No Edge Meshing (Right on Slider).")

        value = int(input("-> "))
        match value:
            case 1:
                self.Speed = "0"
            case 2:
                self.Speed = "1"
            case 3:
                self.Speed = "2"
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeSpeed()

    def ChangeCacheABS(self):
        print("\nВыберите уровень ABS кэширования:" + 
              "\n1) Нет;" + 
              "\n2) Стоп/Перезагрузка;" + 
              "\n3) Мультиразвертка и Стоп/Перезагрузка.\n")

        value = int(input("-> "))
        match value:
            case 1:
                self.CacheABS = "0"
            case 2:
                self.CacheABS = "1"
            case 3:
                self.CacheABS = "2"
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeCacheABS()

    def ChangeQAcc(self):
        print("\nБудет ли использоваться Q-фактор точности?" + 
              "\n1) Да;" + 
              "\n2) Нет.\n")

        value = int(input("-> "))
        match value:
            case 1:
                self.QAcc = "Y"
            case 2:
                self.QAcc = "N"
            case _:
                print("\nЗначение введено неверно.")
                self.ChangeQAcc()

    def ShowControlBlock(self):
        print("\nCONTROL\n", 
              self.Varswp, 
              "\nOPTIONS ", self.Options, 
              "\nSPEED ", self.Speed, 
              "\nCACHE_ABS ", self.CacheABS,  
              "\nQ_ACC ", self.QAcc, 
              "\nEND CONTROL\n")