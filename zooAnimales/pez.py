from zooAnimales.animal import Animal
class Pez(Animal):
  #contadores
  _list = []
  salmones = 0
  bacalaos = 0

  #atributos de la clase
  def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
    super().__init__(nombre, edad, habitat, genero)
    self.colorEscamas = colorEscamas
    self.cantidadAletas = cantidadAletas
    Pez._list.append(self)

  #métodos