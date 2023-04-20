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
        print("\nChoose analysis control options:" +
              "\n1) Generate Current Density;" +
              "\n2) Multi-Frequency Caching;" + 
              "\n3) Memory Saver;" + 
              "\n4) Box Resonance;" +
              "\n5) De-embedding.")

        value = input()
        if value == '1':
            self.Options = "-j"
        if value == '2':
            self.Options = "-A"
        if value == '3':
            self.Options = "-m"
        if value == '4':
            self.Options = "-b"
        if value == '5':    
            self.Options = "-d"

    def ChangeSpeed(self):
        print("\nChoose analysis speed/memory control:" + 
              "\n1) Fine/Edge Meshing (Left on Slider);" + 
              "\n2) Coarse/Edge Meshing (Middle on Slider);" + 
              "\n3) Coarse/No Edge Meshing (Right on Slider).")

        value = input()
        if value == '1':
            self.Speed = "0"
        if value == '2':
            self.Speed = "1"
        if value == '3':
            self.Speed = "2"

    def ChangeCacheABS(self):
        print("\nChoose ABS caching level:" + 
              "\n1) None;" + 
              "\n2) Stop/Restart;" + 
              "\n3) Multi-sweep plus Stop/Restart.")

        value = input()
        if value == '1':
            self.Speed = "0"
        if value == '2':
            self.Speed = "1"
        if value == '3':
            self.Speed = "2"

    def ChangeQAcc(self):
        print("\nChoose Q-Factor Accuracy:" + 
              "\n1) Yes;" + 
              "\n2) No.")

        value = input()
        if value == '1':
            self.Speed = "Y"
        if value == '2':
            self.Speed = "N"

    def ShowControlBlock(self):
        print("\nCONTROL", 
            "\n", self.Varswp, 
            "\nOPTIONS ", self.Options, 
            "\nSPEED ", self.Speed, 
            "\nCACHE_ABS ", self.CacheABS,  
            "\nQ_ACC ", self.QAcc, 
            "\nEND CONTROL")