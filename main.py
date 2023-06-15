from cosas import Alumno, Perro

def main():
    al1 = Alumno("Jose", 19, "ICO")
    print(vars(al1))
    al1.__nombre = "Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))

    print("----------To String----------")
    print(al1)
    al1.estudiar(4)

print("----Perro----")
perro1 = Perro("Poodle", 2, 0.35)
print(vars(perro1))
perro1.raza = "De la calle"
print(vars(perro1))
cachorro = Perro.es_chachorro(perro1.edad)
print(cachorro)
perro2 = Perro()
Perro.dormir()
danes = Perro.perro_grande(0.8)
print(danes)

main()