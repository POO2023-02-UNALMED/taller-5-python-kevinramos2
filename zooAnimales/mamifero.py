from zooAnimales.animal import Animal
class Mamifero(Animal):
  #contadores
  _list = []
  caballos = 0
  leones = 0

  #atributos de la clase
  def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
    super().__init__(nombre,edad,habitat,genero)
    self.pelaje = pelaje
    self.patas = patas
    Mamifero._list.append(self)

  #métodos