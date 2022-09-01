#Se importan las clases del programa Fibonacci recursivo e iterativo
from FibonacciCP import fibonacci
from FibonacciRecursivo import fibonaccirecursivo

fibonacci(15)
print(fibonaccirecursivo(10))

#Las variables que se estaran probando son las de arreglo, donde se pruebe
#en que casos debe mostrar los valores iniciales y en que casos no
#Ademas se probara la variable num, que nos permite ver el rango hasta el
#que llegaremos a partir de las variables que nos muestra por default

#En fibonaccirecursivo se probara la variable n, dependiendo del valor ingresado


#id 1
"""Aqui se estara probando que al pedir una entrada de 0,
este debe arrojar un resultado nulo, en fibonacci tampoco debera arrojar
el arreglo inicial que incluye un 0 y un 1"""

fibonacci(0)
"""El resultado es el esperado pues al mandar a llamar la funcion no
arroja nada"""

#id 2

"""En este caso se estara probando que al pedir una entrada de 0,
este debe arrojar un resultado nulo, pero aqui mostrara
una salida de 0"""   
print(fibonaccirecursivo(0))
"""El resultado es el esperado pues al mandar a llamar la funcion nos
arroja un 0"""

#id 3

"""En este caso se estara probando que al pedir una entrada de x numero,
este debe arrojar solo el resultado de la suma de los dos numeros anteriores
que den al llegar al numero x ingresado
"""
print(fibonaccirecursivo(10))
"""El resultado es el esperado pues al mandar a llamar la funcion nos
arroja un 55, que esta es la suma del numero en la posicion 9 y 10, que es
21+34

Mismo resultado=Aprobado"""
