from zooAnimales.animal import Animal
class Reptil(Animal):
  #contadores
  _list = []
  serpientes = 0
  iguanas = 0

  #atributos de la clase
  def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
    super().__init__(nombre, edad, habitat, genero)
    self._colorEscamas = colorEscamas
    self._largoCola = largoCola
    Reptil._list.append(self)

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

  def getLargoCola(self):
    return self._largoCola
  def setLargocola(self, largoCola):
    self._largoCola = largoCola

  def movimiento(self):
    return "reptar"
  
  @classmethod
  def cantidadReptiles(cls):
    return len(cls._list)
  
  #creacion de objetos

  @classmethod
  def crearSerpiente(cls, nombre, edad, genero):
    reptil = Reptil(nombre, edad, "jungla", genero, "blanco", 1 )
    cls.serpientes += 1
    return reptil
  
  @classmethod
  def crearIguana(cls, nombre, edad, genero):
    reptil = Reptil(nombre, edad, "humedal", genero, "verde", 3)
    cls.crearIguanas += 1
    return reptil
  
