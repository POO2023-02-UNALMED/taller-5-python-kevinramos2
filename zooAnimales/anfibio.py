from zooAnimales.animal import Animal
class Anfibio(Animal):
  #contadores
  _list = []
  ranas = 0
  salamandras = 0
  #atributos de clase
  def __init__(self, nombre,edad, habitat, genero, colorPiel, venenoso):
    super().__init__(nombre, edad, habitat, genero)
    self.colorPiel = colorPiel
    self.venenoso = venenoso
    Anfibio._list.append(self)
  
  #métodos

  @classmethod
  def getList(cls):
    return cls._list
  @classmethod
  def setList(cls, list):
    cls._list = list
  
  def getColorPiel(self):
    return self._colorPiel
  def setColorPiel(self, colorPiel):
    self.colorPiel = colorPiel
  
  def isVenenoso(self):
    return self._venenoso
  def setVenenoso(self, venenoso):
    self._venenoso = venenoso

  @classmethod
  def cantidadAnfibios(cls):
    return len(cls._list)
  
  def movimiento(self):
    return "saltar"
  
  #creación de objetos
  @classmethod
  def crearRana(cls, nombre, edad, genero):
    anfibio = Anfibio(nombre, edad, "selva", genero, "rojo", True)
    cls.ranas += 1
    return anfibio
  
  @classmethod
  def crearSalamandra(cls, nombre, edad, genero):
    anfibio = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    cls.salamandras += 1
    return anfibio