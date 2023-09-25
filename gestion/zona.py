class Zona:
  #atributos de clase
  def __init__(self, nombre, zoo = None):
    self.nombre = nombre
    self.zoo = zoo
    self._animales = []
  
  #metodos

  def getNombre(self):
    return self.nombre
  def setNombre(self, nombre):
    self.nombre = nombre
  def getZoo(self):
    return self._zoo
  def setZoo(self, zoo):
    self._zoo = zoo
  def getAnimales(self):
    return self._animales
  def setAnimales(self, animales):
    return self._animales
  def agregarAnimales(self, animal):
    self._animales.append(animal)
  def cantidadAnimales(self):
    return len(self._animales)
    

  