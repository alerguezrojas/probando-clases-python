class Perro:
  def sonido(self):
    return "Guau!"
  
class Gato:
  def sonido(self):
    return "Miau!"
  
# Una función que acepta cualquier animal
def hacer_ruido(animal):
  print(animal.sonido())

mi_perro = Perro()
mi_gato = Gato()

hacer_ruido(mi_perro)  # Output: Guau!
hacer_ruido(mi_gato)   # Output: Miau!

