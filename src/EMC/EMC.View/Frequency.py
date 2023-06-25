class Frequency :
    def __init__(y,ay,ABSENTRY,start,stop,defelaut,targetFrequency):
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
    def Y(self):
        self.__y = "Y"

    @property
    def AY(self):
        return self.__ay

    @AY.setter
    def AY(self):
        self.__ay = "AY"

    @property
    def ABSENTRY(self):
        return self.__ABSENTRY

    @ABSENTRY.setter
    def ABSENTRY(self):
        self.__ABSENTRY = "ABS_ENTRY"

    @property
    def Defelaut(self):
        return self.__defelaut

    @Defelaut.setter
    def Defelaut(self):
        self.__defelaut = "-1"