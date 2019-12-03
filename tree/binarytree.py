import os
class Node:
    def __init__(self, data =None):
        self.data= data
        self.left = None
        self.right = None
class BST:
    def __init__(self, root = None):
        self.root = root

    def __insert(self, data, root):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self.__insert(data, root.left)
        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                self.__insert(data, root.right)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert(data, self.root)    
    ####           
    def __printData(self, node):
        if node is None:
            return
        self.__printData(node.left)
        print(node.data, end=" ")
        self.__printData(node.right) 

    def printData(self):
        self.__printData(self.root)
    ####    
    def readFromFile(self, filename):
        inFile = open('tree/'+filename, 'r')
        arrNum = [int(i) for i in inFile.readline().split()]
        for num in arrNum:
            self.insert(num)
    ####
    def __findMin(self, node):
        if node.left is None:
            return node.data
        return self.__findMin(node.left)
    def findMin(self):
        return self.__findMin(self.root)
    ####
    def __findMax(self, node):
        if node.right is None:
            return node.data
        return self.__findMax(node.right)
    def findMax(self):
        return self.__findMax(self.root)
    ####
    def __search(self, data, root):
        if root is None:
            return None
        if root.data > data: 
            return self.__search(data, root.left)
        elif root.data < data:   
            return self.__search(data, root.right)
        else:
            return root
    def search(self, data):
        return self.__search(data, self.root)
    def __deleteNode(self, data, root):
        pass


if __name__ == "__main__":
    tree = BST()
    tree.readFromFile("bstinput.txt")
    tree.printData()
    print()
    print("root: ", tree.root.data)
    print("min: ", tree.findMin())