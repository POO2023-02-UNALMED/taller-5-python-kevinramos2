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