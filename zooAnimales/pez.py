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
  @classmethod
  def getList(cls):
    return cls._list
  @classmethod
  def setList(cls, list):
    cls._list = list
  
  def getColorEscamas(self):
    return self._colorEscamas
  def setColorEscamas(self, colorEscamas):
    self._colorEscamas = colorEscamas

  def getCantidadAletas(self):
    return self._cantidadAletas
  def setCantidadAletas(self, cantidadAletas):
    self._cantidadAletas = cantidadAletas
  
  def movimiento(self):
    return "nadar"
  
  @classmethod
  def cantidadPeces(cls):
    return len(cls._list)
  
  #creacion de objetos
  @classmethod
  def crearSalmon(cls, nombre, edad, genero):
    pez = Pez(nombre, edad, "oceano", genero, "rojo", 6)
    cls.salmones += 1
    return pez
  
  @classmethod
  def crearBacalao(cls, nombre, edad, genero):
    pez = Pez(nombre, edad, "oceano", genero, "gris", 6 )
    cls.bacalaos += 1
    return pez