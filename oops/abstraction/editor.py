
from abc import ABC, abstractmethod

class Editor(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class Vscode(Editor):

    def open(self):
         print("open method is start")
         
    def execute(self):
         print("execute method is start")

    def debug(self):
         print("debug method is start")

Vscode1=Vscode()

Vscode1.open()
