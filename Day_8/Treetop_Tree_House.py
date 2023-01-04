f = open("input.txt")

treeGrid = f.readlines()

isSeen = list()

for x in treeGrid:
    lines = x.strip()
    myRow = list()
    for tree in lines:
        myRow.append((tree, False))
    isSeen.append(myRow)

line = 0
visibleTrees = 0

# while line < len(treeGrid) - 1:

#     row = treeGrid[line].strip()

#     if line == 0 or treeGrid[line] == treeGrid[-1]:
#         visibleTrees += len(treeGrid[line].strip())
#         index = 1
#         next = 1
#         if line == 0:
#             while index < len(row) - 1:
#                 while next < len(treeGrid) - 1 and treeGrid[next][index] < treeGrid[next - 1][index]:
#                     visibleTrees
#                     next += 1
#                 index += 1
#         else:

#         pass

    
#     treeIndex = 1
#     visibleTrees += 2

#     while treeIndex < len(row) - 1 and row[treeIndex] > row[treeIndex - 1]:
#         visibleTrees += 1
#         treeIndex += 1
    
#     lastTree = treeIndex
#     treeIndex = len(row) - 2

#     while treeIndex >= lastTree and row[treeIndex] > row[treeIndex + 1]:
#         visibleTrees += 1
#         treeIndex -= 1

#     line += 1

print("There are " + str(visibleTrees) + " visible trees.")