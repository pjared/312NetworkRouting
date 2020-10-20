class BinaryHeap:
    def __init__( self):
        self.listNodes = []
        self.listDist = []
        pass

    def bubbleUp(self, node):
        index = 0
        while True:
            if index == 0:
                break
            #get parent
            listDistParent = 9
            if self.listDist[index] < listDistParent:
                break
            else:
                temp = self.listDist[index]
                #write the parent to the child
                #put temp into parent
                #repeat for listDist

    def deleteMin(self, deleteKey):
        #delete the piece at the top
        #move very last node to top
        #bubble it down
        index = 0
        for i in self.listDist:
            if i == deleteKey:
                index = i
                self.listDist.pop(i)
                #restructure the tree
        self.listNodes.pop(index)


    def insert(self, newInsert,newDist):
        #place at the bottom, let it bubble up.
        #if smaller than parent, swap 2 and repeat
        self.listNodes.append(newInsert)
        self.listDist.append(newDist)

    def makeQueue(self, newList, newListDist):
        #place in order and go through every node to make sure
        #that it's not larger than it's parent?
        self.listNodes.extend(newList)
        self.listDist.extend(newListDist)

    def decreaseKey(self, itemDecreased):
        #move value down, compare it to its parents and let it bubble up
        print("do nothing")
        #do nothing