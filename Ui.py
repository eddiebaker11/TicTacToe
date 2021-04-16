from abc import ABC, abstractmethod

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        print("Running the gui!")
        pass

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()

    def run(self):
        while not self.__game.winner:
            print(self.__game)
            row = int(input("Enter row"))
            col = int(input("Enter col"))
            self.__game.play(row,col)
