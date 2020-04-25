import heapq as hq


class Graph:
    L = []
    N, M = 0, 0

    def get(self):
        self.N, self.M = [int(x) for x in input().split()]
        self.L.extend([] for x in range(self.N))
        for x in range(self.M):
            u, v, w = [int(x) for x in input().split()]
            self.L[u].append([w, v])
            self.L[v].append([w, u])

    def prim(self):
        src, total_weight = 0, 0
        heap, vis = [], []
        vis.extend(False for x in range(self.N))
        vis[src] = True
        for edge in self.L[src]:
            hq.heappush(heap, edge)
        for x in range(self.N - 1):
            total_weight += heap[0][0]
            src = heap[0][1]
            vis[src] = True
            hq.heappop(heap)
            for edge in self.L[src]:
                if not (vis[edge[1]]):
                    hq.heappush(heap, edge)
            while len(heap) and vis[heap[0][1]]:
                hq.heappop(heap)
        print(total_weight)


g = Graph()
g.get()
g.prim()
