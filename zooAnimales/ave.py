from zooAnimales.animal import Animal
class Ave(Animal):
  #contadores
  _list = []
  halcones = 0
  aguilas = 0

  #atributos de clase
  def __init__(self, nombre, edad, habitat, genero, colorPlumas):
    super().__init__(nombre,edad,habitat,genero)
    self._colorPlumas = colorPlumas
    Ave._list.append(self)

  #métodos

  @classmethod
  def getList(cls):
    return cls._list
  @classmethod
  def setList(cls, list):
    cls._list = list
  
  def getColorPlumas(self):
    return self._colorPlumas
  def setColorPlumas(self, colorPlumas):
    self._colorPlumas = colorPlumas
  
  @classmethod
  def cantidadAves(cls):
    return len(cls._list)
  
  def movimiento(self):
    return "volar"
  
  #creacion de objetos
  @classmethod
  def crearHalcones(cls, nombre, edad, genero):
    ave = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    cls.halcones += 1
    return ave

  @classmethod
  def crearAguilas(cls, nombre, edad, genero):
    ave = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    cls.aguilas += 1
    return ave