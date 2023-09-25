class Zoologico:
  #atributos de clase
  def __init__(self, nombre, ubicacion):
    self.nombre = nombre
    self.ubicacion = ubicacion
    self._zona = []
  
  #métodos

  def getNombre(self):
    return self.nombre
  def setNombre(self, nombre):
    self.nombre = nombre
  def getUbicacion(self):
    return self.ubicacion
  def setUbicacion(self, ubicacion):
    self.ubicacion = ubicacion
  def getZona(self):
    return self._zona
  def setZona(self, zona):
    self._zona = zona
  def agregarZonas(self, zona):
    self._zona.append(zona)
  def cantidadTotalAnimales(self):
    canti = 0
    for zona in self._zona:
      canti += zona.cantidadAnimales()
    return canti