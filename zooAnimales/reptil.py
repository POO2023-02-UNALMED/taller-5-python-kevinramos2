from zooAnimales.animal import Animal
class Reptil(Animal):
  #contadores
  _list = []
  serpientes = 0
  iguanas = 0

  #atributos de la clase
  def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
    super().__init__(nombre, edad, habitat, genero)
    self.colorEscamas = colorEscamas
    self.largoCola = largoCola
    Reptil._list.append(self)

  #métodos