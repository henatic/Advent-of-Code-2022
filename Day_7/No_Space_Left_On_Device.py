class Node:
    def __init__(self, parent):
         
        self.parent = parent
        self.file = []
        self.dir = []
   
    def addFile(self, file):
        self.file.append(file)

    def addDir(self, dir):
        self.dir.append(dir)

 # Utility function to create a new tree node.
def newNode(parent):   
    temp = Node(parent)
    return temp


if __name__=='__main__':

    nodeList = []

    f = open('input.txt', 'r')

    for x in f:
        cmd = x.strip()

        if cmd[0] == "$":
            if cmd[2] == 'c' and cmd[3] == 'd':
                pass