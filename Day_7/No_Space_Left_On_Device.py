class Node:
    def __init__(self, parent=None):
         
        self.parent = parent
        self.file = dict()
        self.dir = dict()
        self.fileMem = 0
   
    def addFile(self, filename, size):
        self.file[filename] = size
        self.fileMem += size
        self.updateMem(size)

    def updateMem(self, mem):
        currNode = self.parent
        while currNode.parent != None:
            currNode.fileMem += mem
            currNode = currNode.parent
        currNode.fileMem += mem

    def addDir(self, dirName):
        self.dir[dirName] = Node(self)

    def getParent(self):
        return self.parent

    def goto(self, dirName):
        return self.dir[dirName]

    def ifDirExist(self, dirName):
        if dirName in self.dir:
            return True
        return False

    def ifFileExist(self, fileName, size):
        if fileName in self.file and self.file[fileName] == size:
            return True
        return False

    def getMemSearch(self, rooty, rootMem):
        freeSpace = 70000000 - rootMem
        prevResult = [0,999999999999999999999999999999999] # 48381165
        for directory in rooty.dir.values():
            memory = directory.getMemSearch(directory, rootMem)
            prevResult[0] = memory[0] + prevResult[0]
            prevResult[1] = min(prevResult[1], memory[1])
        if rooty.fileMem <= 100000:
            prevResult[0] += rooty.fileMem
        freeSpace += rooty.fileMem
        if freeSpace >= 30000000 and rooty.fileMem != 0:
            prevResult[1] = min(rooty.fileMem, prevResult[1])
        return prevResult

if __name__=='__main__':

    f = open('input.txt', 'r')

    numRoot = 0

    for x in f:
        cmd = x.strip()

        if cmd[0] == "$":
            if cmd[2:4] == 'cd':
                if cmd[5:] == "..":
                    currDir = currDir.getParent()
                elif cmd[5:] == '/':
                    currDir = Node()
                    root = currDir
                else:
                    if currDir.ifDirExist(cmd[5:]) == False:
                        currDir.addDir(cmd[5:])
                    currDir = currDir.goto(cmd[5:])
        else:
            whiteSpaceIndex = cmd.find(' ')
            if cmd[0:whiteSpaceIndex] == 'dir':
                if currDir.ifDirExist(cmd[5:]) == False:
                    currDir.addDir(cmd[5:])
            elif currDir.ifFileExist(cmd[whiteSpaceIndex + 1:], int(cmd[0:whiteSpaceIndex])) == False:
                currDir.addFile(cmd[whiteSpaceIndex + 1:], int(cmd[0:whiteSpaceIndex]))
            else:
                print('Something\'s not right. We\'re at the line ' + cmd)
                exit(1)

    results = root.getMemSearch(root, root.fileMem)
    print("Part 1: " + str(results[0]) + "\nPart2: " + str(results[1]))
