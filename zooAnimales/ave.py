from zooAnimales.animal import Animal
class Ave(Animal):
  #contadores
  _list = []
  halcones = 0
  aguilas = 0

  #atributos de clase
  def __init__(self, nombre, edad, habitat, genero, colorPlumas):
    super().__init__(nombre,edad,habitat,genero)
    self.colorPlumas = colorPlumas
    Ave._list.append(self)

  #métodos