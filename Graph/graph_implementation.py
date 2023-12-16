

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        # print("Graph dictionary : ", self.graph_dict)
    
    def get_path(self, start, end, path = []):

        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_path(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

        
    def short_distance(self, start, end, path = []):
        entire_path = self.get_path(start, end, path)

        short_path = []
        for i in range(len(entire_path)):
            if not short_path:
                short_path.append(entire_path[i])

            elif len(short_path[-1]) > len(entire_path[i]):
                short_path.pop()
                short_path.append(entire_path[i])

            elif len(short_path[-1]) == len(entire_path[i]):
                short_path.append(entire_path[i])

        return short_path



if __name__ == "__main__":


    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    print(route_graph.get_path("Mumbai", "Toronto"))
    print(route_graph.short_distance("Mumbai", "New York"))
    print(route_graph.short_distance("Mumbai", "Toronto"))

