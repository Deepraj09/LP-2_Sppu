# Implement BFS and DFS 

# DFS Algorithm

def dfs(g,s):
    vis[s] = 1
    print(s)
    for c in g[s]:
        if not vis[c]:
            dfs(g,c)  # recursive call

vis = [0] * 5

def main():
    g = {
        0 : [1, 2],
        1 : [0 ,3, 4],
        2 : [3, 0],
        3 : [2, 1, 4],
        4 : [3,1]
    }

    print("DFS Sequence for the graph is ")
    dfs(g, 0)
    

if __name__ == "__main__":
    main()