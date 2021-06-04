import  re
import  urllib.request
from bs4    import  BeautifulSoup

#Link de prueba:                    https://stackoverflow.com/

class scp:
    pass
    def __init__(self,  link,   regex):
        self.link   =   link
        self.regex  =   regex
        self.get    =   urllib.request.urlopen(self.link)
        self.html   =   self.get.read()
        self.soup   =   BeautifulSoup(self.html,    features='lxml')
        self.soup2  =   str(self.soup.encode("utf-8"))
    
    def buscar(self):
        self.cadena =   re.findall(self.regex,  self.soup2)
        self.compresion =   [x[0]for x  in self.cadena]
        return  self.compresion

    def ordenar(self,   compresion):
        self.contador   =   0
        self.compresion =   compresion
        for i in    self.compresion:
            self.cadenaLink =   str(i)
            self.contador   +=  1
            print(f'{self.contador} | {self.cadenaLink} \n')

pagina  =   input("URL: ")

obj =   scp(pagina,   '((http|ftp|https)(:\/\/)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?)')
obj.ordenar(obj.buscar())

input()