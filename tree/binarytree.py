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
            return node
        return self.__findMin(node.left)
    def findMin(self):
        return self.__findMin(self.root)
    ####
    def __findMax(self, node):
        if node.right is None:
            return node
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
        if root is None:
            return None
        if data < root.data:
            root.left = self.__deleteNode(data, root.left)
        elif data > root.data:
            root.right = self.__deleteNode(data, root.right)
        else:
            if root.left is None:
                temp = root.right
                del root
                return temp
            elif root.right is None:
                temp = root.left
                del root
                return temp
            temp = self.__findMin(root.right)
            root.data = temp.data
            root.right = self.__deleteNode(temp.data, root.right)
        return root
    def deleteNode(self,data):
        return self.__deleteNode(data, self.root)
    ####
    def __getHeight(self, root):
        if root is None:
            return -1
        left_h = self.__getHeight(root.left)
        right_h = self.__getHeight(root.right)
        if left_h > right_h:
            return left_h + 1
        else:
            return right_h + 1
    def getHeight(self):
        return self.__getHeight(self.root)


if __name__ == "__main__":
    tree = BST()
    tree.readFromFile("bstinput.txt")
    tree.printData()
    print()
    print("root: ", tree.root.data)
    search_res = tree.search(14)
    if search_res is None:
        print("not found")
    else:
        print("found")
    tree.deleteNode(13)
    tree.printData()