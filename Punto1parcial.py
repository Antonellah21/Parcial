def listar_inversa(lista):
    if not lista:
        return
    else:
        print(lista[-1])
        listar_inversa(lista[:-1])

mi_lista = [1, 2, 3, 4, 5]
listar_inversa(mi_lista)