class Animal:
  #contador 
  _totalAnimales = 0
  #atributos de clase
  def __init__(self, nombre, edad, habitat, genero):
    self.nombre = nombre
    self.edad = edad
    self.habitat = habitat
    self.genero = genero
    Animal._totalAnimales += 1
    self.zona = None
  
  #métodos

  @classmethod
  def getTotalAnimales(cls):
    return cls._totalAnimales
  @classmethod
  def setTotalAnimales(cls, totalAnimales):
    cls._totalAnimales = totalAnimales
  def getNombre(self):
    return self._nombre
  def setNombre(self, nombre):
    self._nombre = nombre
  def getEdad(self):
    return self._edad
  def setEdad(self, edad):
    self._edad = edad
  def getHabitat(self):
    return self._habitat
  def setHabitat(self, habitat):
    self._habitat = habitat
  def getGenero(self):
    return self._genero
  def setGenero(self, genero):
    self._genero = genero
  def getZona(self):
    return self._zona
  def setZona(self, zona):
    self._zona = zona
  def movimiento(self):
    return "desplazarse"
  
  #metodos para calcular el total de animales 