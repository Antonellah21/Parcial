class Graph:
    def __init__(self):
        self.adj_list = {}
        self.edges = []  

    def add_vertex(self, character):
        """Agrega un personaje como vértice al grafo."""
        if character not in self.adj_list:
            self.adj_list[character] = {}

    def add_edge(self, character1, character2, episodes):
        """Agrega una arista entre dos personajes con el número de episodios compartidos."""
        self.add_vertex(character1)
        self.add_vertex(character2)

        self.adj_list[character1][character2] = episodes
        self.adj_list[character2][character1] = episodes

        self.edges.append((episodes, character1, character2))

    def find_parent(self, parent, vertex):
        """Función para encontrar el padre de un vértice."""
        if parent[vertex] != vertex:
            parent[vertex] = self.find_parent(parent, parent[vertex])
        return parent[vertex]

    def union(self, parent, rank, u, v):
        """Función para realizar la unión de dos conjuntos."""
        root_u = self.find_parent(parent, u)
        root_v = self.find_parent(parent, v)

        if root_u != root_v:
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

    def kruskal_mst(self):
        """Calcula el árbol de expansión mínimo usando el algoritmo de Kruskal."""
        parent = {}
        rank = {}

        for character in self.adj_list:
            parent[character] = character
            rank[character] = 0

        self.edges.sort()

        mst = []  
        total_weight = 0

        for episodes, character1, character2 in self.edges:
            if self.find_parent(parent, character1) != self.find_parent(parent, character2):
                self.union(parent, rank, character1, character2)
                mst.append((character1, character2, episodes))
                total_weight += episodes

        return mst, total_weight

    def contains_character(self, mst, character):
        """Verifica si un personaje está en el árbol de expansión mínimo."""
        for u, v, episodes in mst:
            if u == character or v == character:
                return True
        return False

    def max_shared_episodes(self):
        """Determina el número máximo de episodios que comparten dos personajes."""
        max_episodes = 0
        pair = ()

        for episodes, character1, character2 in self.edges:
            if episodes > max_episodes:
                max_episodes = episodes
                pair = (character1, character2)

        return max_episodes, pair

    def display_graph(self):
        """Muestra el grafo en formato legible."""
        for character, edges in self.adj_list.items():
            for neighbor, episodes in edges.items():
                print(f"{character} -- {neighbor}: {episodes} episodios")

if __name__ == "__main__":
    graph = Graph()

    graph.add_edge("Luke Skywalker", "Darth Vader", 5)
    graph.add_edge("Luke Skywalker", "Yoda", 3)
    graph.add_edge("Luke Skywalker", "Leia", 4)
    graph.add_edge("Luke Skywalker", "Han Solo", 6)
    graph.add_edge("Darth Vader", "Yoda", 2)
    graph.add_edge("Darth Vader", "Boba Fett", 3)
    graph.add_edge("Leia", "Han Solo", 4)
    graph.add_edge("Leia", "C-3PO", 5)
    graph.add_edge("Han Solo", "Chewbacca", 7)
    graph.add_edge("Han Solo", "R2-D2", 2)
    graph.add_edge("Yoda", "BB-8", 1)
    graph.add_edge("Kylo Ren", "Leia", 2)
    graph.add_edge("Kylo Ren", "Darth Vader", 1)
    graph.add_edge("Chewbacca", "R2-D2", 3)

    print("Estructura del grafo de personajes de Star Wars:")
    graph.display_graph()

    mst, total_weight = graph.kruskal_mst()
    print("\nÁrbol de Expansión Mínimo (Kruskal):")
    for u, v, episodes in mst:
        print(f"{u} -- {v}: {episodes} episodios")
    print(f"Peso total del árbol de expansión mínimo: {total_weight}")

    yoda_in_mst = graph.contains_character(mst, "Yoda")
    print(f"\n¿El árbol de expansión mínimo contiene a Yoda? {'Sí' if yoda_in_mst else 'No'}")

    max_episodes, characters = graph.max_shared_episodes()
    print(f"\nNúmero máximo de episodios compartidos: {max_episodes} entre {characters[0]} y {characters[1]}.")