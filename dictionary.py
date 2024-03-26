class Dictionary:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dizionario = self.loadDictionary(file_path)

    def loadDictionary(self,path):
        dizionario = []
        try:
            with (open(path, 'r') as file):
                for line in file:
                    parola = line.strip().split()
                    dizionario.append(parola)
            return dizionario
        except FileNotFoundError:
            print("Il file " + path + " non è stato trovato.")
            return {}

    def printAll(self):
        pass

    def contains(self, parola):
        for p in self.dizionario:
            d = p[0]
            if parola == d:

                return True

        return False

    @property
    def dict(self):
        return self._dict


def replaceChars(text1):
    chars = "\\`*_{}[]()>#+-.!$%'^;,=_~?"
    text = str(text1)
    for c in chars:
        text = text.replace(c, "")
    return text