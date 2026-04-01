class CuentaBancaria:
  def __init__(self, titular, saldo_inicial):
    self.titular = titular
    self.saldo = saldo_inicial

  def depositar(self, cantidad):
    self.saldo += cantidad
    return f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}"
  
  def retirar(self, cantidad):
    if cantidad <= self.saldo:
      self.saldo -= cantidad
      return f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}"
    else:
      return f"Fondos insuficientes para realizar el retiro de {cantidad}. Saldo actual: {self.saldo}"
    
cuenta_paco = CuentaBancaria("Paco", 1000)
print(cuenta_paco.depositar(500))  # Output: Depósito de 500 realizado. Saldo actual: 1500
print(cuenta_paco.retirar(200))    # Output: Retiro de
print(cuenta_paco.retirar(2000))   # Output: Fondos insuficientes para realizar el retiro.