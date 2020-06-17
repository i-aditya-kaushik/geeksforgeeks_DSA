def temp_fun(i,visited,graph,stack):
    visited[i] = True
    for j in graph[i]:
        if visited[j]==0:
            temp_fun(j,visited,graph,stack)
    stack.insert(0,i)

def topoSort(n, graph):
    visited = [False]*n
    stack = []
    for i in range(n):
        if visited[i]==False:
            temp_fun(i,visited,graph,stack)
    return stack