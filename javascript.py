from directory import Directory
from fichier import Fichier
class Js(Directory):
    def __init__(self,name):
        self.name=name
        self.content=Fichier("./",name).lire()
        self.js=True
    def get_html(self):
        return self.content.encode()
