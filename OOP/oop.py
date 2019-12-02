# def reassign(list):
#     list = [1,1,1]


# class Player:
#     minAge= 18
#     maxAge = 50
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

class shape:
    detail = "shape class"
    def __init__(self, color='red'):
        self.__color = color
    def printShape(self):
        print("this is shape class")
    def setColor(self, color):
        self.__color = color
    def printColor(self):
        print("color:", self.__color)
    def printInfo(self):
        print("Shape info")

class rect(shape):
    rect_detail = "rect class"
    def __init__(self, w, h):
        super().__init__()
        self.width= w
        self.height = h
    def printInfo(self):
        print("Rect info:", self.width, self.height)    

if __name__ == "__main__":
    # player1 = Player("hieu", 18)
    # player2 = Player("a", 19)
    # player2.minAge = 9
    # print(player2.minAge)
    # lista = [0]
    # reassign(lista)
    # print(lista)
    # x=1
    # y=x
    # x=2
    # print(y)
    rect1 = rect(8, 9)
    print(rect1.rect_detail)
    print(rect1.detail)
    rect1.printColor()
    rect1.printInfo()
