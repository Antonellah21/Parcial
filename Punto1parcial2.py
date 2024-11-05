class Pokemon:
    def __init__(self, nombre, numero, tipos, nivel=1):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos  
        self.nivel = nivel  

class BSTNode:
    def __init__(self, key, data):
        self.key = key
        self.data = [data]
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if not self.root:
            self.root = BSTNode(key, data)
        else:
            self._insert_recursive(self.root, key, data)

    def _insert_recursive(self, node, key, data):
        if key == node.key:
            node.data.append(data)  
        elif key < node.key:
            if node.left:
                self._insert_recursive(node.left, key, data)
            else:
                node.left = BSTNode(key, data)
        else:
            if node.right:
                self._insert_recursive(node.right, key, data)
            else:
                node.right = BSTNode(key, data)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node:
            return []
        if key == node.key:
            return node.data
        return self._search_recursive(node.left if key < node.key else node.right, key)

def get_pokemon_names_by_type(tree, tipo):
    result = []
    
    def _collect_pokemons(node):
        if node:
            if node.key.lower() == tipo.lower():
                result.extend(pokemon.nombre for pokemon in node.data)
            _collect_pokemons(node.left)
            _collect_pokemons(node.right)

    _collect_pokemons(tree.root)
    return result

def count_pokemons_by_type(tree, tipo):
    count = 0
    
    def _count_recursive(node):
        nonlocal count
        if node:
            if node.key.lower() == tipo.lower():
                count += len(node.data)
            _count_recursive(node.left)
            _count_recursive(node.right)

    _count_recursive(tree.root)
    return count

def search_pokemon_by_name_substring(tree, substring):
    result = []
    
    def _search_recursive(node):
        if node:
            if substring.lower() in node.key.lower():
                result.extend(node.data)
            _search_recursive(node.left)
            _search_recursive(node.right)

    _search_recursive(tree.root)
    return result

def list_pokemons_in_order(tree, key_func=lambda x: x):
    result = []
    
    def _in_order_traversal(node):
        if node:
            _in_order_traversal(node.left)
            result.extend(sorted(node.data, key=key_func))
            _in_order_traversal(node.right)
    
    _in_order_traversal(tree.root)
    return result

pokemons = [
    Pokemon("Bulbasaur", 1, ["Planta", "Veneno"], nivel=5),
    Pokemon("Charmander", 4, ["Fuego"], nivel=10),
    Pokemon("Squirtle", 7, ["Agua"], nivel=8),
    Pokemon("Pikachu", 25, ["Eléctrico"], nivel=15),
    Pokemon("Vaporeon", 134, ["Agua"], nivel=12),
    Pokemon("Flareon", 136, ["Fuego"], nivel=20),
    Pokemon("Jolteon", 135, ["Eléctrico"], nivel=18), 
    Pokemon("Lycanroc", 745, ["Roca"], nivel=14),  
    Pokemon("Tyrantrum", 697, ["Roca", "Dragón"], nivel=22),  
]

name_tree = BST()
number_tree = BST()
type_tree = BST()

for pokemon in pokemons:
    name_tree.insert(pokemon.nombre, pokemon)   
    number_tree.insert(pokemon.numero, pokemon) 
    for tipo in pokemon.tipos:
        type_tree.insert(tipo, pokemon)         

numero_buscado = 1
resultado_numero = number_tree.search(numero_buscado)
print(f"Resultado de búsqueda por número {numero_buscado}:")
for pokemon in resultado_numero:
    print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipo(s): {pokemon.tipos}, Nivel: {pokemon.nivel}")

nombre_buscado = "bul"
resultado_nombre = search_pokemon_by_name_substring(name_tree, nombre_buscado)
print(f"\nResultado de búsqueda por subcadena '{nombre_buscado}' en el nombre:")
for pokemon in resultado_nombre:
    print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipo(s): {pokemon.tipos}, Nivel: {pokemon.nivel}")

tipos_a_buscar = ["Agua", "Fuego", "Eléctrico", "Planta"]

for tipo in tipos_a_buscar:
    nombres_pokemons = get_pokemon_names_by_type(type_tree, tipo)
    print(f"Pokémon de tipo '{tipo}': {', '.join(nombres_pokemons) if nombres_pokemons else 'Ninguno'}")

print("\nListado de Pokémon por número (ascendente):")
for pokemon in list_pokemons_in_order(number_tree):
    print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipo(s): {pokemon.tipos}, Nivel: {pokemon.nivel}")

print("\nListado de Pokémon por nombre (ascendente):")
for pokemon in list_pokemons_in_order(name_tree):
    print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipo(s): {pokemon.tipos}, Nivel: {pokemon.nivel}")

print("\nListado de Pokémon por nivel (ascendente):")
for pokemon in list_pokemons_in_order(number_tree, key_func=lambda p: p.nivel):
    print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipo(s): {pokemon.tipos}, Nivel: {pokemon.nivel}")

pokemon_names_to_show = ["Jolteon", "Lycanroc", "Tyrantrum"]
print("\nDatos de los Pokémon solicitados:")
for nombre in pokemon_names_to_show:
    resultado = name_tree.search(nombre)
    if resultado:
        for pokemon in resultado:
            print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipo(s): {pokemon.tipos}, Nivel: {pokemon.nivel}")
    else:
        print(f"Pokémon '{nombre}' no encontrado.")

electric_count = count_pokemons_by_type(type_tree, "Eléctrico")
steel_count = count_pokemons_by_type(type_tree, "Acero")

print(f"\nNúmero de Pokémon de tipo 'Eléctrico': {electric_count}")
print(f"Número de Pokémon de tipo 'Acero': {steel_count}")
