#!/usr/local/bin/python3
from lib515 import *
from graphics import *
from optparse import OptionParser

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
#
# Drawing
#

def line(win, x1, y1, x2, y2) :
    graphic = Line(Point(x1, y1), Point(x2, y2))
    graphic.setWidth(3)
    graphic.draw(win)


def text(win, x, y, str, s) :
    graphic = Text(Point(x, y), str)
    graphic.setSize(s)
    graphic.draw(win)


## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
#
# the tree draw routines
#
def draw(names, merge, size, height, w, h, s) :
    win = GraphWin('tree', w, h, autoflush=False)   # autoflush requires udpate()
    win.setCoords(-.1*w, -.1*height[-1], 1.1*w, 1.1*height[-1])

    loc = len(merge)-1
    drawAux(win, loc, names, merge, size, height, w, w/2, s)

    update()
    win.getMouse()
#    win.save("tree.png")
    win.close()


def drawAux(win, loc, names, merge, size, height, width, x, s) :
    h = height[loc]
    m = merge[loc]
    if not isinstance(m, tuple) : 
        text(win, x, h, names[loc], s)
    else: 
        rightLoc = m[0]
        leftLoc = m[1]

        part = size[loc]
        leftWidth = size[leftLoc]/part*width
        rightWidth = size[rightLoc]/part*width

        leftEdge = x - width/2
        left = leftEdge + leftWidth/2
        rightEdge = leftEdge + leftWidth
        right = rightEdge + rightWidth/2

        # horizontal
        line(win, left, h, right, h)

        # vertical
        line(win, left, h, left, height[leftLoc])
        text(win, left, (h + height[leftLoc])/2, str(round(h-height[leftLoc], 1)), s)
        line(win, right, h, right, height[rightLoc])
        text(win, right, (h + height[rightLoc])/2, str(round(h-height[rightLoc], 1)), s)

        # subtrees
        drawAux(win, leftLoc, names, merge, size, height, leftWidth, left, s)
        drawAux(win, rightLoc, names, merge, size, height, rightWidth, right, s)



## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
#
# Build Tree
#
def calcD(i, j, size, dist) :
    di = dj = 0.0
    for z in range(0, size) :
        if z != i :
            if i > z :
                di += float(dist[i][z])
            else :
                di += float(dist[z][i])
				 
        if z != j :
            if j > z :
                dj += float(dist[j][z])
            else :
                dj += float(dist[z][j])

    ri = (1 / (size - 2)) * di 
    rj = (1 / (size - 2)) * dj
    D = dist[i][j] - (ri + rj)
    return D

def upgma(names, dist) :
    size = len(dist) * [1]             # size of clusters
    ok = len(dist) * [True]            # cluster used (combined with another) yet?
    height = len(dist) * [0]           # height in drawn tree of cluster with more than one element in them
    merge = list(range(0, len(dist)))  # The merged clusters

    # While there is more than one cluster left
    for joins in range(1, len(dist)) :

        theMin = None
        for i in range(0, len(dist)) :
            if ok[i] :
                for j in range(0, i) :
                    D = calcD(i, j, len(dist), dist)
                    if ok[j] and (theMin==None or D < theMin) : #dist[i][j]<theMin)  :
                        theMin = D #dist[i][j]
                        ij = (i, j)
        (i, j) = ij
        ok[i] = ok[j] = False

        # Merge $C_i \union C_j \rightarrow C_k$ where $k$ is a new cluster
        # number.
        k = len(dist)
        sizek = size[i]+size[j]     
        height.append(dist[i][j]/2)

        # Compute d_{k,z}  \forall z   remembering to keep all subscript pairs [a][b] so that b<a
        newrow = []
        for z in range(0, len(dist)) :
            if ok[z] :
                diz = dist[max(i, z)][min(i, z)]
                djz = dist[max(j, z)][min(j, z)]
                newrow.append((size[i] * diz + size[j] * djz)/sizek)
            else : 
                newrow.append(None)

        merge.append(ij)            # remember pair
        size.append(sizek)          # remember cluster size
        dist.append(newrow)            # add row k
        ok.append(True)             # mark it as available

    return (merge, size, height)



def main() :
    parser = OptionParser(usage = '''usage: %prog [options] file

This will generate a string with the same bigraph frequencies
of the input string.''')
    parser.add_option("-H", "--height", dest="h", default=800,
                      help = "height of window")
    parser.add_option("-W", "--width", dest="w", default=800,
                      help = "width of window")
    parser.add_option("-S", "--size", dest="s", default=28,
                      help = "size of text")
    (options, args) = parser.parse_args()
#     if len(args)!=1 :
#         print("ERROR(isit): file not specified.")
#         parser.print_help()
#         exit(1)
#     else :
#         filename = args[0]
    h = int(options.h)
    w = int(options.w)
    s = int(options.s)

    names = readListStr()
    dist = [[]]
    for i in range(0, len(names)-1) :
        dist.append(readListNum())

    (merge, size, height) = upgma(names, dist)
    print(merge)
    print(size)
    print(height)
    draw(names, merge, size, height, w, h, s)


main()