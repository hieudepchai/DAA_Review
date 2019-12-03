class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self, head = None):
        self.head = head

    def printData(self):
        node = self.head
        while node != None:
            print(node.data)
            node= node.next

    def getLength(self):
        node = self.head
        l = 0
        while node != None:
            l+=1
            node= node.next
        return l

    def addNode(self, node, position):
        pos_end = self.getLength()-1
        if position >=0 and position <= pos_end + 1:
            #pos == 0 -> addHead
            if position ==0:
                if self.head == None:
                    self.head = node
                else:
                    node.next = self.head
                    self.head = node
            #pos ==pos_end -> tail node
            elif position == pos_end + 1:
                tailNode = self.head
                while tailNode != None:
                    if tailNode.next == None:
                        break
                    tailNode = tailNode.next
                tailNode.next = node
            else:
            #mid
                ipos = 0
                #find posNode and prevNode
                prevNode = self.head
                while ipos < position - 1:
                    ipos +=1
                    prevNode = prevNode.next
                posNode = prevNode.next
                prevNode.next = node
                node.next = posNode    
            return 1
        else:
            return 0
    def deleteNode(self, position):
        pos_end = self.getLength()-1
        if position >=0 and position <= pos_end:
            #head
            if position == 0:
                nextNode = self.head.next
                del self.head
                self.head = nextNode
            elif position == pos_end:
                next_tailNode = self.head
                while next_tailNode.next.next != None:
                    next_tailNode = next_tailNode.next
                del next_tailNode.next
                next_tailNode.next = None
            else:
                ipos = 0
                prevNode = self.head
                while ipos < position-1:
                    ipos+=1
                    prevNode=prevNode.next
                delNode = prevNode.next
                prevNode.next = delNode.next
                del delNode
            return 1
            
        else:
            return 0
if __name__ == "__main__":
    nodehead = Node(5)
    LL = SLinkedList(nodehead)
    LL.addNode(Node(8), 0)
    LL.addNode(Node(7), 2)
    LL.addNode(Node(10),3)
    LL.addNode(Node(2),2)
    # LL.printData()
    LL.deleteNode(0)
    LL.deleteNode(3)
    LL.deleteNode(1)
    LL.printData()

