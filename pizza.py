# Métodos de Clase vs Estáticos

class Pizza:
  def __init__(self, ingredientes):
    self.ingredientes = ingredientes

  @classmethod
  def margarita(cls): # Creo una pizza predefinida
    return cls(["queso", "tomate"])
  
  @staticmethod
  def mensaje_bienvenida():
    return "¡Bienvenido a la pizzería!"
  

print(Pizza.mensaje_bienvenida()) # No necesito crear un objeto
mi_pizza = Pizza.margarita() # Uso el "atajo" de la clase
print(mi_pizza.ingredientes) # Output: ['queso', 'tomate']