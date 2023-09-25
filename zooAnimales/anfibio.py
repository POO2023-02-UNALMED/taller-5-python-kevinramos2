from zooAnimales.animal import Animal
class Anfibio(Animal):
  #contadores
  _list = []
  ranas = 0
  salamandras = 0
  #atributos de clase
  def __init__(self, nombre,edad, habitat, genero, colorPiel, venenoso):
    super().__init__(nombre, edad, habitat, genero)
    self.coloPiel = colorPiel
    self.venenoso = venenoso
    Anfibio._list.append(self)
  
  #métodos