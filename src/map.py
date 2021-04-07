import folium
from folium import plugins
from Astar import *
from Graph import *
from File import *


def printPath(path):
    for x in path:
        print(x+1)


def inputRouteAstar(path, route_Astar):
    for idxNode in path:
        node = g1.nodes[idxNode]
        route_Astar.append([node.x, node.y])


def createMarkers(graph):
    # Create Markers
    i = 1
    heu = getHeuristic(graph, idxTo-1)
    for coor in graph.nodes:
        num = str(i)
        koordinat = str(coor.x) + " " + str(coor.y)
        folium.Marker([coor.x, coor.y],
                      popup=heu[i-1],
                      tooltip="Click for more info",
                      icon=plugins.BeautifyIcon(number=i,
                                                border_color='blue',
                                                border_width=2,
                                                text_color='red',
                                                inner_icon_style='margin-top:0px;')).add_to(map1)
        i = i + 1


# Create map object
g1 = convertTextToGraph("../test/AlunAlun.txt")

# peta ITB
# map1 = folium.Map(location=[-6.892650, 107.610433], zoom_start=20)

# peta AlunAlun
map1 = folium.Map(location=[-6.9219, 107.6070], zoom_start=20)


numOfNode = g1.getNumOfNode()

print("Masukkan satu angka diantara 1 sampai ", numOfNode)
idxFrom = int(input("Masukkan simpul mulai (dalam integer) : "))
idxTo = int(input("Masukkan simpul tujuan (dalam integer) : "))

while idxFrom < 1 or idxFrom > numOfNode or idxTo < 1 or idxTo > numOfNode:
    print("\nMasukkan tidak valid. Coba lagi\n")
    print("Masukkan satu angka diantara 1 sampai ", numOfNode)
    idxFrom = int(input("Masukkan simpul mulai (dalam integer) : "))
    idxTo = int(input("Masukkan simpul tujuan (dalam integer) : "))


createMarkers(g1)

#  peta ITB
# route_Graph = [
#     [-6.892650, 107.610433],  # 1
#     [-6.892650, 107.608763],  # 2
#     [-6.891056, 107.608712],  # 3
#     [-6.891057, 107.609713],  # 4
#     [-6.891037, 107.611024],  # 6
#     [-6.891057, 107.609713],  # 4
#     [-6.891934, 107.610388],  # 5
#     [-6.891362, 107.611052],  # 8
#     [-6.891037, 107.611024],  # 6
#     [-6.890978, 107.612087],  # 7
#     [-6.891355, 107.612193],  # 9
#     [-6.891362, 107.611052],  # 8
#     [-6.891355, 107.612193],  # 9
#     [-6.892427, 107.612027],  # 10
#     [-6.892650, 107.610433],  # 1
#     [-6.891934, 107.610388]   # 5
# ]

# peta AlunAlun
route_Graph = [
    [-6.921233, 107.607760], #1
    [-6.921036, 107.606462], #2
    [-6.920924, 107.605099], #3
    [-6.920855, 107.604080], #4
    [-6.922075, 107.604022], #5
    [-6.922405, 107.606410], #8
    [-6.922075, 107.604022], #5
    [-6.923119, 107.603942], #6
    [-6.923417, 107.606222], #7
    [-6.922405, 107.606410], #8
    [-6.922565, 107.607628], #9
    [-6.921233, 107.607760], #1
    [-6.922565, 107.607628], #9
    [-6.922687, 107.608433] #10
]

pathAndHeu = findPath(g1, idxFrom-1, idxTo-1)
path = pathAndHeu[0]
printPath(path)


route_Astar = []
inputRouteAstar(path, route_Astar)


# add route to map
folium.PolyLine(route_Graph).add_to(map1)

# add ant path route to map
plugins.AntPath(route_Astar).add_to(map1)

# Generate map
map1.save('map.html')
