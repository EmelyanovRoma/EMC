class FileOutBlock(object):
    def __init__(fileType, embed, ABS_inc, fileName, comments, sig, parType,parForm,ports):
        self.__fileType = fileType
        self.__embed = embed
        self.__ABS_inc = ABS_inc
        self.__fileName = fileName
        self.__comments = comments
        self.__sig = sig
        self.__parType = parType
        self.__parForm = parForm
        self.__ports = ports
    
    def GetfileType(self):
        return self.__fileType

    def SetfileType(self, fileType):
        self.__fileType = fileType

    def GetEmbed(self):
        return self.__embed

    def SetEmbed(self, embed):
        self.__embed = embed

    def GetABS_inc(self):
        return self.__ABS_inc

    def SetABS_inc(self, ABS_inc):
        self.__ABS_inc = ABS_inc

    def GetfileName(self):
        return self.__fileName

    def SetfileName(self, fileName):
        self.__fileName = fileName
    
    def GetComments(self):
        return self.__comments

    def SetComments(self, comments):
       self.__comments =  comments

    def GetSig(self):
        return self.__sig

    def SetSig(self, sig):
        self.__sig = sig

    def GetParType(self):
        return self.__parType

    def SetParType(self, parType):
        self.__parType = parType

    def GetParForm(self):
        return self.__parForm

    def SetParForm(self, parForm):
        self.__parForm = parForm

    def GetPorts(self):
        return self.__ports

    def SetPorts(self, ports):
        self.__ports = ports
    
    




