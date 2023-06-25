class Frequency :
    def __init__(self,y,ay,ABSENTRY,start,stop,defelaut,targetFrequency):
        self.__start = start    
        self.__stop = stop
        self.__targetFrequency = targetFrequency
        self.__y = y
        self.__ay = ay
        self.__ABSENTRY = ABSENTRY
        self.__defelaut = defelaut

    @property
    def Start(self):
        return self.__start

    @Start.setter
    def Start(self, start):
        self.__start = start

    @property
    def Stop(self):
        return self.__stop

    @Stop.setter
    def Stop(self, stop):
        self.__stop = stop

    @property
    def TargetFrequency(self):
        return self.__targetFrequency

    @TargetFrequency.setter
    def TargetFrequency(self, targetFrequency):
        self.__targetFrequency = targetFrequency

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
    def ABSENTRY(self):
        return self.__ABSENTRY

    @ABSENTRY.setter
    def ABSENTRY(self,ABSENTRY):
        self.__ABSENTRY = ABSENTRY

    @property
    def Defelaut(self):
        return self.__defelaut

    @Defelaut.setter
    def Defelaut(self,defelaut):
        self.__defelaut = defelaut




