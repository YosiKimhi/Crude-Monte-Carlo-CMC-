#Yosi kimhi - 037973856
#Tal Waizman -038054029
import random
import copy

r=0
X=len('YosiKimhi')
Y=len('TalWaizman')

T1 = (X+100) % 21
T2 = (Y+100) % 21
T3 = (X*Y+100) % 21

print("Terminals: T1 = {}, T2 = {}, T3 = {}".format(T1,T2,T3))

## A Dictionary that Describes to given Graph
Graph = {1:{2:'O',16:'O',5:'O'},2:{1:'O',15:'O',3:'O'},3:{2:'O',13:'O',4:'O'},4:{3:'O',8:'O',5:'O'},
         5:{4:'O',6:'O',1:'O'},6:{5:'O',18:'O',7:'O'},7:{6:'O',9:'O',8:'O'},8:{7:'O',11:'O',4:'O'},
         9:{19:'O',10:'O',7:'O'},10:{9:'O',12:'O',11:'O'},11:{8:'O',10:'O',13:'O'},12:{20:'O',14:'O',10:'O'},
         13:{14:'O',3:'O',11:'O'},14:{15:'O',13:'O',12:'O'},15:{17:'O',2:'O',14:'O'},16:{1:'O',17:'O',18:'O'},
         17:{16:'O',15:'O',20:'O'},18:{16:'O',19:'O',6:'O'},19:{18:'O',20:'O',9:'O'},20:{19:'O',17:'O',12:'O'}, }


def searchPath(graph, start, end, path=[]):
    path = path + [start]
    if start not in graph:
        return False
    if start == end:
        return True
    for i in graph[start]:
        if i not in path:
            if searchPath(graph, i, end, path):
                return True
    return False

p=float(input('Enter p value: '))
valuesOfM = (1000, 10000)
for i, M in enumerate(valuesOfM):
    print("select {} for {}".format(i, M))
s = int(input("Select M: "))
M = valuesOfM[s]

def MonteCarlo(M,r,Graph,T1,T2,T3):
    for _ in range(M):
        copyOfGraph = copy.deepcopy(Graph)
        MC_graph = {}  
        # iterate over all the edges and set their state
        for v1 in range(1, 20):
            for v2 in copyOfGraph[v1]:
                if copyOfGraph[v1][v2] == 'O':
                    # random number
                    monte_carlo = random.uniform(0, 1)
                    if monte_carlo <= p:
                        copyOfGraph[v1][v2] = 'UP'  # each edge is represented twice
                        copyOfGraph[v2][v1] = 'UP'
                        if v1 not in MC_graph:
                            MC_graph[v1] = []
                        MC_graph[v1].append(v2)
                        if v2 not in MC_graph:
                            MC_graph[v2] = []
                        MC_graph[v2].append(v1)
                    else:
                        copyOfGraph[v1][v2] = 'DOWN'
                        copyOfGraph[v2][v1] = 'DOWN'
        # check if one vertex is connected to the other two, if it is so the system is up
        if (searchPath(MC_graph, T3, T1) and searchPath(MC_graph, T3, T2))  or (
            searchPath(MC_graph, T2, T1) and searchPath(MC_graph, T2, T3)) or (
            searchPath(MC_graph, T1, T2) and searchPath(MC_graph, T1, T3)):
            r = r + 1
    
    R = r / M
    print("Result:\n p = {}, M = {} ,R = {}".format(p,M,R))
    
MonteCarlo(M, r, Graph, T1, T2, T3)
