class cucaracha():
    tipo = 'blatodeos'
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuerpos = []
        self.vuela = []
        self.colores = []

    def agregar_cuerpo(self, cuerpo):
            self.cuerpos.append(cuerpo)

    def agregar_volar(self, volar):
            self.vuela.append(volar)

    def agregar_color(self, color):
            self.colores.append(color)
  

a = cucaracha('cucaracha')
b = cucaracha('cucaracha rinoceronte')
c = cucaracha('cucaracha gigante')
a.tipo
'blatodeos'
b.tipo
'blatodeos'
c.tipo
'blatodeos'
a.agregar_cuerpo('ovalado y aplanado')
b.agregar_cuerpo('ovalado y robusto')
c.agregar_cuerpo('ovalado y gigante')
a.cuerpos
['ovalado y aplanado']
b.cuerpos
['ovalado y robusto']
c.cuerpos
['ovalado y gigante']
a.agregar_volar('si vuelo wey, tengo alas')
b.agregar_volar('yo no wey, diosito me queria para otras cosas')
c.agregar_volar('wey cuando vuelo soy una cometa')
a.vuela
['si vuelo wey, tengo alas']
b.vuela
['yo no wey, diosito me queria para otras cosas']
c.vuela
['wey cuando vuelo soy una cometa']
a.agregar_color('soy castaño oscuro')
b.agregar_color('soy negro con un toque de castaño')
c.agregar_color('soy marron claro')
a.colores
['soy castaño oscuro']
b.colores
['soy negro con un toque de castaño']
c.colores
['soy marron claro']

if __name__ == "__main__":

    c = input("menu\nFavor ingresar tipo de cucaracha\n1. cucaracha \n2. cucaracha rinoceronte \n3. cucaracha gigante \n " )
    
    
    if (c == 1):
        print ("la cucaracha comun o cucaracha es la que se encuentra en las casas", a)

    elif (c == 2):
        print ("la cucaracha rinoceronte y no, no tiene cuernos", b)   
      
    elif (c == 3):
        print ("la curacha gigante, tambien hay en Panamá", c)

    else:
        print ("el animal que ha tratado de introducir no es valido por favor ingrese nuevamente")
     