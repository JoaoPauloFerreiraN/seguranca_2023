
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def buscaProfunda (Arv, compare_node, i):
  # Procura em profundidade
  start_node = i
  depth_limit = 10  #

  visited = set()
  queue = [(start_node, 0)]  # Tuple format: (node, depth)

  while queue:
    node, depth = queue.pop(0)
    if depth > depth_limit:
      break
    if node not in visited:
      #print("Node:", node, "Depth:", depth)
      visited.add(node)
      neighbors = Arv.neighbors(node)  # Get neighbors of the current node
      queue.extend((neighbor, depth + 1) for neighbor in neighbors)
      if np.array_equal(compare_node,node):
        return True
  return False

def possib (arr3):
  pos = np.argwhere(arr3==0)
  x = pos[0][0]
  y = pos[0][1]
  if ( x == 0 ): #Retorna um vetor de matrizes com os possiveis estados
    if (y ==0 ):
      next1_arr3 = arr3.copy()
      next1_arr3[0,1] , next1_arr3[0,0] = next1_arr3[0,0], next1_arr3[0,1]
      next2_arr3 = arr3.copy()
      next2_arr3[1,0] , next2_arr3[0,0] = next2_arr3[0,0], next2_arr3[1,0]
      resultsMatrix = np.array([next1_arr3,next2_arr3])
    elif ( y==1 ):
      next1_arr3 = arr3.copy()
      next1_arr3[0,0] , next1_arr3[0,1] = next1_arr3[0,1], next1_arr3[0,0]
      next2_arr3 = arr3.copy()
      next2_arr3[1,1] , next2_arr3[0,1] = next2_arr3[0,1], next2_arr3[1,1]
      next3_arr3 = arr3.copy()
      next3_arr3[0,2] , next3_arr3[0,1] = next3_arr3[0,1], next3_arr3[0,2]
      resultsMatrix = np.array([next1_arr3,next2_arr3,next3_arr3])
    else: #if ( y=2 ):
      next1_arr3 = arr3.copy()
      next1_arr3[0,2] , next1_arr3[0,1] = next1_arr3[0,1], next1_arr3[0,2]
      next2_arr3 = arr3.copy()
      next2_arr3[0,2] , next2_arr3[1,2] = next2_arr3[1,2], next2_arr3[0,2]
      resultsMatrix = np.array([next1_arr3,next2_arr3])
  elif ( x == 1 ):
    if (y ==0 ):
      next1_arr3 = arr3.copy()
      next1_arr3[1,0], next1_arr3[0,0] = next1_arr3[0,0], next1_arr3[1,0]
      next2_arr3 = arr3.copy()
      next2_arr3[1,0] , next2_arr3[1,1] = next2_arr3[1,1], next2_arr3[1,0]
      next3_arr3 = arr3.copy()
      next3_arr3[1,0] , next3_arr3[2,0] = next3_arr3[2,0], next3_arr3[1,0]
      resultsMatrix = np.array([next1_arr3,next2_arr3,next3_arr3])
    elif ( y == 1 ):
      next1_arr3 = arr3.copy()
      next1_arr3[1,1] , next1_arr3[1,0] = next1_arr3[1,0], next1_arr3[1,1]
      next2_arr3 = arr3.copy()
      next2_arr3[1,1] , next2_arr3[0,1] = next2_arr3[0,1], next2_arr3[1,1]
      next3_arr3 = arr3.copy()
      next3_arr3[1,1] , next3_arr3[1,2] = next3_arr3[1,2], next3_arr3[1,1]
      next4_arr3 = arr3.copy()
      next4_arr3[1,1] , next4_arr3[2,1] = next4_arr3[2,1], next4_arr3[1,1]
      resultsMatrix = np.array([next1_arr3,next2_arr3,next3_arr3,next4_arr3])
    else: #if ( y=2 ):
      next1_arr3 = arr3.copy()
      next1_arr3[1,2] , next1_arr3[0,2] = next1_arr3[0,2], next1_arr3[1,2]
      next2_arr3 = arr3.copy()
      next2_arr3[1,2] , next2_arr3[1,1] = next2_arr3[1,1], next2_arr3[1,2]
      next3_arr3 = arr3.copy()
      next3_arr3[1,2] , next3_arr3[2,2] = next3_arr3[2,2], next3_arr3[1,2]
      resultsMatrix = np.array([next1_arr3,next2_arr3,next3_arr3])
  else: #( x == 0 ):
    if ( y == 0 ):
      next1_arr3 = arr3.copy()
      next1_arr3[2,0] , next1_arr3[1,0] = next1_arr3[1,0], next1_arr3[2,0]
      next2_arr3 = arr3.copy()
      next2_arr3[2,0] , next2_arr3[2,1] = next2_arr3[2,1], next2_arr3[2,0]
      resultsMatrix = np.array([next1_arr3,next2_arr3])
    elif ( y == 1 ):
      next1_arr3 = arr3.copy()
      next1_arr3[2,1] , next1_arr3[2,0] = next1_arr3[2,0], next1_arr3[2,1]
      next2_arr3 = arr3.copy()
      next2_arr3[2,1] , next2_arr3[1,1] = next2_arr3[1,1], next2_arr3[2,1]
      next3_arr3 = arr3.copy()
      next3_arr3[2,1] , next3_arr3[2,2] = next3_arr3[2,2], next3_arr3[2,1]
      resultsMatrix = np.array([next1_arr3,next2_arr3,next3_arr3])
    else: #if ( y=2 ):
      next1_arr3 = arr3.copy()
      next1_arr3[2,2] , next1_arr3[1,2] = next1_arr3[1,2], next1_arr3[2,2]
      next2_arr3 = arr3.copy()
      next2_arr3[2,2] , next2_arr3[2,1] = next2_arr3[2,1], next2_arr3[2,2]
      resultsMatrix = np.array([next1_arr3,next2_arr3])
  #print(resultsMatrix)
  return resultsMatrix

def incrementaArvore (Arv, estados, profundidade, quantNo)->(int):
  j = 0
  if profundidade == -1:
    for i in range(estados.shape[0]):  # Adiciona os nós/estados ao pai
      Arv.add_node(i + quantNo, estado=estados[i])
      j += 1
    for i in range(j):
      Arv.add_edge('Inicial', i)
  else:
    for i in range(estados.shape[0]):  # Adiciona os nós/estados ao pai
      if buscaProfunda(Arv, estados[i], profundidade):
        print("No igual ao Avo")
      else:
        Arv.add_node(i + quantNo, estado=estados[i])
        j += 1
    for i in range(j):
      Arv.add_edge(profundidade, i + quantNo)
  return j



# arr = np.array([[0, 3, 1], [2, 5, 6], [4,7,8]]) #S/ Resposta
# arr = np.array([[2, 3, 1], [0, 5, 6], [4,7,8]]) # S/ Resposta
# arr = np.array([[1, 2, 3], [5, 0, 6], [4,7,8]]) # NODE 71 - 206 nodes criados = > 69 / 70
# arr = np.array([[2, 3, 0], [1, 5, 6], [4,7,8]]) # NODE 247 - 710 nodes criados = > 245 / 247
# arr = np.array([[4, 5, 8], [0, 1, 6], [7,2,3]]) # NODE
# arr = np.array([[6, 1, 7], [3, 2, 8], [0,4,5]]) # NODE
# arr = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]]) # NODE 6 - 5 nodes criados
arr = np.array([[1, 2, 3], [0, 5, 6], [4, 7, 8]]) # NODE 32 / 33
final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
#final = arr.copy()

Arv = nx.Graph() # Cia a arvore
profund = -1 # A profundidade inicial
quantNodes = 0 # Quantidade de Nós
Arv.add_node("Inicial", estado=arr) # Adiciona o estado inicial a raiz da arvore
result = possib(arr)  # Chama a função que retorna as jogadas possiveis

for i in range(5000000000):
  chave = 0
  quantIncrementada = incrementaArvore(Arv, result, profund, quantNodes)
  quantNodes += quantIncrementada
  profund += 1
  result = possib(Arv.nodes[i]["estado"])
  for k in range(result.shape[0]):
    if np.array_equal(final, result[k]):
      Arv.add_node(quantNodes, estado=result[k])
      Arv.add_edge(profund, quantNodes)
      profund += 1
      quantNodes+= 1
      chave = 1
      break
  if chave == 1:
    break
  # print(quantNodes)
shortest_path = nx.shortest_path(Arv, "Inicial", quantNodes-1)
print(shortest_path)

nodes_to_color_differently = shortest_path
edges_to_color_differently= []
for h in range(len(shortest_path)-1):
  edges_to_color_differently.append((shortest_path[h], shortest_path[h + 1]))
node_colors = ['red' if node in nodes_to_color_differently else 'skyblue' for node in Arv.nodes]
edge_colors = ['black' if edge not in edges_to_color_differently else 'red' for edge in Arv.edges]
posi = nx.spring_layout(Arv)
nx.draw(Arv, posi, with_labels=True, node_size=200, node_color=node_colors, font_size=10,edge_color=edge_colors, font_color="black", arrows=False)
plt.show()