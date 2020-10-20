class UnsortedArray:
    def __init__( self):
        self.listNodes = []
        self.listDist = []
        pass

    def deleteMin(self, deleteKey):
        index = 0
        for i in self.listDist:
            if i == deleteKey:
                index = i
                self.listDist.pop(i)
        self.listNodes.pop(index)


    def insert(self, newInsert,newDist):
        self.listNodes.append(newInsert)
        self.listDist.append(newDist)

    def makeQueue(self, newList, newListDist):
        self.listNodes.extend(newList)
        self.listDist.extend(newListDist)

    def decreaseKey(self, itemDecreased, decreasedKey):
        index = self.listNodes.index(itemDecreased)
        self.listDist[index] = decreasedKey
        #do nothing