# Estefanía Ruiz Cuartas
# Lenguaje de programación: Python
# Tema: Programación orientada a objetos. Clases, objetos (instancias), método constructor (__init__())
# Fuentes de consulta: https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/#poo-clases-objetos     https://pythones.net/clases-y-metodos-python-oop/          https://www.youtube.com/watch?v=4GV20aOmbt4

# Programación orientada a objetos. Clases, objetos (instancias), método constructor (__init__()): 
print("Programación orientada a objetos (POO)\n")


# Comenzaremos por definir un poco algunos términos clave 

# Clase: modelos sobre los que se construyen objetos.
# Objetos: entidades que almacenan información en forma de argumento para atributos y realizan acciones organizadas a través de métodos
# Atributos: Variables de diferentes tipos (str,int,bool) cuyos valores pueden ser asignados por defecto o en la instancia de un objeto
# Los métodos: Son funciones; acciones realizables por el objeto que permiten cambiar sus atributos o el de otros objetos de la clase permitiendo un cambio de estado del objeto
# Instancia: creación de un objeto partiendo de una clase
# Método constructor: inicializar los atributos del objeto creado a partir de la clase que lo posea
# Parámetro self: se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método

# Ejercicio 1: Class Fiesta
print("\n- Ejercicio 1: Class Fiesta\n")

# Creación de la clase Fiesta, donde incluiremos algunos elementos fundamentales en una fiesta elegante. Para esto usamos la palabra clave 'class' y la acompañamos con el nombre elegido 'Fiesta'.
class Fiesta():
  # Uso del método constructor para definir e inicializar los atributos de la clase fiesta. Los parámetros que tendrá son: anfitrion,lugar,color,comida 
  def __init__(self,anfitrion,lugar,color,comida):
    # Creación de los atributos de la instancia. Están igualados a los parametros del método constructor, esto para que al crear el objeto, capture la información que trae y se le asigne al atributo correspondiente 
    self.anfitrion = anfitrion
    self.lugar = lugar
    self.color = color
    self.comida = comida

# Instancia 1, crearemos el objeto a mostrar
# Objeto 1: Fiesta para Carolina, de color aguamarina, será en el Dann Carlton, y se servirá salmón
fiesta1 = Fiesta("Carolina","Hotel Dann Carlton","aguamarina","salmon")

# Mostrar los atributos del objeto 1. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver 
print("Lugar de la fiesta1:\n",fiesta1.lugar)
print("\nColor temático de la fiesta1:\n",fiesta1.color)
print("\nAnfitrión de la fiesta1:\n",fiesta1.anfitrion)
print("\nComida a servir en la fiesta1:\n", fiesta1.comida)

# Ejercicio 2: Class Fiesta
print("\n","\n- Ejercicio 2: Class Fiesta\n")

# Instancia 2, crearemos el objeto a mostrar
# Objeto 2: Fiesta de Isabela, de color palo de rosa, se servirá filet mignon en el Hotel Intercotinental
fiesta2 = Fiesta("Isabela","Hotel Intercontinental","palo de rosa","filet mignon")

# Mostrar los atributos del objeto 2. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver
print("\nComida a servir en la fiesta2:\n", fiesta2.comida) 
print("\nAnfitrión de la fiesta2:\n",fiesta2.anfitrion)
print("\nColor temático de la fiesta2:\n",fiesta2.color)
print("\nLugar de la fiesta2:\n",fiesta2.lugar)

print("\n","----------"*7,"\n")

# Ejercicio 1: Class Salida
print("\n- Ejercicio 1: Class Salida\n")

# Creación de la clase Salida, con salida hacemos referencia a planes para salir el fin de semana. Para esto usamos la palabra clave 'class' y la acompañamos con el nombre elegido 'Salida'.
class Salida():
  # Uso del método constructor para definir e inicializar los atributos de la clase Salida. Los parámetros que tendrá son: plan,dia,hora,lugar, invitados
  def __init__(self,plan,dia,hora,lugar,invitados):
    # Creación de los atributos de la instancia. Están igualados a los parametros del método constructor, esto para que al crear el objeto, capture la información que trae y se le asigne al atributo correspondiente 
    self.plan = plan
    self.dia = dia
    self.hora = hora
    self.lugar = lugar
    self.invitados = invitados

# Instancia 1, crearemos el objeto a mostrar
# Objeto 1: Plan de salir a comer con amigos, dia sábado, restaurante Delirio, y será a las 7:00 pm
salida1 = Salida("salir a comer","sábado","19:00","restaurante Delirio","amigos")

# Mostrar los atributos del objeto 1. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver 
print("Hora de la salida1:\n",salida1.hora)
print("\nLugar de llegada:\n",salida1.lugar)
print("\nInvitados a la salida1:\n",salida1.invitados)
print("\nPlan de la salida1:\n", salida1.plan)
print("\nDía de la salida1:\n", salida1.dia)

# Ejercicio 2: Class Salida
print("\n","\n- Ejercicio 2: Class Salida\n")

# Instancia 2, crearemos el objeto a mostrar
# Objeto 2: Plan de salir de picnic en familia, dia lunes festivo, en la UVA del Tesoro, y será a las 15:00
salida2 = Salida("salir de picnic","lunes festivo","15:00"," UVA del Tesoro","familia")

# Mostrar los atributos del objeto 2. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver 
print("\nInvitados a la salida2:\n",salida2.invitados)
print("\nPlan de la salida2:\n", salida2.plan)
print("\nDía de la salida2:\n", salida2.dia)
print("\nLugar de llegada:\n",salida2.lugar)
print("\nHora de la salida2:\n",salida2.hora)
