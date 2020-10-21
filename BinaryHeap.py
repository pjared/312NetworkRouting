class BinaryHeap:
    #Lines to double check that code is correct
    #line 15 (parentIndex), 57 continue statement
    def __init__( self):
        self.listNodes = []
        self.listDist = []
        pass

    def bubbleUp(self, nodeIndex):
        index = nodeIndex
        while True:
            if index == 0:
                break
            #get parent
            parentIndex = ((nodeIndex + 1) // 2) - 1
            listDistParent = self.listDist[parentIndex]
            if self.listDist[index] < listDistParent:
                break
            else:
                temp = self.listDist[index]
                #write the parent to the child
                self.listDist[index] = self.listDist[parentIndex]
                #put temp into parent
                self.listDist[parentIndex] = temp
                #repeat for listNodes
                temp = self.listNodes[index]
                self.listNodes[index] = self.listNodes[parentIndex]
                self.listNodes[parentIndex] = temp
                index = parentIndex

    def deleteMin(self):
        #delete the piece at the top
        #move very last node to top
        #bubble it down
        self.listDist[0] = self.listDist[len(self.listDist) - 1]
        self.listNodes[0] = self.listNodes[len(self.listDist) - 1]
        self.listDist.pop(len(self.listDist) - 1)
        self.listNodes.pop(len(self.listNodes) - 1)
        index = 0
        while True:
            if index == len(self.listNodes) - 1:
                break
            #get lChild
            leftChildIndex = ((index + 1) * 2) - 1
            if self.listDist[leftChildIndex] < self.listDist[index]:
                temp = self.listDist[index]
                #write the parent to the child
                self.listDist[index] = self.listDist[leftChildIndex]
                #put temp into parent
                self.listDist[leftChildIndex] = temp
                #repeat for listNodes
                temp = self.listNodes[index]
                self.listNodes[index] = self.listNodes[leftChildIndex]
                self.listNodes[leftChildIndex] = temp
                index = leftChildIndex
                continue #this should skip the rest of the code
            rightChildIndex = (index + 1) * 2
            if self.listDist[rightChildIndex] < self.listDist[index]:
                temp = self.listDist[index]
                #write the parent to the child
                self.listDist[index] = self.listDist[rightChildIndex]
                #put temp into parent
                self.listDist[rightChildIndex] = temp
                #repeat for listNodes
                temp = self.listNodes[index]
                self.listNodes[index] = self.listNodes[rightChildIndex]
                self.listNodes[rightChildIndex] = temp
                index = rightChildIndex
            else:
                break




    def insert(self, newInsert, newDist):
        #place at the bottom, let it bubble up
        self.listNodes.append(newInsert)
        self.listDist.append(newDist)
        self.bubbleUp(len(self.listNodes) - 1)

    def makeQueue(self, newList, newListDist):
        #place in order and bubble up every node to make sure
        #that it's not larger than it's parent?
        self.listNodes.extend(newList)
        self.listDist.extend(newListDist)
        for i in range(len(self.listNodes)):
            self.bubbleUp(i)


    def decreaseKey(self, newKey, index):
        #move value down, compare it to its parents and let it bubble up
        self.listDist[index] = newKey
        self.bubbleUp(index)
        print("do nothing")