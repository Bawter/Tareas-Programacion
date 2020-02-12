def printr():
    print("\nMi Lista")
    num = 1
    for dict in sm:
        for q,t in dict.items():
            print(str(num) + ". " + q  + " , Cantidad: " + str(t)  )
        num += 1


if __name__ == "__main__":
    print("Lista de Supermercado")
    sm = []
    art = {}

    archivo = open("super.txt", "r")
    for linea in archivo:
        art[linea.rstrip('\n')] = 1
    for a,b in art.items():
        sm.append({a : b})
    print(sm)
    archivo.close()

    for n in range(5):
        articulo = input("Articulo: ")
        m = 0
        for q,t in art.items():
            if q.lower() == articulo.lower():
                mas = {q.capitalize() : t+1}
                sm[m].update(mas)
                art.update(mas)
                break
            elif m+1 == len(sm):
                new = {articulo.capitalize() : 1}
                sm.append(new)
                art.update(new)
                break
            m += 1

    printr()

    while True:
        try:
            opc = int(input("\nArt. por Eliminar (n): "))
        except:
            print("Numero invalido")
            opc = len(sm)+1
        if opc <= len(sm) and opc > 0:
            break
        else:
            print("Articulo no existe")

    [[key, value]] = sm[opc-1].items()
    print("\nEstariamos eliminando: " + key)
    sm.pop(opc-1)

    printr()

    while True:
        try:
            opc = int(input("\nArt. por Sustituir (n): "))
        except:
            print("Numero invalido")
            opc = len(sm)+1
        if opc <= len(sm) and opc > 0:
            break
        else:
            print("Articulo no existe")

    [[key, value]] = sm[opc-1].items()
    print("\nEstariamos sustituyendo: " + key)
    articulo = input("Nuevo Articulo: ")
    cambio = {articulo.capitalize() : value}
    sm[opc-1] = cambio

    printr()

    archivo = open("super.txt", "w")
    for a in sm:
        for q,t in a.items():
            archivo.write(q + "\n")
    archivo.close()
