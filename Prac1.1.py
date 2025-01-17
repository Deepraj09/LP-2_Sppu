# BFS Algorithm..

def bfs(g, s):
    q = [s]
    vis = [s]
    while q:
        cur = q.pop(0)
        print(cur)
        for c in g[cur]:
            if c not in vis:
                q.append(c)
                vis.append(c)

def main():
    g = {
        0 : [1, 2],
        1 : [0 ,3, 4],
        2 : [3, 0],
        3 : [2, 1, 4],
        4 : [3,1]
    }

    bfs(g,0)

if __name__ == "__main__":
    main()
