from zooAnimales.animal import Animal
class Mamifero(Animal):
  #contadores
  _list = []
  caballos = 0
  leones = 0

  #atributos de la clase
  def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
    super().__init__(nombre,edad,habitat,genero)
    self._pelaje = pelaje
    self._patas = patas
    Mamifero._list.append(self)

  #métodos
  @classmethod
  def getList(cls):
    return cls._list
  @classmethod
  def setList(cls, list):
    cls._list = list
  
  def isPelaje(self):
    return self._pelaje
  def setPelaje(self, pelaje):
    self._pelaje = pelaje
  
  def getPatas(self):
    return self._patas
  def setPatas(self, patas):
    self._patas = patas

  @classmethod
  def cantidadMamiferos(cls):
    return len(cls._list)
  
  #creacion de objetos
  @classmethod
  def crearCaballos(cls, nombre, edad, genero):
    mamifero = Mamifero(nombre, edad, "pradera",genero, True, 4 )
    cls.caballos += 1
    return mamifero
  
  @classmethod
  def crearLeones(cls, nombre, edad, genero):
    mamifero = Mamifero(nombre, edad, "selva", genero, True, 4)
    cls.leones += 1
    return mamifero