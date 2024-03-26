import time
import dictionary
import multiDictionary as md
import richWord

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        str = "C:/Users/Masif/PycharmProjects/Lab03/resources/" + language + ".txt"
        self.dc = dictionary.Dictionary(str)
        riWord = []
        frase = replaceChars(txtIn)
        frase.lower()
        parole = frase.strip().split()

        for p in parole:
            x = richWord.RichWord(p)

            x.corretta = self.dc.contains(p)
            riWord.append(x)

        for p in riWord:
            if p.corretta == False:
                print(f"{p}")







    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~?"
    for c in chars:
        text = text.replace(c, "")
    return text