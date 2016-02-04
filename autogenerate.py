import os
import sys
import random
import string

colors = ["aliceblue", "antiquewhite1", "aquamarine1", "bisque", "blanchedalmond", "brown", "chartreuse", "crimson", "darkgoldenrod", "darkorange"]
def genName(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Node:
    def __init__ (self, f):
        self.name = genName()
        self.directedEdges = []
        #declare self with random attributes
        declaration = '"' + self.name + '" [sides=' + str(random.randint(0,10)) + ', distortion="' + str(random.uniform(-1,1)) + '", orientation=' + str(random.randint(10,60)) + ', skew="' + str(random.uniform(-1,1)) + '", color=' + colors[random.randint(0,len(colors)-1)] + ' ] \n'
        f.write(declaration)
    def setChild(self, child):
        self.directedEdges.append(child)
        f.write('"' + self.name + '" -> "' + child.name + '"')

def tree(f, numNodes):
    root = Node(f)
    openNodes = [root]
    nodesUsed = 1
    while (nodesUsed < numNodes):
        parent = openNodes[random.randint(0,len(openNodes)-1)]
        child = Node(f)
        nodesUsed+=1
        parent.setChild(child)
        openNodes.append(child)
        if (len(parent.directedEdges) == 2):
            openNodes.remove(parent)


def disconnected(f, numNodes, numEdges):
    nodesUsed = 0
    edgesUsed = 0
    openNodes = []
    while (nodesUsed < numNodes):
        child = Node(f)
        nodesUsed+=1
        openNodes.append(child)
    while (edgesUsed < numEdges):
        node = openNodes[random.randint(0,len(openNodes)-1)]
        node.setChild(openNodes[random.randint(0,len(openNodes)-1)])
        edgesUsed+=1



if __name__ == '__main__':
    #creates file named temp.dot
    #argv[0] is the file
    #argv[1] is the number of nodes
    #argv[2] is the type of graph you are looking to generate. Options are tree, clique, planar, bipartite, disconnected
    #argv[3] is the number of edges per node from 0 to 5, as a double. Only works with fullrandom(for now)
    if (len(sys.argv) > 2 and len(sys.argv) < 5 and int(sys.argv[1]) > 0):
        numNodes = sys.argv[1]
        graphType = sys.argv[2]
        f = open('temp.dot', 'w')
        opener = 'digraph G { \n node [	shape = polygon, sides = 4, distortion = "0.0", orientation = "0.0", skew = "0.0", color = white, style = filled, fontname = "Helvetica-Outline" ] \n'
        f.write(opener)
        if (sys.argv[2] == "tree"):
            tree(f, int(numNodes))
        elif(sys.argv[2] == "disconnected"):
            edgeDensity = numNodes
            if (len(sys.argv) == 4):
                edgeDensity = int(float(sys.argv[3]) * float(numNodes))
            disconnected(f,int(numNodes),edgeDensity)
        f.write("}")




    else:
        print "Usage: python autogenerate.py NumberOfNodes TypeOfGraph EdgeDensity \n" + "Types of Graphs: tree, clique, planar, bipartite, disconnected \n" + "note EdgeDensity only works will full random right now"
