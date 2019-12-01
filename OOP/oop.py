def reassign(list):
    list = [1,1,1]


class Player:
    minAge= 18
    maxAge = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age



if __name__ == "__main__":
    player1 = Player("hieu", 18)
    player2 = Player("a", 19)
    player2.minAge = 9
    print(player2.minAge)
    lista = [0]
    reassign(lista)
    print(lista)
    x=1
    y=x
    x=2
    print(y)
