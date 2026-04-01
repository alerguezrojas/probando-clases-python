class Empleado:
  def __init__(self, nombre, sueldo, puesto="Empleado"):
    self.nombre = nombre
    self.sueldo = sueldo
    self.puesto = puesto
    

  def presentarse(self):
    return f"Hola, soy {self.nombre}, mi puesto es de {self.puesto} y mi sueldo es de {self.sueldo} euros."

# Gerente hereda de Empleado  
class Gerente(Empleado):
  def __init__(self, nombre, sueldo):
    super().__init__(nombre, sueldo, puesto="Gerente")

  def supervisar(self):
    return f"{self.nombre} está supervisando a su equipo."
  
empleado1 = Empleado("Juan", 2000)
print(empleado1.presentarse())  # Output: Hola, soy Juan y mi sueldo

jefe = Gerente("Marta", 3000)
print(jefe.presentarse())  # Output: Hola, soy Marta y mi sueldo es de 3000.
print(jefe.supervisar())    # Output: Marta está supervisando a su equipo.
