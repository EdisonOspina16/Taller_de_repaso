from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

# Ejemplo de uso
elemento1 = Elemento("Ejemplo")
elemento2 = Elemento("Ejemplo")
elemento3 = Elemento("OtroEjemplo")

print(elemento1 == elemento2)  # True, los nombres son iguales
print(elemento1 == elemento3)  # False, los nombres son diferentes


