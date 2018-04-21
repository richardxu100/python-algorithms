def dfs(node):
    node.visited = True
    print("%s ->" % node.name)

    for node in node.neighbors:
        if not node.visited:
            dfs(node)
