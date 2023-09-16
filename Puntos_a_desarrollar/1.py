from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False


class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.elementos = self.elementos.copy()
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nombre_resultante = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nombre_resultante)
        nuevo_conjunto.elementos = elementos_comunes
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join([elemento.nombre for elemento in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"



