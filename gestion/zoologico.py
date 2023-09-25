class Zoologico:
  #atributos de clase
  def __init__(self, nombre, ubicacion):
    self.nombre = nombre
    self.ubicacion = ubicacion
    self._zona = []
  
  #métodos