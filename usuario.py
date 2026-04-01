class Usuario:
  def __init__(self, nombre, clave):
    self.nombre = nombre
    self.__clave = clave  # Atributo privado

  def cambiar_clave(self, vieja, nueva):
    if vieja == self.__clave:
      self.__clave = nueva
      return "Clave cambiada exitosamente."
    return "Clave actual incorrecta. No se pudo cambiar la clave."
  
user = Usuario("alejandro", "12345")
# print(user.__clave)  # Esto generará un error porque __clave es privado
print(user.cambiar_clave("12345", "54321"))  # Output: Clave cambiada exitosamente.


