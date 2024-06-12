dinosaurios = [
    {"nombre": "Tyrannosaurus Rex", "especie": "Theropoda", "peso": "7000 kg", "descubridor": "Barnum Brown", "ano_descubrimiento": 1902},
    {"nombre": "Triceratops", "especie": "Ceratopsidae", "peso": "6000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1889},
    {"nombre": "Velociraptor", "especie": "Dromaeosauridae", "peso": "15 kg", "descubridor": "Henry Fairfield Osborn", "ano_descubrimiento": 1924},
    {"nombre": "Brachiosaurus", "especie": "Sauropoda", "peso": "56000 kg", "descubridor": "Elmer S. Riggs", "ano_descubrimiento": 1903},
    {"nombre": "Stegosaurus", "especie": "Stegosauridae", "peso": "5000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1877},
    {"nombre": "Spinosaurus", "especie": "Spinosauridae", "peso": "10000 kg", "descubridor": "Ernst Stromer", "ano_descubrimiento": 1912},
    {"nombre": "Allosaurus", "especie": "Theropoda", "peso": "2000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1877},
    {"nombre": "Apatosaurus", "especie": "Sauropoda", "peso": "23000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1877},
    {"nombre": "Diplodocus", "especie": "Sauropoda", "peso": "15000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1878},
    {"nombre": "Ankylosaurus", "especie": "Ankylosauridae", "peso": "6000 kg", "descubridor": "Barnum Brown", "ano_descubrimiento": 1908},
    {"nombre": "Parasaurolophus", "especie": "Hadrosauridae", "peso": "2500 kg", "descubridor": "William Parks", "ano_descubrimiento": 1922},
    {"nombre": "Carnotaurus", "especie": "Theropoda", "peso": "1500 kg", "descubridor": "José Bonaparte", "ano_descubrimiento": 1985},
    {"nombre": "Styracosaurus", "especie": "Ceratopsidae", "peso": "2700 kg", "descubridor": "Lawrence Lambe", "ano_descubrimiento": 1913},
    {"nombre": "Therizinosaurus", "especie": "Therizinosauridae", "peso": "5000 kg", "descubridor": "Evgeny Maleev", "ano_descubrimiento": 1954},
    {"nombre": "Pteranodon", "especie": "Pterosauria", "peso": "25 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1876},
    {"nombre": "Quetzalcoatlus", "especie": "Pterosauria", "peso": "200 kg", "descubridor": "Douglas A. Lawson", "ano_descubrimiento": 1971},
    {"nombre": "Plesiosaurus", "especie": "Plesiosauria", "peso": "450 kg", "descubridor": "Mary Anning", "ano_descubrimiento": 1824},
    {"nombre": "Mosasaurus", "especie": "Mosasauridae", "peso": "15000 kg", "descubridor": "William Conybeare", "ano_descubrimiento": 1829},
]

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

    def tamano(self):
        return len(self.items)

def contar_especies(dinosaurios):
    especies = Pila()
    for dinosaurio in dinosaurios:
        especies.apilar(dinosaurio["especie"])

    especies_diferentes = set()
    while not especies.esta_vacia():
        especie = especies.desapilar()
        especies_diferentes.add(especie)

    return len(especies_diferentes)

def contar_descubridores(dinosaurios):
    descubridores = Pila()
    for dinosaurio in dinosaurios:
        descubridores.apilar(dinosaurio["descubridor"])

    descubridores_distintos = set()
    while not descubridores.esta_vacia():
        descubridor = descubridores.desapilar()
        descubridores_distintos.add(descubridor)

    return len(descubridores_distintos)


print("Número de especies diferentes:", contar_especies(dinosaurios))

print("Número de descubridores distintos:", contar_descubridores(dinosaurios))
print()
def mostrar_dinosaurios_con_T(dinosaurios):
    pila_resultado = Pila()
    for dinosaurio in dinosaurios:
        nombre = dinosaurio["nombre"]
        if nombre.startswith("T"):
            pila_resultado.apilar(nombre)
    return pila_resultado


def mostrar_dinosaurios_ligeros(dinosaurios):
    pila_resultado = Pila()
    for dinosaurio in dinosaurios:
        peso = int(dinosaurio["peso"].split()[0]) 
        if peso < 275:
            pila_resultado.apilar(dinosaurio["nombre"])
    return pila_resultado

def dinosaurios_con_letra_especifica(dinosaurios):
    letras_especificas = ['A', 'Q', 'S']
    pila_resultado = Pila()
    for dinosaurio in dinosaurios:
        nombre = dinosaurio["nombre"]
        primera_letra = nombre[0]
        if primera_letra in letras_especificas:
            pila_resultado.apilar(nombre)
    return pila_resultado

print("Dinosaurios que empiezan con T:")
pila_dinosaurios_T = mostrar_dinosaurios_con_T(dinosaurios)
while not pila_dinosaurios_T.esta_vacia():
    print(pila_dinosaurios_T.desapilar())

print("\nDinosaurios que pesan menos de 275 Kg:")
pila_dinosaurios_ligeros = mostrar_dinosaurios_ligeros(dinosaurios)
while not pila_dinosaurios_ligeros.esta_vacia():
    print(pila_dinosaurios_ligeros.desapilar())

print("\nDinosaurios que empiezan con A, Q, S:")
pila_dinosaurios_especificos = dinosaurios_con_letra_especifica(dinosaurios)
while not pila_dinosaurios_especificos.esta_vacia():
    print(pila_dinosaurios_especificos.desapilar())


