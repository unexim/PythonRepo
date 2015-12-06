g = {"A":{"A":0, "B":3,"C":5, "D":999}, "B":{"A":3,"B":0,"C":999,"D":4}, "C":{"A":5,"B":999,"C":0,"D":999}, "D":{"A":999, "B":4, "C":999, "D":0}}

def dict2adj(g):
    node_list = g.keys()
    
    matrix=[]
    for node in g:
        matrix.append(g[node].values())
     
    return node_list, matrix

print dict2adj(g)

def write_graph_to_file(node_list, matrix, node_file, matrix_file):
    with open(node_file, 'w') as f:
        f.write(str(node_list.items()))
    
    with open(matrix_file, 'w') as f:
        for row in matrix:
            for element in row:
                f.write(str(element))
                f.write('\n')
        
write_graph_to_file(g, dict2adj(g), "graph.txt",  "matrix.txt")