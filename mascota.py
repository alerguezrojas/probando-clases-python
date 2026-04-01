class Mascota:
  def __init__(self, nombre, especie):
    self.nombre = nombre
    self.especie = especie

  def describir(self):
    return f"{self.nombre} es un {self.especie}"
  
mi_perro = Mascota("Bobby", "perro")
mi_gato = Mascota("Luna", "gato")

print(mi_perro.describir())  # Output: Bobby es un perro
print(mi_gato.describir())    # Output: Luna es un gato

