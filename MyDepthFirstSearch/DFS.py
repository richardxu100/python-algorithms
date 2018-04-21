def dfs(node):
    node.visited = True 
    print("%s ->" % node.name)

    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor)