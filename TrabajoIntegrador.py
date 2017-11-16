from Clases1 import *

def main ():
    barrio1 = Barrio()
    barrio1.SetCodigo(20)
    barrio1.SetNombre("Urquiza")
    barrio1.SetTipo("barrio")
    barrio1.SetPoblacion(10)
    barrio1.Agregar(barrio1)

    ciudad1 = Lugar()
    ciudad1.SetCodigo(15)
    ciudad1.SetNombre("Capital")
    ciudad1.SetTipo("ciudad")
    ciudad1.Agregar(barrio1)

    provincia1 = Lugar()
    provincia1.SetCodigo(10)
    provincia1.SetNombre("Buenos Aires")
    provincia1.SetTipo("provincia")
    provincia1.Agregar(ciudad1)

    pais1 = Lugar()
    pais1.SetCodigo(5)
    pais1.SetNombre("Argentina")
    pais1.SetTipo("pais")
    pais1.Agregar(provincia1)

    continente1 = Lugar()
    continente1.SetCodigo(0)
    continente1.SetNombre("America")
    continente1.SetTipo("continente")
    continente1.Agregar(pais1)


    barrio1.Borrar(barrio1)
    ciudad1.Borrar(ciudad1)
    provincia1.Borrar(provincia1)
    pais1.Borrar(pais1)

    continente1.Borrar(continente1)
    barrio1 = ciudad1.Modificar(20, nombre  = "Devoto")
    barrio1.GetPoblacion()

main()



























main()