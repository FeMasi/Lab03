import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       pass

    def printDic(self, language):
        str = "C:/Users/Masif/PycharmProjects/Lab03/resources/" + language + ".txt"
        self.dc = d.Dictionary(str)

    def searchWord(self, words, language):
        pass


